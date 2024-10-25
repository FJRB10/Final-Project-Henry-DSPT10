# Consultora Socius Lab

![Logo Socius Lab](./Images/LOGO%20(color).png)

## Alcance del proyecto
Las tareas que se realizarán en este proyecto están documentadas en el tablero de actividades de Trello, algunas de estas son:

* Formulación de minimo 3 KPI's.
* Análisis preliminar de los datos.
* Análisis EDA.
* ETL Completo.
* Pipeline del ETL.
* Diseño del modelo Entidad Relación.
* Dashboard.
* Modelo de ML.

El objetivo final de este proyecto es desarrollar un MVP (Producto Mínimo Viable) que recomiende al usuario en qué lugar de una ciudad invertir para crear un negocio en un rubro específico que él mismo seleccione. Este MVP consistirá en un dashboard que mostrará insights obtenidos a partir de los datos recopilados de Google Maps y Yelp. Además, se integrará un modelo de Machine Learning (ML), el cual proporcionará las mejores recomendaciones al usuario.

Dado que este proyecto es un MVP, se utilizarán solo algunos datos. Específicamente, se trabajará con datos de una sola ciudad y se considerarán únicamente dos sectores.

## Equipo de trabajo - Roles y responsabilidades
* <a href = "https://github.com/DomiAndi"> Leslie Andrea </a> - Data Analyst
* <a href = "https://github.com/matiasbarriosled"> Matias Barrios </a> - Data Engineer
* <a href = "https://github.com/moralespbl"> Pablo Morales </a> - ML Engineer
* <a href = "https://github.com/AgustinNiederle"> Agustin Niederle </a> - Data Scientist
* <a href = "https://github.com/FJRB10"> Francisco Ramirez </a> - Analista Funcional

## Metodología de trabajo
La metodología de trabajo que se decidió utilizar está basada en Scrum, ya que todo el equipo tiene una reunión diaria. Sin embargo, esta reunión excede el tiempo estipulado por Scrum para una daily; en este caso, la reunión diaria dura entre 45 y 60 minutos. En esta reunión se expone el avance logrado, los problemas encontrados, cómo se resolvieron o si aún no se ha encontrado una solución, y finalmente, se discute con qué se continuará.

Las tareas que se deben realizar por cada sptint se ingresan en la aplicación Trello y se asigna a la persona o personas encargadas de dicha tarea. La tarea solo puede tener 3 estados dentro de la aplicación de Trello y son:

* Por hacer (To Do)
* Haciendo (Doing)
* Hecho (Done)

Además para saber cuanto es la duración aproximada de cada tarea se realizo un diagrama de Gannt en la aplocación Gantter de Google y la aplicación Trello también nos permite visualizar un diagrama de Gannt de acuerdo a la duración de las actividades.

## Cronograma general - GANNT
<table>
    <tr>
        <td> <img src = "https://www.conectasoftware.com/wp-content/uploads/2021/04/Trello-Emblema-1300x867.png" alt = "Logo de Trello" Width = "700"> </td>
        <td> <img src = "https://lh3.googleusercontent.com/-kTfFzkEzgx4/WAo2rS97EUI/AAAAAAAAAQs/6pDmnPbfJLUxSHsqpaE9OrEdcPhIegGaQCMYCGAYYCw/s400/g256x256.png" alt = "Logo de Gantter" width = "700"> </td>
    </tr>
    <tr style="text-align: center;">
        <td> <a href = "https://trello.com/b/dt6k7HK2/proyectofinal"> Tablero de actividades </a> </td>
        <td> <a href = "https://google.gantter.com/gantterforgoogleapps/index.html?fileID=19jRy4hklzPthEojqQ-HWhzz0Tj3s3t6I#amode=normal&fileID=19jRy4hklzPthEojqQ-HWhzz0Tj3s3t6I"> Diagrama de Gantt </a> </td>
    </tr>
</table>


## Análisis preliminar de los datos
### Datasets de Google Maps
### Metadata de sitios
Las siguientes observaciones son de los datos sin hacer ninguna modificación o alteración.

1. **Valores Nulos y Vacíos**:
   - Varias columnas, como `description`, `price`, y `hours`, presentan un alto número de valores nulos. En particular, la columna `description` tiene un 91.59% de valores nulos, lo que indica que la mayoría de las entradas no tienen descripción. En concecuencia estos datos habra que analizar su utilidad en el analisis.
   - La columna `price` también tiene un alto porcentaje de valores nulos (90.90%).
   - La columna `city` contiene 80914 valores nulos.
   - `name` tiene un bajo número de valores nulos (37).

2. **Duplicados**:
   - La columna `gmap_id` tiene 53,156 valores duplicados, lo que sugiere que hay múltiples registros asociados con la misma identificación de Google Maps. Este tipo de duplicados podría ser un área de preocupación si se necesita unicidad en la identificación de lugares.

3. **Columnas Numéricas**:
   - Las columnas `latitude` y `longitude` tienen un rango amplio de valores, con latitudes que van desde -40.93 hasta 87.86 y longitudes desde -178.81 hasta 180.0. Esto puede ser esperado, pero es importante validar que todos los registros caen dentro de las coordenadas geográficas válidas.
   - La columna `avg_rating` tiene una media de 4.30, lo que sugiere una percepción mayormente positiva en la evaluación de los lugares.

4. **Valores Vacíos**:
   - Hay una cantidad mínima de valores vacíos en las columnas, lo que indica que la mayoría de las entradas están completas en este aspecto. Sin embargo, la columna `city` tiene 687 valores vacíos, lo que podría ser relevante si se realizan análisis geográficos.

5. **Observaciones Generales**:
   - Alta proporción de valores nulos en columnas clave como `description`, `price`, y `MISC`.

6. **Columnas con datos anidados:**
   - `MISC`, `Category`, `hours` y `relative_results`

Las siguientes observaciones son una vez eliminados todos los duplicados de los datos.

Comparando con el informe anterior, las principales diferencias son:

1. **Total de Registros**: El número total de registros ha disminuido de **3,025,011** a **2,998,428**.

2. **Valores Nulos en `address`**: La cantidad de valores nulos en `address` ha disminuido ligeramente, de **80,511** a **79,520**, lo que representa un cambio mínimo en la calidad de esta columna.

3. **Valores Nulos en `description`**: El porcentaje de valores nulos en `description` se mantiene alto, con **2,745,412** valores nulos, lo que equivale al **91.56%** de los registros, sin cambios significativos.

4. **Valores Nulos en `price`**: El número de valores nulos en `price` ha disminuido, de **2,749,808** a **2,724,510**, lo que indica que todavía hay un alto porcentaje de datos faltantes.

5. **Duplicados en `address`**: La cantidad de duplicados en `address` ha aumentado, de **57,210** a **6,106**, lo que sugiere que a pesar de la eliminación de registros, todavía hay duplicados en esta columna.

6. **Duplicados en `gmap_id`**: La columna `gmap_id` ahora muestra **0** duplicados, indicando que se ha mantenido la unicidad en esta columna, lo cual es un punto positivo en comparación con la versión anterior.

7. **Valores Nulos en `state`**: El número de valores nulos en `state` ha disminuido, de **746,455** a **738,858**, lo que indica una ligera mejora en la completitud de esta columna.

En resumen, el nuevo informe muestra una ligera mejora en algunas columnas, pero persisten problemas significativos de nulos y duplicados en columnas clave, lo que requiere atención adicional. Otros como `desciption` o `price` contienen un elevado porcentaje de valores nulos (91% y 90%) seguido por `hours` (26%) y `MISC`.

### Datasets de Yelp
Desde el dataset de Google Maps se encontro que las ciudades con más reseñas son:
* **Houston**
* **New York**
* **Chicago**
* **Los Angeles**
* **Brooklyn**
* **San Antonio**
* **Dallas**
* **Las Vegas**
* **Miami**
* **Philadelphia**

Con estas ciudades se filtro la data de los datasets de Yelp.

### Reviews
1. Se verifico si existían valores nulos o vacios en el dataset *review*.
    * Se encontro que no habían valores nulos o vacios en ninguna de las columnas, por lo que se procede a revisar la cantidad de duplicados.

2. Se revisa la cantidad de duplicados para las columnas review_id y text.
    * Para la columna review_id no se encontro ningún duplicado, pero para la columna text se encontraron 3450 duplicados.
    * Se hayaron los inidces de esos registros duplicados y se procede a revisar que más se puede encontrar en estos registros.

3. Se eligieron dos registros de la columna text al azar para revisar sus demás características (columnas).
    * Se encontro que los datos son casi identicos en todas sus características, lo unico que suele cambiar es la fecha y el review_id, por lo que podriamos decir que son datos que se ingresaron mal por algun bug de la aplicacion.


### Users
1. Se reviso solo la columna user_id, la cual no debería tener duplicados.
    * Se observo que hay un total de 10298 duplicados para la columna user_id.

2. Se removieron la cantidad de duplicados y se verificao si había nulos o vacios.
    * No se encontraron nulos o vacios en ninguna de las columnas.

3. Se reviso si el dataset checkin para ver si tenia valores nulos, vacios o duplicados.
    * No se encontraron valores nulos, vacios o duplicados en este dataset.

4. Se reviso la cantidad de nulos, vacios y duplicados en el dataset tip.
    * No se encontraron valores nulos o vacios en ninguna columna.
    * Pero si se encontraron valores duplicados en la columna text, con un total de 6885 valores duplicados.

5. Se eligieron dos valores de la columna text al azar que estuvierann dentro de la lista de duplicados y se procedio analizar los registros.
    * Se encontro que los registros eran de usuarios diferentes y de diferentes lugares, por lo tanto, no se pueden cosiderar como duplicados y se mantienen dentro del dataset.

## EDA de los datos
En base al análisis preliminar de los datos obtenidos de Google, para reducir la data, vamos a analizar solamente los estados más rentables para el modelo de negocio planteado:
California, Florida, Illinois, Nevada, Nueva York, Pennsylvania y Texas.
De los datos de Yelp decidimos reducir la información de los datasets Business, Check-in, reviews, Maps_Category, Tips y Users, para los lugares antes mencionados.

Antes de analizar patrones y tendencias, realizamos un reporte de nulos, outliers y faltantes.

El reporte de la tabla Business entregó los siguientes valores:

![Reporte de business](./Images/1%20reporte%20de%20business.jpg)

El reporte de la tabla TIPS:

![Reporte del df de tips](./Images/2%20reporte%20df%20TIPS.jpg)

Notamos que no tiene nulos ni valores significativos de outliers.
Más adelante, analizaremos la utilidad de esta tabla en relación a ML para entender las devoluciones en relación al modelo de negocio, usando nube de palabras para cata categoría de negocio, por ejemplo.
Podemos ver que cada negocio tiene un ID, lo que permitirá relacionar el negocio con la fecha de apertura del mismo usando esta tabla. 
Vemos que la tabla Maps Category nos va a permitir relacionar el id de google maps (ubicación) con la categoría del negocio.

El reporte de la tabla Maps (final):

![Reporte df Maps Final 1](./Images/3%20reporte%20Df%20Maps%20Final%201.jpg) 
![Reporte df Maps Final 2](./Images/4%20reporte%20Df%20Maps%20Final%202.jpg)

Si realizamos un scatterplot de outliers de la tabla USERS, obtenemos:

![Outliers columna numerica df Users](./Images/5%20Outliers%20columna%20numerica%20DF%20USERS.jpg)

A su vez, las tablas de MAPS, nos dan el siguiente reporte de valores faltantes:

![Faltantes text y textResp df maps](./Images/6%20faltantes%20text%20y%20textResp%20DF%20maps.jpg)

De las tablas por ciudad, podemos rescatar que hay un texto (escrito por el usuario), un rating de ese comentario y una respuesta al texto (realizada por el negocio comentado).
Correlación entre rating y la presencia de texto en textResp: 0.0139, es decir, no es significativa.
A su vez, la cantidad de textos y respuestas al texto es grande:

![Faltantes por columna df MAPS](./Images/7%20%20faltante%20por%20columna%20MAPS.jpg)

La mitad de las veces que se puntúa se pone un comentario, después, menos del 15 por ciento de las veces se obtiene una respuesta por parte del negocio (para Nueva York)

Si se hace este análisis para cada ciudad elegida (de los datos de Google), notamos que entre Text y TextResp los valores van entre 39 y 44 % para Text y entre 83 y 90 % para TextRespr de valores faltantes.

Lo que corresponde a TEXTRESP no podríamos usarlo por el alto porcentaje de valores faltantes. Por otro lado, que haya texto no parece alterar el puntaje recibido.
En la tablas por ciudad, hay una distribución cercana al 50% de comentarios duplicados. 
Podemos decir que los textos duplicados tienen una proporción significativa, esto puede llegar a ser contraproducente cuando se relacione el texto con el puntaje asociado, si el mismo texto tiene diferentes puntajes, por ejemplo.

En este caso, todos los dataframes de MAPS tienen un porcentaje cercano al 50% de duplicados en los textos de reseña.

En base al análisis de valores nulos, faltantes, duplicados y de outliers, cuyos resultados se adjuntan en las tablas, podemos entender qué categorías podremos usar y cuales no serán útiles.
Del df_maps_final, vemos que hay varios campos útiles: Name, address, gmap_id, description, latitude, longitude, avg_rating, num_of_reviews, url y city. De esta tabla, podríamos usar description y avg_rating para relacionar con ML.
Esta tabla TIPS puede servir para entrenar el LLM y entender las devoluciones en relación al modelo de negocio: Nube de palabras para cada categoría de negocio, por ejemplo.
En la tabla puntaje observamos que hay pocas apreciaciones negativas en relación a las que van desde el 3 al 5.

![Distribución de stars](./Images/9%20distribucion%20de%20stars.png)

El coeficiente de correlación de Pearson entre review_count y stars es: 0.0655147893638808

![Correlación review y stars](./Images/10%20correlacion%20review%20y%20stars.png)

Ahora, si pensamos si es que importa la cantidad de reseñas realizadas, más allá que no haya correlación con el puntaje en sí, es importante porque nos puede representar el nivel de respuesta al negocio:

![Top categorias con más reseñas](./Images/11%20Top%20categorias%20copn%20mas%20reseñas.png)

![Top categorias con más reseñas](./Images/11%20top%20categorias%20con%20menos%20reseñas.jpg)

Podemos identificar de este análisis que los restoranes (bares y vida nocturna) son el rubro con más reseñas, por lo que podríamos considerarlo como el rubro con el cual entrenar nuestro modelo MVP.

Ahora veremos de los datos en “Users”, cómo se comportan las apreciaciones a las reseñas hechas. A las reseñas se las puede categorizar como útil, divertida o interesante (cool), a su vez los usuarios tienen un conteo de reviews realizadas.

Pensando en nuestro modelo de negocio, podemos analizar si hay alguna proporción significativa de las reseñas útiles (useful) con respecto al total:

![Conteo de reviews por categoria useful, cool y fun](./Images/12%20conteo%20de%20reviews%20por%20categoria%20useful,%20cool%20y%20fun.jpg)

Entonces, sí podríamos proyectar usar esta categoría para poder plantear mejoras de los negocios en base a estas devoluciones.

Ahora veremos generalmente las correlaciones posibles en la tabla USER:

![Correlación general user](./Images/13%20correlacion%20general%20user.jpg)

De la tabla TIPS (consejos) vamos a ver si es útil tener en cuenta los conejos para la etapa posterior de ML:
Observamos que no existe una correlación evidente en el DF, al menos no de una manera que podamos identificar inmediatamente. Quizá entre usefull y fans podríamos proyectar alguna correlación útil.
Vemos que, ante un texto de consejo, existe un rate para el compliment count (cantidad de respuestas o resolución de esa queja), pero no resulta significativo: 

![Falta de compliment count](./Images/14%20falta%20de%20compliment%20count.png)

### **Conclusiones Generales**
En base al análisis de valores nulos, faltantes, duplicados y de outliers, cuyos resultados se adjuntan en las tablas, podemos rescatar cuales categorías serán útiles de cada tabla.
Del df_maps_final: Name, address, gmap_id, description, latitude, longitude, avg_rating, num_of_reviews, url y city. Además, podríamos usar description y avg_rating para relacionar con ML.
La tabla TIPS puede servir para entrenar el LLM y entender las devoluciones en relación al modelo de negocio: Nube de palabras para cada categoría de negocio, por ejemplo.
Podemos identificar de este análisis que los restoranes (bares y vida nocturna) son el rubro con más reseñas, por lo que podríamos considerarlo como el rubro con el cual entrenar nuestro modelo MVP.
Finalmente, observamos que no existe una correlación evidente en USER, quizá entre usefull y fans podríamos proyectar alguna correlación útil.

## 3 KPI's
### 1. **Densidad de reseñas por ciudad**

Cantidad promedio de reseñas por negocio en una ciudad puede darte una idea del nivel de actividad o interés en los negocios locales. Ciudades con más reseñas por negocio pueden indicar una mayor interacción de los consumidores, lo que es un buen indicador para posibles negocios.

* **Formula**: (Densidad de reseñas = Total de reseñas en una ciudad / Número de negocios en la ciudad)

* **Periodicidad**: Trimestral o Semestral: Para detectar cambios estacionales o tendencias en la actividad de los consumidores.

* **Objetivo**: Comparar ciudades y buscar aquellas con una densidad de reseñas alta, idealmente por encima del promedio.

### 2. **Indicador de Expansión de Clientela**

Porcentaje de crecimiento de check-ins de un periodo con respecto a otros negocios.

* **Formula**: (Cantidad de check-ins del periodo actual – Cantidad de check-ins del periodo anterior) / Cantidad de check-ins del periodo anterior * 100

* **Periodicidad**: Mensual.

* **Objetivo**: Identificar establecimientos con un crecimiento positivo de clientes del x% durante un periodo dterminado.

### 3. **Promedio de rating por categoría en la ciudad**

Evalúa el promedio de calificaciones (estrellas) por categoría de negocio en una ciudad, para identificar los sectores mejor valorados.

* **Formula**: (Promedio de rating = Sumatoria de ratings de una categoría / Numero de negocios en esa categoría)

* **Periodicidad**: Semestral.

* **Objetivo**: Priorizar ciudades y categorías con un promedio de rating mayor a 4.

## Diseño detallado
### Objetivos, contexto y público objetivo
Los objetivos de este MVP son dos. El primero es probar si existe interés y demanda por este tipo de servicio antes de realizar una inversión en un desarrollo completo. El segundo es mostrar el valor potencial del servicio con una funcionalidad mínima para atraer a inversores.

Todo emprendedor e inversor enfrenta la incertidumbre de decidir en qué sector o rubro invertir. Si este sector requiere de un lugar físico, surge una nueva duda: ¿Dónde establecer el emprendimiento o la inversión? Además, incluso después de resolver estas preguntas, surge otro desafío: si no se tiene experiencia previa en el sector o rubro, el camino hacia el éxito será más complicado.

Es por esto que nace Socius Lab, una aplicación que permite consultar el estado de un sector o rubro específico en una ciudad. Con esta herramienta, emprendedores e inversionistas pueden obtener respuestas de manera más ágil y precisa. La aplicación también proporcionará recomendaciones sobre las mejores localizaciones y señalará características positivas y negativas de cada sector o rubro, ayudando así a identificar las mejores opciones para establecer un negocio o inversión, y las particularidades que se deben considerar.

La audiencia objetivo de este servicio son personas que buscan dónde invertir su dinero, así como emprendedores que desean saber dónde invertir su dinero y tiempo

### Componetes principales y flujo de datos

El flujo de datos en este proyecto comienza con la extracción de información de las aplicaciones Google Maps y Yelp. De estas plataformas se obtienen datos como el número de reseñas, contenido de las reseñas, puntuación, promedio de puntuaciones, nombre del negocio, dirección, ciudad, latitud, longitud, entre muchas otras características.

Luego, los datos pasan por un proceso de transformación, en el cual se ajustan y se eliminan aquellas características que no sean relevantes para el proyecto. Este proceso de transformación no compromete la integridad ni la calidad de los datos. Al finalizar la transformación, los datos resultantes se cargan en un data warehouse alojado en la nube de Google (GCP). Este flujo constituye el proceso de ETL (Extracción, Transformación y Carga).

Para automatizar aún más el proceso y gestionar los flujos de trabajo, se utilizará Apache Airflow, que permitirá orquestar la obtención de los datos finales del ETL y realizar las acciones necesarias para que la información esté disponible en el data warehouse. Desde ahí, se podrán exportar los datos necesarios para llevar a cabo el análisis exploratorio de datos (EDA).

Después del análisis EDA, los datos se enviarán a un script que contiene el modelo de recomendación basado en Machine Learning. El modelo se entrenará con los nuevos datos y luego se evaluarán las métricas seleccionadas, así como el desempeño del modelo. Paralelamente, se producirá el dashboard. En este paso, los datos derivados del EDA se enviarán a la herramienta de visualización escogida, donde se crearán los dashboards y visualizaciones necesarias.

Al final se subirán todas las actualizaciones pertinentes a la pagina web y a la aplicación.

![Ilustración flujo de datos](./Images/Data%20Adicional.png)

### Funcioamiento del servicio
El funcionamiento del servicio es el mismo tanto en la página web como en la aplicación móvil. Primero, el usuario ingresa y, desde la página principal, selecciona el rubro o sector y la ciudad donde desea realizar el análisis. Luego, se dirige a la sección de inversiones, donde deberá ingresar el monto que tiene o desea invertir.

Con esta información, el programa se encargará de buscar las mejores ubicaciones según el sector seleccionado y mostrará algunas recomendaciones clave. Estas sugerencias se basan en las valoraciones, tanto positivas como negativas, que han recibido otros negocios en la misma categoría.

### Siguientes pasos
Si el proyecto continúa, las posibles mejoras incluyen la expansión de los sectores o rubros que se pueden analizar, así como la incorporación de más ciudades. Como se comenzó con datos solo de Estados Unidos, sería pertinente ir implementando progresivamente todas las ciudades, al igual que los diferentes rubros. También se podría realizar un análisis de mercado para identificar en qué países se encuentra la mayor parte del público objetivo y en qué países o ciudades desean invertir.

Otra posible mejora sería la recolección de datos de otras fuentes además de Google Maps y Yelp. Estas fuentes no se limitarían únicamente a reseñas, sino que también podrían incluir datos sobre negocios populares, estadísticas y análisis de diferentes sectores por país, o incluso información no pública de empresas recopilada por terceros y disponible para la compra.

### Mockups
<table>
    <tr>
        <td> <h2>Página inicial</h2> </td>
        <td> <h2>Página Inversiones</h2> </td>
    </tr>
    <tr>
        <td> <img src = "./Images/Mockup2.jpg" alt = "Mockup página principal" width = "700"> </td>
        <td> <img src = "./Images/Mockup1.jpg" alt = "Mockup página inversiones" width = "700"> </td>
    </tr>
    
</table>

## Implementación Stack Tecnologico
<table>
    <tr style = "text-align: center">
        <td> <h2>Python</h2> </td>
        <td> <h2>Google Colab</h2> </td>
        <td> <h2>Visual Studio Code</h2> </td>
    </tr>
    <tr>
        <td> <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt = "Logo Pyhton" Width = "700"> </td>
        <td> <img src = "https://www.cursosgis.com/wp-content/uploads/1-17.png" alt = "Logo Google Colab" Width = "700"> </td>
        <td> <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/1024px-Visual_Studio_Code_1.35_icon.svg.png" alt = "Logo Visual Studio Code" Width = "700"> </td>
    </tr>
    <tr style = "text-align: center">
        <td> <h2>Apache Airflow</h2> </td>
        <td> <h2>Power BI</h2> </td>
        <td> <h2>Scikit Learn</h2> </td>
    </tr>
    <tr>
        <td> <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/AirflowLogo.png/1200px-AirflowLogo.png" alt = "Logo Apache Airflow" Width = "700"> </td>
        <td> <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdhsYAK6nmwgqgYPX0dw4RORIUdC_cphd7qQ&s" alt = "Logo Google Colab" Width = "700"> </td>
        <td> <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt = "Logo Scikit Learn" Width = "700"> </td>
    </tr>
    <tr style = "text-align: center">
        <td> <h2>Google Cloud Platform GCP</h2> </td>
        <td> <h2>Trello</h2> </td>
        <td> <h2>Gantter</h2> </td>
    </tr>
    <tr style = "text-align: center">
        <td> <img src = "https://ucloudglobal.com/wp-content/uploads/2021/09/gcp-02.png" alt = "Logo Google Cloud Platform" Width = "700"> </td>
        <td> <img src = "https://www.conectasoftware.com/wp-content/uploads/2021/04/Trello-Emblema-1300x867.png" alt = "Logo Google Cloud Platform" Width = "700"> </td>
        <td> <img src = "https://lh3.googleusercontent.com/-kTfFzkEzgx4/WAo2rS97EUI/AAAAAAAAAQs/6pDmnPbfJLUxSHsqpaE9OrEdcPhIegGaQCMYCGAYYCw/s400/g256x256.png" alt = "Logo Google Cloud Platform" Width = "700"> </td>
    </tr>
    <tr style = "text-align: center">
        <td> <h2>GitHub</h2> </td>
        <td> <h2>Git</h2> </td>
    </tr>
    <tr style = "text-align: center">
        <td> <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/180px-GitHub_Invertocat_Logo.svg.png" alt = "Logo Google Cloud Platform" Width = "700"> </td>
        <td> <img src = "https://victorroblesweb.es/wp-content/uploads/2018/04/git.png" alt = "Logo Google Cloud Platform" Width = "700"> </td>
    </tr>
</table>