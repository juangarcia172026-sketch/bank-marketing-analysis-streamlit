# -*- coding: utf-8 -*-
"""Evaluación 2-Juan Garcia.ipynb

# Módulo 1: Home (Presentación del proyecto)

## Análisis de Campañas de Marketing Bancario

### El análisis busca:

- Identificar las variables más asociadas a la aceptación de la campaña (`y`).
- Explorar el perfil de los clientes que responden positivamente.
- Evaluar el impacto de la duración del contacto, el canal utilizado y la recencia del último contacto.
- Analizar el rol de variables macroeconómicas en el comportamiento de los clientes.


###Datos del autor:   
  o Nombre completo: Juan García Soto  
  o Curso / Especialización: ESP EN PYTHON FOR ANALYTICS ed.53  
  o Año: 2025 - 2026

##Breve explicación del dataset

El dataset de marketing bancario contiene información sobre clientes y campañas de marketing directo realizadas por un banco. Incluye:

- **Variables demográficas:** edad, estado civil, nivel educativo.
- **Variables laborales:** tipo de trabajo (`job`).
- **Variables financieras:** saldo promedio, créditos, préstamos.
- **Variables de contacto:** tipo de contacto (`contact`), duración de la llamada (`duration`), número de contactos previos (`campaign`, `pdays`, `previous`).
- **Variables macroeconómicas:** índices económicos y de confianza.
- **Variable objetivo:** `y`, que indica si el cliente aceptó (`yes`) o no (`no`) la oferta.

El propósito del EDA es generar insights que permitan diseñar campañas más efectivas, segmentar mejor a los clientes y optimizar los recursos comerciales.
"""

"""## 1. Importar librerías"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""##2. Cargar el dataset correctamente"""

df = pd.read_csv('data/BankMarketing.csv')
df.head()

df.info()

df.columns

"""## 3. Definir la Clase POO (DataAnalyzer)"""

import io

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def info(self):
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        return buffer.getvalue()

    def variable_types(self):
        numeric = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical = self.df.select_dtypes(include=['object']).columns.tolist()
        return numeric, categorical

    def descriptive_stats(self):
        return self.df.describe(include='all')

    def missing_values(self):
        return self.df.isna().sum()

"""## 4. Crear el objeto analyzer

"""

analyzer = DataAnalyzer(df)

"""##5. Ítem 1 — Información general del dataset

"""

print("Información general:")
print(analyzer.info())

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores nulos:")
print(df.isna().sum())

"""## 6. Ítem 2 — Clasificación de variables

"""

numeric_cols, categorical_cols = analyzer.variable_types()

print("Variables numéricas:")
print(numeric_cols)

print("\nVariables categóricas:")
print(categorical_cols)

"""##7. Ítem 3 — Estadísticas descriptivas"""

analyzer.descriptive_stats()

"""## 8. Ítem 4 — Valores faltantes"""

missing = analyzer.missing_values()
missing

missing = analyzer.missing_values()
print(missing)

# Solo graficar si hay valores faltantes
missing_nonzero = missing[missing > 0]

if missing_nonzero.empty:
    print("\nNo hay valores faltantes en el dataset.")
else:
    missing_nonzero.plot(kind='bar')
    plt.title("Valores faltantes por columna")
    plt.show()

"""## 9. Ítem 5 — Distribución de variables numéricas"""

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribución de {col}")
    plt.show()

"""## 10. Ítem 6 — Variables categóricas"""

for col in categorical_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x=col)
    plt.xticks(rotation=45)
    plt.title(f"Distribución de {col}")
    plt.show()

"""## 11. Ítem 7 — Análisis bivariado (numérico vs categórico)"""

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(data=df, x='y', y=col)
    plt.title(f"{col} vs y")
    plt.show()

"""## 12. Ítem 8 — Análisis bivariado (categórico vs categórico)

"""

for col in categorical_cols:
    if col != 'y':
        tabla = pd.crosstab(df[col], df['y'], normalize='index')
        print(f"\n{col} vs y")
        print(tabla)

        tabla.plot(kind='bar', stacked=True)
        plt.title(f"{col} vs y")
        plt.xticks(rotation=45)
        plt.show()

"""## 13. Ítem 9 — Análisis basado en parámetros seleccionados"""

x = 'age'
y = 'duration'

sns.scatterplot(data=df, x=x, y=y, hue='y')
plt.title(f"{x} vs {y}")
plt.show()

"""## 14. Ítem 10 — Hallazgos clave"""

print("""
1. La duración de la llamada (duration) es el factor más asociado a la aceptación.
2. El canal celular es más efectivo que telefono.
3. Clientes contactados recientemente (pdays) responden mejor.
4. Variables macroeconómicas influyen en la aceptación.
5. El perfil del cliente (job, education) afecta la probabilidad de éxito.
""")

"""## Conclusiones finales
1. La duración del contacto (`duration`) es el factor más determinante para la aceptación de la campaña. Cuanto mayor es el tiempo de conversación, mayor es la probabilidad de obtener una respuesta positiva.
2. Los clientes contactados recientemente (`pdays` bajos) muestran una mayor disposición a aceptar la oferta, lo que sugiere que la recencia del contacto es clave en la estrategia comercial.
3. El canal de contacto celular (`contact = cellular`) es más efectivo que el teléfono fijo, indicando que los clientes responden mejor a medios más directos y personales.
4. Variables macroeconómicas como `euribor3m` y `cons.price.idx` influyen en el comportamiento del cliente, lo que evidencia que el contexto económico afecta la decisión final.
5. El perfil del cliente —incluyendo profesión (`job`), nivel educativo (`education`) y estado civil (`marital`)— tiene un impacto significativo en la probabilidad de éxito de la campaña, permitiendo segmentar mejor las acciones de marketing.
Estas conclusiones permiten orientar estrategias más efectivas, optimizar recursos y mejorar la tasa de conversión en campañas futuras.
"""
