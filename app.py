# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ============================
# TÍTULO Y PRESENTACIÓN
# ============================

st.title("Análisis de Campañas de Marketing Bancario")
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

df = pd.read_csv("data/BankMarketing.csv")

st.subheader("Vista previa del dataset")
st.write(df.head())

# ============================
# INFORMACIÓN GENERAL
# ============================

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


# ============================
# CLASIFICACIÓN DE VARIABLES
# ============================

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

st.subheader("Clasificación de variables")
st.write("**Variables numéricas:**", numeric_cols)
st.write("**Variables categóricas:**", categorical_cols)

# ============================
# ESTADÍSTICAS DESCRIPTIVAS
# ============================

st.subheader("Estadísticas descriptivas")
st.write(df.describe(include='all'))

# ============================
# VALORES FALTANTES
# ============================

st.subheader("Valores faltantes")

missing = df.isna().sum()
st.write(missing)

missing_nonzero = missing[missing > 0]

if missing_nonzero.empty:
    st.success("No hay valores faltantes en el dataset.")
else:
    fig, ax = plt.subplots()
    missing_nonzero.plot(kind='bar', ax=ax)
    st.pyplot(fig)

# ============================
# DISTRIBUCIÓN DE VARIABLES NUMÉRICAS
# ============================

st.subheader("Distribución de variables numéricas")

col_num = st.selectbox("Selecciona una variable numérica:", numeric_cols)

fig, ax = plt.subplots()
sns.histplot(df[col_num], kde=True, ax=ax)
st.pyplot(fig)

# ============================
# VARIABLES CATEGÓRICAS
# ============================

st.subheader("Distribución de variables categóricas")

col_cat = st.selectbox("Selecciona una variable categórica:", categorical_cols)

fig, ax = plt.subplots()
sns.countplot(data=df, x=col_cat, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# ============================
# ANÁLISIS BIVARIADO
# ============================

st.subheader("Análisis bivariado")

st.write("### Numérico vs Variable objetivo (y)")
col_num2 = st.selectbox("Selecciona variable numérica:", numeric_cols, key="num2")

fig, ax = plt.subplots()
sns.boxplot(data=df, x='y', y=col_num2, ax=ax)
st.pyplot(fig)

st.write("### Categórico vs Variable objetivo (y)")
col_cat2 = st.selectbox("Selecciona variable categórica:", categorical_cols, key="cat2")

if col_cat2 != 'y':
    tabla = pd.crosstab(df[col_cat2], df['y'], normalize='index')
    st.write(tabla)

    fig, ax = plt.subplots()
    tabla.plot(kind='bar', stacked=True, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ============================
# ANÁLISIS PERSONALIZADO
# ============================

st.subheader("Análisis basado en parámetros seleccionados")

x = st.selectbox("Variable X:", numeric_cols, key="scatter_x")
y = st.selectbox("Variable Y:", numeric_cols, key="scatter_y")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x=x, y=y, hue='y', ax=ax)
st.pyplot(fig)

# ============================
# HALLAZGOS CLAVE
# ============================

st.subheader("Hallazgos clave")
st.markdown("""
1. La duración de la llamada (`duration`) es el factor más asociado a la aceptación.  
2. El canal celular es más efectivo que el teléfono fijo.  
3. Clientes contactados recientemente (`pdays`) responden mejor.  
4. Variables macroeconómicas influyen en la aceptación.  
5. El perfil del cliente (`job`, `education`) afecta la probabilidad de éxito.  
""")

# ============================
# CONCLUSIONES FINALES
# ============================

st.subheader("Conclusiones finales")
st.markdown("""
1. La duración del contacto (`duration`) es el factor más determinante para la aceptación de la campaña.  
2. Los clientes contactados recientemente (`pdays` bajos) muestran mayor disposición a aceptar la oferta.  
3. El canal celular (`contact = cellular`) es más efectivo que el teléfono fijo.  
4. Variables macroeconómicas como `euribor3m` y `cons.price.idx` influyen en el comportamiento del cliente.  
5. El perfil del cliente —profesión (`job`), educación (`education`), estado civil (`marital`)— impacta la probabilidad de éxito.  
""")
