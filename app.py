import streamlit as st
import random
import numpy as np
from collections import Counter

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Generador 3R", layout="wide")

# ---------------- ESTILO CASINO ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #0B0F1A, #111827);
    color: white;
}

h1, h2, h3 {
    color: #FACC15;
    text-align: center;
}

.stButton > button {
    background: linear-gradient(135deg, #FACC15, #EAB308);
    color: black;
    font-weight: bold;
    border-radius: 12px;
    height: 55px;
    font-size: 18px;
}

.card {
    background: #1F2937;
    padding: 15px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.4);
}

.ball {
    width: 55px;
    height: 55px;
    border-radius: 50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:bold;
    font-size:20px;
    background:#111827;
    border:3px solid #FACC15;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FUNCIONES ----------------

def generar_combinaciones(cantidad, rango_suma):
    combinaciones = []

    while len(combinaciones) < cantidad:
        nums = sorted(random.sample(range(1, 57), 6))
        suma = sum(nums)

        if rango_suma[0] <= suma <= rango_suma[1]:
            combinaciones.append(nums)

    return combinaciones


def render_ticket(numbers, modo):
    color = "#3B82F6" if modo == "ESTRUCTURA" else "#22C55E"

    html = '<div class="card"><div style="display:flex; justify-content:center; gap:12px;">'

    for n in numbers:
        html += f'<div class="ball" style="border:3px solid {color};">{n:02d}</div>'

    html += '</div></div>'

    st.markdown(html, unsafe_allow_html=True)


# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1, 3])

# ---------------- PANEL ----------------
with col1:
    st.markdown("## 🎛️ Panel de control")

    with st.form("formulario"):

        cantidad = st.slider("Cantidad de combinaciones", 1, 20, 5)

        modo = st.selectbox(
            "Modo de juego",
            ["ESTRUCTURA", "DISPERSIÓN"]
        )

        rango_suma = st.slider("Rango de suma", 50, 300, (120, 200))

        st.caption(f"Se generarán {cantidad} combinaciones en modo {modo}")

        generar = st.form_submit_button("🎯 GENERAR")


# ---------------- RESULTADOS ----------------
with col2:

    st.markdown("# 🎰 Generador 3R")

    st.markdown("""
    ### 🧠 Interpretación

    🔵 **Estructura:** Sigue patrones históricos  
    🟢 **Dispersión:** Cubre más combinaciones posibles
    """)

    if generar:

        st.success("Combinaciones listas 🎉")
        st.balloons()

        resultados = generar_combinaciones(
            cantidad,
            rango_suma
        )

        st.markdown("## 🎟️ Tus boletos")

        for combo in resultados:
            render_ticket(combo, modo)

        # ---------------- RESUMEN ----------------
        st.markdown("## 📊 Resumen")

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric("Total", len(resultados))

        with colB:
            suma_prom = int(np.mean([sum(c) for c in resultados]))
            st.metric("Suma promedio", suma_prom)

        with colC:
            st.metric("Estado", "Activo")

        # ---------------- TOP ----------------
        all_nums = [n for combo in resultados for n in combo]
        top = [num for num, _ in Counter(all_nums).most_common(3)]

        st.markdown("### 🔝 Números clave")
        render_ticket(top, modo)

        # ---------------- DATOS CRUDOS ----------------
        with st.expander("🧪 Modo experto"):
            st.write(resultados)
