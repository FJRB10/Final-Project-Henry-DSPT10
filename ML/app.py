import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import Counter
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim.parsing.preprocessing import STOPWORDS  # Stopwords de Gensim
from google.cloud import storage
from google.oauth2 import service_account
import os

# Configuración de PyTorch
os.environ['PYTORCH_JIT'] = '0'

# Cargar modelos de lenguaje
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()

# Credenciales de Google Cloud
credentials = service_account.Credentials.from_service_account_file(
    'C:/Users/Agustin/Desktop/PF/ML/utopian-honor-438417-u7-5b7f84fcfd25.json'
)
client = storage.Client(project='utopian-honor-438417-u7', credentials=credentials)

# Función para descargar archivo del bucket
def descargar_archivo(bucket_name, archivo_name):
    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(archivo_name)
        archivo_local = f"./{archivo_name}"
        blob.download_to_filename(archivo_local)
        return archivo_local
    except Exception as e:
        st.error(f"Error al descargar el archivo {archivo_name}: {e}")
        raise

# Función para procesar reseñas y generar gráficos de pastel
def procesar_reseñas(reseñas, tipo):
    textos = reseñas['frase']
    quejas = {"Food": [], "Service": [], "Ambience": [], "Prices": [], "Organization": []}
    alabanzas = {"Food": [], "Service": [], "Ambience": [], "Prices": []}
    
    for texto in textos.dropna():
        sentimiento = sia.polarity_scores(texto)
        doc = nlp(texto)
        for sent in doc.sents:
            if sentimiento["compound"] < 0:  # Reseñas negativas
                for token in sent:
                    if token.pos_ in ["NOUN", "ADJ"]:
                        if token.text.lower() in ["food", "meal", "dish", "cuisine"]:
                            quejas["Food"].append(token.text)
                        elif token.text.lower() in ["service", "staff", "waiter", "server"]:
                            quejas["Service"].append(token.text)
                        elif token.text.lower() in ["ambience", "atmosphere", "environment"]:
                            quejas["Ambience"].append(token.text)
                        elif token.text.lower() in ["price", "cost", "value"]:
                            quejas["Prices"].append(token.text)
                        elif token.text.lower() in ["organization", "management", "operation"]:
                            quejas["Organization"].append(token.text)
            elif sentimiento["compound"] > 0:  # Reseñas positivas
                for token in sent:
                    if token.pos_ in ["NOUN", "ADJ"]:
                        if token.text.lower() in ["ambience", "atmosphere", "environment"]:
                            alabanzas["Ambience"].append(token.text)
                        elif token.text.lower() in ["food", "meal", "dish", "cuisine"]:
                            alabanzas["Food"].append(token.text)
                        elif token.text.lower() in ["service", "staff", "waiter", "server"]:
                            alabanzas["Service"].append(token.text)
                        elif token.text.lower() in ["price", "cost", "value"]:
                            alabanzas["Prices"].append(token.text)

    if tipo == 'positivos':
        etiquetas = alabanzas.keys()
        tamaños = [len(alabanza) for alabanza in alabanzas.values()]
        cmap = plt.get_cmap('Blues')
    elif tipo == 'negativos':
        etiquetas = quejas.keys()
        tamaños = [len(queja) for queja in quejas.values()]
        cmap = plt.get_cmap('Reds')

    if sum(tamaños) == 0:
        st.warning(f"No hay datos suficientes para generar un gráfico de {tipo}.")
        return

    porcentajes = [tam / sum(tamaños) * 100 for tam in tamaños]
    norm = mcolors.Normalize(vmin=min(porcentajes), vmax=max(porcentajes))
    colores = [cmap(norm(porcentaje)) for porcentaje in porcentajes]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(tamaños, labels=[f"{etiqueta}\n({porcentaje:.1f}%)" for etiqueta, porcentaje in zip(etiquetas, porcentajes)], colors=colores, autopct=None, textprops={'fontsize': 12})
    ax.set_title("Frecuencia de Alabanzas" if tipo == 'positivos' else "Frecuencia de Quejas")
    ax.axis('equal')

    st.pyplot(fig)


# Función para analizar y mostrar el resultado más importante gráficamente
def analizar_y_mostrar_principal(reseñas, tipo, top_n=5):
    textos = reseñas['frase']
    sustantivos_adjetivos = {}

    # Extraer sustantivos y adjetivos
    for texto in textos.dropna():
        doc = nlp(texto)
        for token in doc:
            if token.pos_ == "NOUN":  # Buscar sustantivos
                adjetivos = [child.text.lower() for child in token.children if child.pos_ == "ADJ"]
                if token.text.lower() not in sustantivos_adjetivos:
                    sustantivos_adjetivos[token.text.lower()] = adjetivos
                else:
                    sustantivos_adjetivos[token.text.lower()].extend(adjetivos)

    # Determinar el sustantivo más frecuente
    sustantivo_mas_relevante = max(sustantivos_adjetivos, key=lambda k: len(sustantivos_adjetivos[k]))
    adjetivos_asociados = sustantivos_adjetivos[sustantivo_mas_relevante]

    # Contar frecuencias de adjetivos
    adjetivos_frecuencias = Counter(adjetivos_asociados).most_common(5)  # Top 5 adjetivos más comunes
    adjetivos, frecuencias = zip(*adjetivos_frecuencias)  # Separar en listas

    total_adjetivos = sum(frecuencias)
    porcentajes = [freq / total_adjetivos * 100 for freq in frecuencias]

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(adjetivos, frecuencias, color='skyblue' if tipo == "alabanzas" else 'salmon')

    # Crear gráfico
    for i, bar in enumerate(bars):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, f'{porcentajes[i]:.1f}%', ha='center', va='bottom', fontsize=12)
    
    ax.set_title(f"{tipo.capitalize()} - de {sustantivo_mas_relevante}", fontsize=16)
    ax.set_xlabel("Adjetivos Asociados", fontsize=12)
    ax.set_ylabel("Frecuencia", fontsize=12)
    ax.tick_params(axis='x', labelrotation=45)
    
    # Mostrar gráfico en Streamlit
    st.pyplot(fig)

    # Mostrar texto explicativo
    st.write(f"**{tipo.capitalize()}**: El sustantivo más importante es '{sustantivo_mas_relevante}', descrito frecuentemente como:")
    st.write(", ".join([f"{adj} ({freq} veces, {porc:.1f}%)" for adj, freq, porc in zip(adjetivos, frecuencias, porcentajes)]))


# Ejecución principal
try:
    st.write("Cargando configuración inicial...")
    bucket_name = 'review_main_cities'
    ciudades = ['Nueva York', 'California', 'Florida', 'Texas']
    archivo_dict = {
        'Nueva York': {'positivos': 'comentarios_positivos_NY.csv', 'negativos': 'comentarios_negativos_NY.csv'},
        'California': {'positivos': 'comentarios_positivos_CA.csv', 'negativos': 'comentarios_negativos_CA.csv'},
        'Florida': {'positivos': 'comentarios_positivos_FL.csv', 'negativos': 'comentarios_negativos_FL.csv'},
        'Texas': {'positivos': 'comentarios_positivos_TX.csv', 'negativos': 'comentarios_negativos_TX.csv'}
    }

    # Selección de ciudad
    ciudad_seleccionada = st.selectbox('Selecciona una ciudad o estado:', ciudades)
    st.write(f"Has seleccionado: {ciudad_seleccionada}")

    # Botón para confirmar la selección
    if st.button("Iniciar análisis"):
        st.write("Cargando datos de los archivos...")
        archivo_bucket = archivo_dict[ciudad_seleccionada]

        archivo_positivos = descargar_archivo(bucket_name, archivo_bucket['positivos'])
        archivo_negativos = descargar_archivo(bucket_name, archivo_bucket['negativos'])
        st.success("Archivos cargados exitosamente.")

        st.write("Procesando datos cargados...")
        reseñas_positivas = pd.read_csv(archivo_positivos, on_bad_lines='warn')
        reseñas_negativas = pd.read_csv(archivo_negativos, on_bad_lines='warn')
        st.success("Datos procesados exitosamente.")

        st.write("Analizando reseñas positivas...")
        procesar_reseñas(reseñas_positivas, 'positivos')
        st.success("Análisis de reseñas positivas completado.")

        st.write("Analizando reseñas negativas...")
        procesar_reseñas(reseñas_negativas, 'negativos')
        st.success("Análisis de reseñas negativas completado.")

        st.write("Generando resultados de alabanzas...")
        analizar_y_mostrar_principal(reseñas_positivas, "alabanzas")
        st.success("Resultados de alabanzas generados.")

        st.write("Generando resultados de críticas...")
        analizar_y_mostrar_principal(reseñas_negativas, "críticas")
        st.success("Resultados de críticas generados.")

except Exception as e:
    st.error(f"Error: {e}")

