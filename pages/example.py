import streamlit as st
import pandas as pd

st.title("Mi primera App con Streamlit")
st.write("Aquí se visualizará los datos y resultados de forma interactiva")

# Crear un slider
n_filas = st.slider("Selecciona el número de filas a mostrar", 1, 100)

# Generar datos aleatorios y mostrarlos
df = pd.DataFrame({'Columna A': range(n_filas)})
st.line_chart(df)


# Ejemplo visual de cómo se estructura la GUI en código
# 1. Configurar barra lateral
with st.sidebar:
    st.header("Configuración")
    opcion = st.selectbox("Elige una opción", ["A", "B"])

# 2. Configurar el cuerpo principal en columnas
col1, col2 = st.columns(2)

with col1:
    st.header("Columna Izquierda")
    st.button("Botón Acción")

with col2:
    st.header("Columna Derecha")
    st.metric(label="Temperatura", value="24 °C", delta="1.2 °C")
import streamlit as st
import numpy as np
import pandas as pd

# Título de la página de ejemplo
st.title("📈 Mi Primer Gráfico Interactivo")
st.write("¡Bienvenido a mi código de práctica! Mueve los controles de la izquierda para ver la magia.")

# 1. Creamos controles interactivos en la barra lateral
st.sidebar.header("🎛️ Controles del Gráfico")
frecuencia = st.sidebar.slider("Frecuencia (Velocidad de la onda)", min_value=1, max_value=10, value=2)
amplitud = st.sidebar.slider("Amplitud (Altura de la onda)", min_value=1, max_value=5, value=1)
agregar_ruido = st.sidebar.checkbox("¿Agregar ruido a la señal?")

# 2. Generamos datos matemáticos basados en los controles
tiempo = np.linspace(0, 10, 500)
senal_pura = amplitud * np.sin(frecuencia * tiempo)

if agregar_ruido:
    ruido = np.random.normal(0, 0.2, size=500)
    senal_final = senal_pura + ruido
else:
    senal_final = senal_pura

# 3. Guardamos los datos en una tabla ordenada
datos = pd.DataFrame({
    "Tiempo": tiempo,
    "Señal": senal_final
})

# 4. Mostramos el gráfico en la pantalla principal
st.subheader("📊 Visualización en Tiempo Real")
st.line_chart(datos.set_index("Tiempo"))

# 5. Un extra: Mostrar los datos crudos si el usuario quiere
if st.button("👁️ Ver datos numéricos"):
    st.write("Aquí están los primeros números que generan el gráfico:")
    st.dataframe(datos.head(10))
