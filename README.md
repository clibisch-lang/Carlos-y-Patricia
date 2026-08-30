# Análisis de resultados académicos de estudiantes

## Descripción del proyecto

Este proyecto realiza un análisis exploratorio de datos sobre los resultados académicos de estudiantes.

El objetivo es identificar patrones relacionados con el rendimiento académico considerando variables como género, edad y nivel educativo.

Para el desarrollo del proyecto se utilizaron Python, Pandas y Streamlit.

## Dataset

El análisis utiliza datos de estudiantes que contienen información académica y demográfica.

Entre las principales variables analizadas se encuentran:

- Género
- Grupo de edad
- Nivel educativo
- Créditos estudiados
- Número de intentos previos
- Resultado académico final

Los posibles resultados finales son:

- Pass
- Fail
- Withdrawn
- Distinction

## Limpieza de datos

Durante el análisis se revisaron los tipos de datos y los valores nulos.

La variable `imd_band` contenía 1,111 valores nulos, los cuales fueron tratados durante el proceso de limpieza.

El dataset limpio fue guardado en:

`data/processed/student_info_clean.csv`

## Análisis exploratorio

Se realizaron diferentes análisis para estudiar el comportamiento de los estudiantes:

- Distribución general de resultados finales.
- Resultados según género.
- Resultados según nivel educativo.
- Resultados según grupo de edad.

También se utilizaron tablas y gráficos para facilitar la interpretación de los resultados.

## Principales resultados

El resultado académico más frecuente fue **Pass**, con 12,361 registros (37.93%).

Los demás resultados fueron:

- Withdrawn: 10,156 (31.16%)
- Fail: 7,052 (21.64%)
- Distinction: 3,024 (9.28%)

El análisis también permitió observar diferencias en los resultados según el nivel educativo y el grupo de edad.

## Aplicación interactiva

Se desarrolló una aplicación utilizando **Streamlit** para explorar los resultados de forma interactiva.

La aplicación incluye:

- Información general del dataset.
- Vista previa de los datos.
- Tablas y gráficos.
- Filtro por módulo.
- Filtro por género.
- Filtro por grupo de edad.
- Filtro por nivel educativo.

## Estructura del proyecto

- `data/raw/`: datos originales.
- `data/processed/`: datos procesados.
- `notebooks/`: análisis exploratorio en Jupyter Notebook.
- `app.py`: aplicación desarrollada con Streamlit.
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.

## Autores

### Aplicación publicada

La aplicación se encuentra disponible en Streamlit:

https://carlos-y-patricia-js9xlrwrirkupcbtbbasnd.streamlit.app/


Carlos y Patricia