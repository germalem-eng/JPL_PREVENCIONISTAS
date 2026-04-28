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
    
    /* Título en Blanco Perla */
    .titulo-sidebar {
        color: #F0EAD6; 
        font-weight: bold;
        font-size: 1.2em;
        margin-bottom: 15px;
        text-align: center;
        text-transform: uppercase;
    }

    /* Recuadro Gris con Texto Negro para Usuario */
    .usuario-box {
        background-color: #D3D3D3; 
        padding: 12px;
        border-radius: 8px;
        color: #000000; 
        font-weight: bold;
        font-size: 0.85em;
        text-align: center;
        border: 1px solid #A9A9A9;
    }

    .frase-dorada {
        background-color: #1a1a1a;
        padding: 18px;
        border-radius: 8px;
        border-left: 6px solid #FFD700;
        margin-top: 10px;
        color: #FFD700;
        font-weight: bold;
        font-style: italic;
    }
    
    .alerta-multa {
        background-color: #f8d7da;
        color: #721c24;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO DE SESIÓN ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "es_premium" not in st.session_state:
    st.session_state.es_premium = False
if "usuario_nombre" not in st.session_state:
    st.session_state.usuario_nombre = ""

# --- BLOQUE DE ACCESO (LOGIN) ---
if not st.session_state.autenticado:
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
        st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
        
        st.subheader("Control de Acceso")
        user_input = st.text_input("ID de Usuario (Ej: Gerardo)")
        token_input = st.text_input("Clave Dinámica (Token)", type="password")
        
        if st.button("Validar Acceso Premium"):
            if token_input == "2026JPL":
                st.session_state.autenticado = True
                st.session_state.es_premium = True
                st.session_state.usuario_nombre = user_input if user_input else "JPL PREVENCIONISTAS S.A.S"
                st.success("Acceso Premium validado")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Token incorrecto")
        
        if st.button("Ingresar como Invitado"):
            st.session_state.autenticado = True
            st.session_state.es_premium = False
            st.session_state.usuario_nombre = "Invitado"
            st.rerun()
    
    st.info("👋 Bienvenida(o). Por favor use el panel lateral para ingresar.")
    st.stop()

# --- SI ESTÁ AUTENTICADO: MOSTRAR CONTENIDO ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
    
    opciones = ["Micropyme (<10 Emp)", "Mipyme (11-50 Emp)", "Corporación I (51-200 Emp)", "Corporación II (>200 Emp)"]
    categoria = st.selectbox("Estructura de Auditoría", opciones)
    
    st.divider()
    # Recuadro gris con texto negro (Admin para Premium, Invitado para el resto)
    status = "(Admin)" if st.session_state.es_premium else "(Demo)"
    st.markdown(f'<div class="usuario-box">Usuario: {st.session_state.usuario_nombre} {status}</div>', unsafe_allow_html=True)
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- CONTENIDO DE AUDITORÍA ---
st.title(f"Módulo de Auditoría: {categoria}")

tab1, tab2, tab3 = st.tabs(["📋 Estándares y Evidencias", "📊 Gráficas y Riesgos", "📄 Reportes Premium"])

with tab1:
    with st.expander("🔹 Estándar 1: Responsable del Sistema"):
        st.markdown('<div class="frase-dorada">📌 La seguridad es el cimiento de la productividad corporativa.</div>', unsafe_allow_html=True)
        if st.session_state.es_premium:
            st.file_uploader("Cargar soporte legal")
        else:
            st.warning("🔒 Función de carga bloqueada para invitados.")

with tab2:
    st.header("Análisis de Riesgo Económico")
    fig = px.pie(values=[60, 40], names=["Cumplido", "En Riesgo"], color_discrete_sequence=['#800000', '#D3D3D3'], hole=.5)
    st.plotly_chart(fig)
    
    # Simulación de multas cargadas previamente
    st.markdown("""
        <div class="alerta-multa">
            ⚠️ <b>ALERTA DE MULTA LEY 1562:</b><br>
            Su empresa podría enfrentar sanciones proporcionales a su tamaño por incumplimiento.
        </div>
    """, unsafe_allow_html=True)

with tab3:
    if st.session_state.es_premium:
        st.success("Acceso total habilitado.")
        st.button("Descargar Reporte Ejecutivo PDF")
    else:
        st.error("🛑 Acceso Restringido: El reporte final solo está disponible en la versión Premium.")
