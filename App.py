import streamlit as st
from data import get_sample_history
from filters import detect_mode
from logic import generate_multiple

st.set_page_config(page_title="3R System", layout="wide")

st.title("🔥 3R System (Revancha • Revanchita • Real)")

# HISTORIAL
st.header("📊 Historial")
df = get_sample_history()
st.dataframe(df)

# ANALISIS
st.header("🧠 Análisis de modo")

for i, row in df.iterrows():
    combo = row.tolist()
    mode = detect_mode(combo)
    st.write(f"{combo} → {mode}")

# GENERADOR
st.header("🎯 Generador 3R")

modo = st.selectbox("Modo de juego", ["ESTRUCTURA", "DISPERSION"])
cantidad = st.slider("Cantidad de combinaciones", 1, 20, 5)

if st.button("Generar"):
    resultados = generate_multiple(cantidad, modo)

    for r in resultados:
        st.success(r)
