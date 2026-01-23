# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ============================
# CONFIGURACIÓN INICIAL
# ============================

st.set_page_config(page_title="Bank Marketing EDA", layout="wide")

# ============================
# TÍTULO Y PRESENTACIÓN
# ============================

st.title("📊 Análisis de Campañas de Marketing Bancario")

st.markdown("""
Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre una base de datos de campañas de marketing directo de una entidad bancaria.

### Objetivos del análisis:
- Identificar las variables más asociadas a la aceptación de la campaña (`y`).
- Explorar el perfil de los clientes que responden positivamente.
- Evaluar el impacto de la duración del contacto, el canal utilizado y la recencia del último contacto.
- Analizar el rol de variables macroeconómicas en el comportamiento del cliente.

### Datos del autor:
- **Nombre:** Juan García Soto  
- **Curso:** ESP EN PYTHON FOR ANALYTICS ed.53  
- **Año:** 2025 - 2026
""")

# ============================
# CARGA DEL DATASET
# ============================

df = pd.read_csv("data/BankMarketing.csv", sep=';')

# ============================
# SIDEBAR – FILTROS GLOBALES
# ============================

st.sidebar.header("🔍 Filtros del Dataset")

# Slider de edad
age_range = st.sidebar.slider(
    "Rango de edad",
    int(df["age"].min()),
    int(df["age"].max()),
    (25, 60)
)

# Multiselect de profesiones
jobs = st.sidebar.multiselect(
    "Profesiones",
    df["job"].unique()
)

# Checkbox para mostrar dataset completo
show_data = st.sidebar.checkbox("Mostrar dataset completo")

# Aplicación de filtros
df_filtered = df[
    (df["age"] >= age_range[0]) &
    (df["age"] <= age_range[1])
]

if jobs:
    df_filtered = df_filtered[df_filtered["job"].isin(jobs)]

# ============================
# TABS PRINCIPALES
# ============================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📁 Información General",
    "📈 Distribuciones",
    "🔀 Análisis Bivariado",
    "📊 Análisis Personalizado",
    "📝 Conclusiones"
])

# ============================
# TAB 1 – INFORMACIÓN GENERAL
# ============================

with tab1:

    st.subheader("Vista previa del dataset filtrado")
    st.write(df_filtered.head())

    if show_data:
        st.dataframe(df_filtered)

    st.subheader("Información general del dataset")

    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)

    st.write("### Tipos de datos")
    st.write(df.dtypes)

    st.write("### Valores nulos")
    st.write(df.isna().sum())

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    st.subheader("Clasificación de variables")
    st.write("**Variables numéricas:**", numeric_cols)
    st.write("**Variables categóricas:**", categorical_cols)

    st.subheader("Estadísticas descriptivas")
    st.write(df.describe(include='all'))

# ============================
# TAB 2 – DISTRIBUCIONES
# ============================

with tab2:

    st.subheader("Distribución de variables numéricas")

    col1, col2 = st.columns(2)

    with col1:
        col_num = st.selectbox("Selecciona una variable numérica:", numeric_cols)

    with col2:
        bins = st.slider("Número de bins", 5, 50, 20)

    fig, ax = plt.subplots()
    sns.histplot(df_filtered[col_num], kde=True, bins=bins, ax=ax)
    st.pyplot(fig)

    st.subheader("Distribución de variables categóricas")

    col_cat = st.selectbox("Selecciona una variable categórica:", categorical_cols)

    fig, ax = plt.subplots()
    sns.countplot(data=df_filtered, x=col_cat, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ============================
# TAB 3 – ANÁLISIS BIVARIADO
# ============================

with tab3:

    st.subheader("Numérico vs Variable objetivo (y)")

    col_num2 = st.selectbox("Selecciona variable numérica:", numeric_cols, key="num2")

    fig, ax = plt.subplots()
    sns.boxplot(data=df_filtered, x='y', y=col_num2, ax=ax)
    st.pyplot(fig)

    st.subheader("Categórico vs Variable objetivo (y)")

    col_cat2 = st.selectbox("Selecciona variable categórica:", categorical_cols, key="cat2")

    if col_cat2 != 'y':
        tabla = pd.crosstab(df_filtered[col_cat2], df_filtered['y'], normalize='index')
        st.write(tabla)

        fig, ax = plt.subplots()
        tabla.plot(kind='bar', stacked=True, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

# ============================
# TAB 4 – ANÁLISIS PERSONALIZADO
# ============================

with tab4:

    st.subheader("Scatterplot personalizado")

    x = st.selectbox("Variable X:", numeric_cols, key="scatter_x")
    y = st.selectbox("Variable Y:", numeric_cols, key="scatter_y")

    fig, ax = plt.subplots()
    sns.scatterplot(data=df_filtered, x=x, y=y, hue='y', ax=ax)
    st.pyplot(fig)

# ============================
# TAB 5 – CONCLUSIONES
# ============================

with tab5:

    st.subheader("Hallazgos clave")
    st.markdown("""
1. La duración de la llamada (`duration`) es el factor más asociado a la aceptación.  
2. El canal celular es más efectivo que el teléfono fijo.  
3. Clientes contactados recientemente (`pdays`) responden mejor.  
4. Variables macroeconómicas influyen en la aceptación.  
5. El perfil del cliente (`job`, `education`) afecta la probabilidad de éxito.  
""")

    st.subheader("Conclusiones finales")
    st.markdown("""
1. La duración del contacto (`duration`) es el factor más determinante para la aceptación de la campaña.  
2. Los clientes contactados recientemente (`pdays` bajos) muestran mayor disposición a aceptar la oferta.  
3. El canal celular (`contact = cellular`) es más efectivo que el teléfono fijo.  
4. Variables macroeconómicas como `euribor3m` y `cons.price.idx` influyen en el comportamiento del cliente.  
5. El perfil del cliente —profesión (`job`), educación (`education`), estado civil (`marital`)— impacta la probabilidad de éxito.  
""")
