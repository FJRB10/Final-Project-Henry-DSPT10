# Diccionario de Datos


---

## Plataforma Yelp

### Review (Reseñas con puntuacion)
- **review_id**: ID único de la reseña.
- **user_id**: ID del usuario que hizo la reseña.
- **business_id**: ID del negocio reseñado.
- **stars**: Calificación dada al negocio, de 1 a 5.
- **useful**: Número de personas que marcaron la reseña como útil.
- **text**: Comentario o reseña del usuario.
- **date**: Fecha en la que se realizó la reseña.

### Checkin (Registros de visita, algunos locales dan beneficios a los usuarios al confirmar una visita en YELP)
- **date**: Fecha de la visita o registro.
- **business_id**: ID del negocio visitado.

### Business (Datos de los negocios)
- **business_id**: ID único del negocio.
- **name**: Nombre del negocio.
- **address**: Dirección del negocio.
- **city**: Ciudad donde se ubica el negocio.
- **state**: Estado o provincia donde se encuentra.
- **postal_code**: Código postal de la ubicación.- **latitude**: Latitud (coordenada geográfica) del negocio.
- **longitude**: Longitud (coordenada geográfica) del negocio.
- **stars**: Promedio de estrellas (calificación) del negocio.
- **reviews_count**: Número total de reseñas del negocio.
- **is_open**: Indicador de si el negocio está abierto (`1`) o cerrado (`0`).
- **attributes**: Atributos adicionales del negocio.
- **categories**: Subcategorías del negocio.
- **hours**: Horarios de atención del negocio.

### tip (Opinión corta, o datos breves de algun local)
- **user_id**: ID del usuario que dejó la opinión.
- **business_id**: ID del negocio comentado.
- **text**: Opinión breve del usuario sobre el negocio.
- **date**: Fecha en que se dejó la opinión.

### user (Datos de los usuarios que dan feedback)
- **user_id**: ID único del usuario.
- **name**: Nombre del usuario.
- **reviews_count**: Total de reseñas que ha hecho el usuario.
- **yelping_since**: Fecha en la que el usuario se unió a Yelp.
- **fans**: Número de seguidores del usuario.
- **average_stars**: Calificación promedio dada por el usuario en sus reseñas.


---

## Plataforma Google Maps

### Reviews (Reseñas en Google)
- **user_Id**: ID único del usuario que realizó la reseña.
- **name**: Nombre del negocio o lugar al que se refiere la reseña.
- **time**: Fecha en que se publicó la reseña, en formato `YYYY/MM/DD`.
- **rating**: Calificación que dio el usuario al negocio, de 1 a 5.
- **text**: Texto de la reseña, comentarios o impresiones del usuario.
- **textResp**: Respuesta del negocio o local a la reseña del usuario.
- **timeResp**: tiempo de respuesta del negocio o local
- **gmap_id**: Código de ubicación específica del negocio en Google Maps.

### Metadata (Información del negocio)
- **name**: Nombre del negocio o lugar.
- **address**: Dirección completa del negocio.
- **gmap_id**: Código único de la ubicación en Google Maps.
- **description**: Descripción del negocio o lugar.
- **latitude**: Latitud de la ubicación del negocio (coordenada).
- **longitude**: Longitud de la ubicación del negocio (coordenada).
- **avg_rating**: Calificación promedio del negocio basada en todas las reseñas.
- **num_of_reviews**: Número total de reseñas recibidas por el negocio.
- **price**: Indicador de precios (bajo, medio, alto) del negocio.
- **hours**: Horarios de operación del negocio.
- **state**: Estado o provincia donde se encuentra el negocio.
- **url**: Direccion de la pagina del local o negocio
- **city**: Ciudad donde se encuentra el negocio
- **Monday**: Horarios de atencion durante el dia en cuestion
- **Tuesday**: Horarios de atencion durante el dia en cuestion
- **Wednesday**: Horarios de atencion durante el dia en cuestion
- **Thursday**: Horarios de atencion durante el dia en cuestion
- **Friday**: Horarios de atencion durante el dia en cuestion
- **Saturday**: Horarios de atencion durante el dia en cuestion
- **Sunday**: Horarios de atencion durante el dia en cuestion
- **gmap_id**: Código único de la ubicación en Google Maps.
- **accessibility**: Opciones de accesibilidad (como rampas).
- **activities**: Actividades ofrecidas en el negocio.
- **amenities**: Servicios adicionales (como WiFi, estacionamiento).
- **atmosphere**: Ambiente o estilo del lugar (relajado, formal).
- **crowd**: Público o tipo de personas que frecuentan el lugar.
- **dinning_options**: Opciones de comida que ofrece el negocio.
- **from_the_business**: Información adicional proporcionada por el negocio.
- **getting_here**: Indicaciones o formas de llegar al lugar.
- **health_and_safety**: Información de salud y seguridad.
- **highlights**: Características destacadas del negocio.
- **offerings**: Servicios especiales o adicionales.
- **payments**: Métodos de pago aceptados por el negocio.
- **planning**: Servicios de planificación, como eventos o bodas.
- **Popular for**: identifica el momento de consumo al que esta mejor destinado, si es bueno para cenar, almorzar o desayunar
- **recycling**: Opciones o políticas de reciclaje.
- **service_options**: Servicios opcionales (como entrega delivery, recogida).

### Category (Categorias del negocio)
- **gmap_id**: Código único de la ubicación en Google Maps.
- **category**: Subcategoría o tipo de negocio (ej., restaurante, hotel).

### Relative Results (Negocios semejantes al negocio apuntado)
- **gmap_id**: Código único de la ubicación en Google Maps.
- **relative_Results**: Código gmap_id de los negocios semejantes

---

