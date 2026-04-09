import streamlit as st
import numpy as np
from collections import Counter

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Generador 3R",
    layout="wide"
)

# ---------------- ESTILO CASINO ----------------
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #0B0F1A, #111827);
    color: white;
}

/* TITULOS */
h1, h2, h3 {
    color: #FACC15;
    text-align: center;
}

/* BOTON */
.stButton > button {
    background: linear-gradient(135deg, #FACC15, #EAB308);
    color: black;
    font-weight: bold;
    border-radius: 12px;
    height: 55px;
    font-size: 18px;
}

/* TARJETAS */
.card {
    background: #1F2937;
    padding: 15px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.4);
}

/* BADGES */
.badge-blue {
    background: #1E3A8A;
    color: #93C5FD;
}

.badge-green {
    background: #064E3B;
    color: #6EE7B7;
}

.badge {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: bold;
}

/* BOLAS */
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
    box-shadow: 0 4px 12px rgba(0,0,0,0.6);
    transition: 0.2s;
}

.ball:hover {
    transform: scale(1.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------- FUNCIONES VISUALES ----------------

def render_ticket(numbers, mode):
    border_color = "#3B82F6" if mode == "ESTRUCTURA" else "#22C55E"

    html = f"""
    <div class="card">
        <div style="display:flex; justify-content:center; gap:12px;">
    """

    for n in numbers:
        html += f"""
        <div class="ball" style="border:3px solid {border_color};">
            {n:02d}
        </div>
        """

    html += "</div></div>"

    st.markdown(html, unsafe_allow_html=True)


def render_analysis_row(numbers, mode):
    badge_class = "badge-blue" if mode == "ESTRUCTURA" else "badge-green"

    html = f"""
    <div class="card" style="display:flex; justify-content:space-between; align-items:center;">
        <div class="badge {badge_class}">
            {mode}
        </div>

        <div style="display:flex; gap:8px;">
    """

    for n in numbers:
        html += f"""
        <div style="
            width:38px;
            height:38px;
            border-radius:50%;
            background:#374151;
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:bold;
        ">
            {n:02d}
        </div>
        """

    html += "</div></div>"

    st.markdown(html, unsafe_allow_html=True)


# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1, 3])

# ---------------- PANEL CONTROL ----------------
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

        # ---------------- AQUI CONECTAS TU LOGICA ----------------
        # Reemplaza esto por tu sistema real
        resultados = [
            [5, 12, 18, 24, 33, 40],
            [3, 9, 15, 27, 31, 44],
            [1, 7, 19, 22, 36, 41]
        ]

        resultados_con_modo = [(r, modo) for r in resultados]

        # ---------------- BOLETOS ----------------
        st.markdown("## 🎟️ Tus boletos")

        for combo, m in resultados_con_modo:
            render_ticket(combo, m)

        # ---------------- RESUMEN ----------------
        st.markdown("## 📊 Resumen")

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric("Total", len(resultados))

        with colB:
            suma_prom = int(np.mean([sum(c) for c in resultados]))
            st.metric("Suma promedio", suma_prom)

        with colC:
            st.metric("Estado", "Óptimo")

        # ---------------- TOP NUMEROS ----------------
        all_nums = [n for combo in resultados for n in combo]
        top = [num for num, _ in Counter(all_nums).most_common(3)]

        st.markdown("### 🔝 Números clave")
        render_ticket(top, modo)

        # ---------------- ANALISIS ----------------
        st.markdown("## 📊 Análisis de modo")

        tab1, tab2 = st.tabs(["Vista general", "Por clasificación"])

        with tab1:
            for combo, m in resultados_con_modo:
                render_analysis_row(combo, m)

        with tab2:

            st.markdown("### 🔵 Estructura")
            for combo, m in resultados_con_modo:
                if m == "ESTRUCTURA":
                    render_analysis_row(combo, m)

            st.markdown("### 🟢 Dispersión")
            for combo, m in resultados_con_modo:
                if m == "DISPERSIÓN":
                    render_analysis_row(combo, m)

        # ---------------- DATOS CRUDOS ----------------
        with st.expander("🧪 Modo experto"):
            st.write(resultados)
