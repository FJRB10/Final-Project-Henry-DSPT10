# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación
COPY . .

# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Expone el puerto en el que escucha la aplicación
EXPOSE 8080

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
