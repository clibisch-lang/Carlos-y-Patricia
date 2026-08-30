import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Análisis de estudiantes",
    page_icon="📊",
    layout="wide"
)

# Título de la aplicación
st.title("📊 Análisis de resultados de estudiantes")

st.write(
    "Aplicación interactiva para explorar los resultados académicos "
    "de los estudiantes."
)

# Cargar el dataset procesado
df = pd.read_csv("data/processed/student_info_clean.csv")

# Barra lateral con filtros
st.sidebar.header("Filtros")

modulo = st.sidebar.multiselect(
    "Módulo",
    options=df["code_module"].unique()
)

genero = st.sidebar.multiselect(
    "Género",
    options=df["gender"].unique()
)

edad = st.sidebar.multiselect(
    "Grupo de edad",
    options=df["age_band"].unique()
)

educacion = st.sidebar.multiselect(
    "Nivel educativo",
    options=df["highest_education"].unique()
)

# Creamos una copia de los datos para aplicar los filtros
df_filtrado = df.copy()

if modulo:
    df_filtrado = df_filtrado[df_filtrado["code_module"].isin(modulo)]

if genero:
    df_filtrado = df_filtrado[df_filtrado["gender"].isin(genero)]

if edad:
    df_filtrado = df_filtrado[df_filtrado["age_band"].isin(edad)]

if educacion:
    df_filtrado = df_filtrado[
        df_filtrado["highest_education"].isin(educacion)
    ]


# Mostrar información general
st.subheader("Información general")

col1, col2, col3 = st.columns(3)

col1.metric("Registros", len(df_filtrado))
col2.metric("Columnas", len(df_filtrado.columns))
col3.metric(
    "Estudiantes únicos",
    df_filtrado["id_student"].nunique()
)

# Vista previa de los datos
st.subheader("Vista previa del dataset")

st.dataframe(df_filtrado.head(20), use_container_width=True)

# Distribución de resultados finales
st.subheader("Distribución de resultados finales")

resultados = (
    df_filtrado["final_result"]
    .value_counts()
    .sort_values(ascending=False)
)

st.write(resultados)

st.bar_chart(resultados)

# Resultados según género
st.subheader("Resultados finales según género")

tabla_genero = pd.crosstab(
    df_filtrado["gender"],
    df_filtrado["final_result"],
    normalize="index"
) * 100

st.dataframe(tabla_genero.round(2), use_container_width=True)

st.bar_chart(tabla_genero)

# Resultados según nivel educativo
st.subheader("Resultados finales según nivel educativo")

tabla_educacion = pd.crosstab(
    df_filtrado["highest_education"],
    df_filtrado["final_result"],
    normalize="index"
) * 100

st.dataframe(tabla_educacion.round(2), use_container_width=True)

st.bar_chart(tabla_educacion)

# Resultados según grupo de edad
st.subheader("Resultados finales según grupo de edad")

tabla_edad = pd.crosstab(
    df_filtrado["age_band"],
    df_filtrado["final_result"],
    normalize="index"
) * 100

st.dataframe(tabla_edad.round(2), use_container_width=True)

st.bar_chart(tabla_edad)