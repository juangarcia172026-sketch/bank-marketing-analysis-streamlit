[README.md](https://github.com/user-attachments/files/24785506/README.md)

# Bank Marketing – Exploratory Data App
Aplicación interactiva en Streamlit para analizar los factores que influyen en la aceptación de campañas de marketing directo en una entidad bancaria. El proyecto incluye un análisis exploratorio completo, visualizaciones dinámicas y conclusiones basadas en los principales hallazgos del conjunto de datos BankMarketing.csv.

## Descripción del proyecto
Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre el dataset de marketing bancario, con el objetivo de identificar qué características de los clientes y qué condiciones de contacto influyen en la probabilidad de que acepten una campaña de marketing.

La aplicación permite:
- Explorar distribuciones y relaciones entre variables numéricas y categóricas.
- Identificar patrones asociados a la aceptación de la campaña (`y`).
- Analizar perfiles de clientes según edad, profesión, educación, estado civil, entre otros.
- Evaluar el impacto de variables macroeconómicas y de contacto.
- Generar insights clave para optimizar estrategias comerciales.
- Navegar por módulos organizados mediante pestañas, con filtros globales en la barra lateral.

## Hallazgos principales
- La duración de la llamada (`duration`) es el factor más determinante para la aceptación de la campaña.
- El canal celular (`contact = cellular`) es más efectivo que el teléfono fijo.
- Clientes contactados recientemente (`pdays` bajos) muestran mayor probabilidad de respuesta positiva.
- Variables macroeconómicas como `euribor3m` y `cons.price.idx` influyen en el comportamiento del cliente.
- El perfil del cliente (profesión, nivel educativo, estado civil) tiene un impacto significativo en la probabilidad de éxito.

## Visualizaciones principales

### Distribución por edad
(Imagen próximamente)

### Distribución por profesión
(Imagen próximamente)

### Relación entre profesión y aceptación (`y`)
(Imagen próximamente)

## Tecnologías utilizadas
- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Streamlit

## Ejecución de la aplicación
Para ejecutar la aplicación localmente:
pip install -r requirements.txt
streamlit run app.py

## Uso de la aplicación
1. Acceda a la aplicación desplegada en Streamlit Cloud.
2. Descargue el archivo BankMarketing.csv desde la carpeta `/data` del repositorio.
3. Súbalo mediante el botón “Sube el archivo BankMarketing.csv”.
4. Explore los módulos del EDA utilizando los filtros del sidebar y las pestañas superiores.

## Conclusiones finales
- La duración del contacto es el predictor más fuerte de aceptación.
- Los clientes con contacto reciente responden mejor.
- El canal celular es más eficiente que el teléfono fijo.
- Los factores macroeconómicos y demográficos influyen en la decisión.
- El análisis permite orientar estrategias de marketing más efectivas y segmentadas.
