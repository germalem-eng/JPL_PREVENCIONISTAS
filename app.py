import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="App JPL - Gestión SST", layout="wide")

# --- TRUCO DE DISEÑO PARA BOTONES Y TEXTO ---
st.markdown("""
    <style>
    /* 1. Fondo general de la barra lateral (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #8B0000 !important;
    }

    /* 2. Cuadros de texto (Usuario y Clave) */
    div[data-baseweb="input"] {
        background-color: white !important;
        border-radius: 5px !important;
    }
    
    input {
        color: black !important; /* Texto que escribes en negro */
        -webkit-text-fill-color: black !important;
    }

    /* 3. BOTONES (Acceder, Inicio, Estadísticas) */
    /* Esto obliga a que el botón sea BLANCO con letras NEGRAS */
    .stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 5px !important;
        height: 3em !important;
        width: 100% !important;
        visibility: visible !important;
    }

    /* 4. Etiquetas de texto (Usuario / Clave) */
    .stWidgetLabel p {
        color: white !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)
# --- 2. BASE DE DATOS TÉCNICA (EXTRAÍDA DE TUS APUNTES) ---
# Estándares adicionales del cuaderno
E_7 = [
    "Asignación de la persona que diseña el SG-SST",
    "Capacitación (Programa de capacitación)",
    "Matriz (Procedimientos, Metodología, Controles)",
    "Recursos para el Sistema",
    "Afiliación a Seguridad Social",
    "Plan Anual de Trabajo",
    "Evaluaciones Médicas Ocupacionales"
]

# Nuevos ítems de tus notas
ESTANDARES_ADICIONALES = {
    "COPASST": "Gestión de comité y actas",
    "POLÍTICA": "Revisión anual (Septiembre)",
    "PERFIL SOCIODEMOGRÁFICO": "Actualización trimestral (Enero/Abril/Julio)",
    "INVESTIGACIÓN AT": "Investigación de Incidentes y Accidentes",
    "ENTREGA DE EPP": "Registro y control de dotación"
}

# --- 3. ESTILOS CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stApp { background-color: #F8F9FA; }
    .timeline-box {
        border-left: 6px solid #800000;
        padding: 15px 25px;
        margin: 15px 0;
        background: #ffffff;
        border-radius: 0 15px 15px 0;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.05);
    }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background: #F2F2F2; text-align: center; padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; }
</style>
""", unsafe_allow_html=True)

# --- 4. ESTADO DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'respuestas' not in st.session_state: st.session_state.respuestas = {}
if 'autenticado' not in st.session_state: st.session_state.autenticado = False

# --- 5. SIDEBAR ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    if not st.session_state.autenticado:
        u = st.text_input("Usuario")
        p = st.text_input("Clave", type="password")
        if st.button("ACCEDER"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Sesión: Gerardo")
        if st.button("SALIR"): st.session_state.autenticado = False; st.rerun()
    
    st.divider()
    if st.button("🏠 INICIO"): st.session_state.pantalla = 'inicio'; st.rerun()
    if st.button("📊 ESTADÍSTICAS"): st.session_state.pantalla = 'stats'; st.rerun()

# --- 6. PANTALLAS ---

if st.session_state.pantalla == 'inicio':
    st.title("🛡️ Diagnóstico de Alerta Temprana")
    st.write("Seleccione el nivel de evaluación según sus apuntes de la norma 0312:")
    
    c1, c2, c3 = st.columns(3)
    if c1.button("🏢 MICRO (7)"): st.session_state.nivel = "7"; st.session_state.pantalla = 'auditoria'; st.rerun()
    if c2.button("🏬 PYME (21)"): st.session_state.nivel = "21"; st.session_state.pantalla = 'auditoria'; st.rerun()
    if c3.button("🏭 GRANDE (62)"): st.session_state.nivel = "62"; st.session_state.pantalla = 'auditoria'; st.rerun()

    st.divider()
    st.markdown("### 📋 Soporte y Consultoría JPL")
    p1, p2, p3, p4 = st.columns(4)
    planes = [("Asesoría Micro", "$30.000"), ("Soporte Pyme", "$60.000"), ("Gestión Grande", "$100.000"), ("Corporativo", "Convenio")]
    for i, (n, v) in enumerate(planes):
        with [p1, p2, p3, p4][i]:
            st.markdown(f"**{n}**\n\n{v}")

elif st.session_state.pantalla == 'auditoria':
    st.header(f"Instrumento Diagnóstico: Nivel {st.session_state.nivel}")
    
    # Cálculo de progreso
    lista = E_7 if st.session_state.nivel == "7" else list(ESTANDARES_ADICIONALES.keys())
    cumplidos = sum(1 for it in lista if st.session_state.respuestas.get(it) == "CUMPLE")
    total = len(lista)
    porcentaje = round((cumplidos / total) * 100, 2)

    # Gráfico circular (Pie Chart) igual al de tu dibujo
    fig = px.pie(values=[porcentaje, 100-porcentaje], names=['Cumple', 'Pendiente'], 
                 color_discrete_sequence=['#800000', '#C0C0C0'], hole=0.4)
    fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=250)
    
    col_graph, col_alert = st.columns([1, 2])
    with col_graph:
        st.plotly_chart(fig, use_container_width=True)
    
    with col_alert:
        color = "red" if porcentaje < 60 else "orange" if porcentaje < 85 else "green"
        st.markdown(f"""<div class='timeline-box' style='border-left-color:{color};'>
            <h3 style='color:{color};'>ESTADO: {porcentaje}%</h3>
            <p><b>Alerta:</b> Evaluación basada en la Resolución 0312 de 2019.</p>
        </div>""", unsafe_allow_html=True)

    st.write("---")
    for it in lista:
        c_a, c_b = st.columns([2, 1])
        res = c_a.radio(f"**{it}**", ["Pendiente", "CUMPLE", "NO CUMPLE"], key=it, horizontal=True, disabled=not st.session_state.autenticado)
        st.session_state.respuestas[it] = res
        c_b.text_input("Observación", key=f"obs_{it}", disabled=not st.session_state.autenticado)

# --- 7. PIE DE PÁGINA ---
st.markdown(f"""<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus
</div>""", unsafe_allow_html=True)
