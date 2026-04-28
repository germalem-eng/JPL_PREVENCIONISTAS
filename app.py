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
    
    .titulo-sidebar { color: #F0EAD6; font-weight: bold; font-size: 1.3em; margin-bottom: 15px; text-align: center; }

    .usuario-box {
        background-color: #D3D3D3; padding: 12px; border-radius: 8px;
        color: #000000; font-weight: bold; font-size: 0.9em; text-align: center; border: 1px solid #A9A9A9;
    }

    .frase-dorada {
        background-color: #1a1a1a; padding: 18px; border-radius: 8px;
        border-left: 6px solid #FFD700; margin-top: 10px; color: #FFD700;
        font-weight: bold; font-style: italic;
    }
    
    h1, h2, h3 { color: #800000; }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE SEGURIDAD (TOKEN DINÁMICO) ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "es_premium" not in st.session_state:
    st.session_state.es_premium = False

def login():
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
        st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
        
        st.subheader("Acceso al Sistema")
        user = st.text_input("ID de Usuario")
        token = st.text_input("Clave Dinámica / Token", type="password")
        
        col_inv, col_pre = st.columns(2)
        
        with col_inv:
            if st.button("Entrar Invitado"):
                st.session_state.autenticado = True
                st.session_state.es_premium = False
                st.rerun()
        
        with col_pre:
            if st.button("Validar Premium"):
                # Aquí simulamos la clave dinámica estilo banco (ejemplo: 2026JPL)
                if token == "2026JPL": 
                    st.session_state.autenticado = True
                    st.session_state.es_premium = True
                    st.success("Token Válido")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Token Incorrecto")

# --- LÓGICA DE CONTENIDO ---
if not st.session_state.autenticado:
    login()
    st.warning("⚠️ Inicie sesión para acceder a la auditoría.")
    st.stop()

# --- SI ESTÁ AUTENTICADO, MOSTRAR APP ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
    
    # Categorías basadas en tus 4 divisiones de cobro
    opciones = ["Micropyme (<10 Emp)", "Mipyme (11-50 Emp)", "Corporación I (51-200 Emp)", "Corporación II (>200 Emp)"]
    categoria = st.selectbox("Estructura Organizacional", opciones)
    
    st.divider()
    # Recuadro de Usuario según tu pedido
    label_user = "JPL PREVENCIONISTAS S.A.S (Admin)" if st.session_state.es_premium else "USUARIO INVITADO (Lectura)"
    st.markdown(f'<div class="usuario-box">Usuario: {label_user}</div>', unsafe_allow_html=True)
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- CUERPO DE LA APP ---
st.title(f"Módulo de Auditoría: {categoria}")

if not st.session_state.es_premium:
    st.warning("🔓 Estás en modo INVITADO. Puedes visualizar, pero la carga de evidencias y reportes está reservada para cuentas PREMIUM.")

tab1, tab2, tab3 = st.tabs(["📋 Lista de Chequeo", "📊 Gráficas de Control", "📄 Reporte Final"])

with tab1:
    st.info("Identifique si aplica o no según el SG-SST de la empresa.")
    # Ejemplo de ítem con frase dorada
    with st.expander("🔹 Estándar: Asignación de Responsable"):
        st.markdown('<div class="frase-dorada">📌 La seguridad es el cimiento de la productividad corporativa.</div>', unsafe_allow_html=True)
        aplica = st.radio("¿Aplica?", ["Sí", "No"], key="ap_1")
        if aplica == "Sí":
            if st.session_state.es_premium:
                st.file_uploader("Cargar Soporte Documental")
            else:
                st.info("Para cargar evidencias, adquiera el módulo Premium.")

with tab2:
    # Gráficas dinámicas (se mantienen fieles a lo avanzado)
    fig = px.pie(values=[70, 30], names=["Cumplido", "Pendiente"], color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    if st.session_state.es_premium:
        st.success("✅ Generación de Reporte PDF habilitada.")
        st.button("Descargar Informe Ejecutivo")
    else:
        st.error("🔒 Función Bloqueada: El reporte final solo está disponible para clientes Premium con Soluciones MyM.")
