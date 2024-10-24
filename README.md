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


## EDA de los datos


## 3 KPI's


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