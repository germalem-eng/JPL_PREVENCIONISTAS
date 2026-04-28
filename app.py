import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- CONFIGURACIÓN E IDENTIDAD VISUAL ---
st.set_page_config(page_title="JPL Prevencionistas - Auditoría Élite", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    [data-testid="stHeader"] { background-color: #800000; }
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    .stTabs [data-baseweb="tab-list"] { background-color: #800000; }
    .stTabs [data-baseweb="tab"] { color: white; }
    
    .titulo-sidebar { color: #F0EAD6; font-weight: bold; font-size: 1.2em; text-align: center; text-transform: uppercase; margin-bottom: 15px; }

    .usuario-box {
        background-color: #D3D3D3; padding: 12px; border-radius: 8px;
        color: #000000; font-weight: bold; font-size: 0.85em; text-align: center; border: 1px solid #A9A9A9;
    }

    .frase-dorada {
        background-color: #1a1a1a; padding: 18px; border-radius: 8px;
        border-left: 6px solid #FFD700; margin-top: 10px; color: #FFD700;
        font-weight: bold; font-style: italic;
    }
    
    .alerta-multa { background-color: #f8d7da; color: #721c24; padding: 15px; border-radius: 5px; border: 1px solid #f5c6cb; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS LEGAL ---
INFO_LEGAL = {
    "Micropyme (<10 Emp)": {"multa": "Hasta 24 SMMMLV", "n_items": 7, "prefix": "Estándar Mínimo"},
    "Mipyme (11-50 Emp)": {"multa": "Hasta 150 SMMMLV", "n_items": 21, "prefix": "Estándar Técnico"},
    "Corporación I (51-200 Emp)": {"multa": "Hasta 400 SMMMLV", "n_items": 62, "prefix": "Gestión Corporativa"},
    "Corporación II (>200 Emp)": {"multa": "Hasta 1000 SMMMLV", "n_items": 62, "prefix": "Alta Complejidad"}
}

FRASES = [
    "📌 La seguridad es el cimiento de la productividad corporativa.",
    "📌 Un entorno seguro es un entorno eficiente y rentable.",
    "📌 La prevención hoy evita la crisis de mañana.",
    "📌 El cumplimiento legal es la mejor inversión para su patrimonio."
]

# --- ESTADO DE SESIÓN ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "es_premium" not in st.session_state:
    st.session_state.es_premium = False
if "usuario_nombre" not in st.session_state:
    st.session_state.usuario_nombre = ""

# --- LOGIN ---
if not st.session_state.autenticado:
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
        st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
        user_input = st.text_input("ID de Usuario (Ej: Gerardo)")
        token_input = st.text_input("Clave Dinámica (Token)", type="password")
        
        if st.button("Validar Acceso Premium"):
            if token_input == "2026JPL":
                st.session_state.autenticado = True
                st.session_state.es_premium = True
                st.session_state.usuario_nombre = user_input if user_input else "JPL PREVENCIONISTAS S.A.S"
                st.rerun()
            else:
                st.error("Token incorrecto")
        
        if st.button("Ingresar como Invitado"):
            st.session_state.autenticado = True
            st.session_state.es_premium = False
            st.session_state.usuario_nombre = "Invitado"
            st.rerun()
    st.stop()

# --- SIDEBAR POST-LOGIN ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
    
    categoria = st.selectbox("Estructura de Auditoría", list(INFO_LEGAL.keys()))
    st.divider()
    
    # Usuario en recuadro gris con texto negro
    status_label = "(Admin)" if st.session_state.es_premium else "(Demo)"
    st.markdown(f'<div class="usuario-box">Usuario: {st.session_state.usuario_nombre} {status_label}</div>', unsafe_allow_html=True)
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- CUERPO PRINCIPAL ---
st.title(f"Módulo: {categoria}")
tab1, tab2, tab3, tab4 = st.tabs(["📋 Estándares", "📊 Gráficas", "📈 Cronograma", "💎 Premium"])

cumplidos = 0
total_activos = INFO_LEGAL[categoria]['n_items']

with tab1:
    st.info(f"Mostrando los {total_activos} estándares oficiales.")
    for i in range(1, total_activos + 1):
        with st.expander(f"🔹 {INFO_LEGAL[categoria]['prefix']} {i}"):
            st.markdown(f'<div class="frase-dorada">{FRASES[i % len(FRASES)]}</div>', unsafe_allow_html=True)
            aplica = st.radio("¿Aplica?", ["Sí", "No"], key=f"it_{categoria}_{i}", horizontal=True)
            if aplica == "Sí":
                if st.session_state.es_premium:
                    st.file_uploader(f"Soporte Estándar {i}", key=f"file_{i}")
                    if st.checkbox("¿Cumple?", key=f"c_{i}"): cumplidos += 1
                else:
                    st.warning("🔒 Carga de evidencias bloqueada en modo Invitado.")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(values=[cumplidos, total_activos-cumplidos], names=["Cumple", "Riesgo"], 
                     color_discrete_sequence=['#800000', '#D3D3D3'], hole=.5)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown(f'<div class="alerta-multa">⚠️ RIESGO POR LEY 1562:<br>Sanción máxima: {INFO_LEGAL[categoria]["multa"]}</div>', unsafe_allow_html=True)

with tab3:
    st.header("Línea de Tiempo")
    df_t = pd.DataFrame([dict(Tarea="Diagnóstico", Inicio='2026-04-01', Fin='2026-04-20'), dict(Tarea="Mejora", Inicio='2026-04-21', Fin='2026-06-01')])
    st.plotly_chart(px.timeline(df_t, x_start="Inicio", x_end="Fin", y="Tarea", color_discrete_sequence=['#800000']))

with tab4:
    if st.session_state.es_premium:
        st.success("✅ Acceso Premium Activo")
        st.button("Generar Reporte PDF Final")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        st.error("🔒 Contenido bloqueado. Adquiera su clave con JPL Prevencionistas.")

st.divider()
st.caption("Soluciones MyM - Bogotá, Colombia 2026")
