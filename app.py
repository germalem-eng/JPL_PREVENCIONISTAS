import streamlit as st
import pandas as pd
import plotly.express as px

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
    
    .alerta-multa {
        background-color: #f8d7da; color: #721c24; padding: 15px;
        border-radius: 5px; border: 1px solid #f5c6cb; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE MULTAS (LEY 1562) ---
MULTAS = {
    "Micropyme (<10 Emp)": "Hasta 24 SMMMLV",
    "Mipyme (11-50 Emp)": "Hasta 150 SMMMLV",
    "Corporación I (51-200 Emp)": "Hasta 400 SMMMLV",
    "Corporación II (>200 Emp)": "Hasta 1000 SMMMLV"
}

# --- SISTEMA DE SESIÓN ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "es_premium" not in st.session_state:
    st.session_state.es_premium = False

# --- LOGIN ---
if not st.session_state.autenticado:
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
        st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
        token = st.text_input("Clave Dinámica (Premium)", type="password")
        if st.button("Acceso Premium"):
            if token == "2026JPL":
                st.session_state.autenticado = True
                st.session_state.es_premium = True
                st.rerun()
        if st.button("Acceso Invitado"):
            st.session_state.autenticado = True
            st.session_state.es_premium = False
            st.rerun()
    st.warning("🔒 Por favor, seleccione un modo de acceso en el panel lateral.")
    st.stop()

# --- SIDEBAR POST-LOGIN ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
    
    categoria = st.selectbox("Categoría de Auditoría", list(MULTAS.keys()))
    st.divider()
    
    user_label = "JPL PREVENCIONISTAS S.A.S (Admin)" if st.session_state.es_premium else "MODO INVITADO (Demo)"
    st.markdown(f'<div class="usuario-box">Usuario: {user_label}</div>', unsafe_allow_html=True)
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- CONTENIDO PRINCIPAL ---
st.title(f"Sistema de Auditoría - {categoria}")

tab1, tab2, tab3, tab4 = st.tabs(["📋 Estándares", "📊 Gráficas", "📈 Línea de Tiempo", "💎 Zona Premium"])

# Simulación de datos para que el invitado vea movimiento
cumplidos, totales = 4, 7

with tab1:
    st.info("Identifique si el ítem aplica. El modo Invitado no permite cargar archivos.")
    with st.expander("🔹 Estándar 1: Asignación de Responsable"):
        st.markdown('<div class="frase-dorada">📌 La seguridad es el cimiento de la productividad corporativa.</div>', unsafe_allow_html=True)
        aplica = st.radio("¿Aplica?", ["Sí", "No"], key="it1")
        if aplica == "Sí":
            if st.session_state.es_premium:
                st.file_uploader("Subir Evidencia Legal")
            else:
                st.warning("🔒 Carga de archivos bloqueada para invitados.")

with tab2:
    st.header("Análisis de Riesgo Actual")
    fig = px.pie(values=[cumplidos, totales-cumplidos], names=["Cumplido", "En Riesgo"], 
                 color_discrete_sequence=['#800000', '#D3D3D3'], hole=.5)
    st.plotly_chart(fig, use_container_width=True)
    
    # MOSTRAR MULTAS (El gancho comercial)
    st.markdown(f"""
        <div class="alerta-multa">
            ⚠️ RIESGO ECONÓMICO DETECTADO:<br>
            Según Ley 1562, por su categoría, las multas pueden ascender hasta: {MULTAS[categoria]}
        </div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("Línea de Tiempo de Implementación")
    df_timeline = pd.DataFrame([
        dict(Tarea="Fase 1: Diagnóstico", Inicio='2026-04-01', Fin='2026-04-10'),
        dict(Tarea="Fase 2: Documentación", Inicio='2026-04-11', Fin='2026-05-15')
    ])
    fig_time = px.timeline(df_timeline, x_start="Inicio", x_end="Fin", y="Tarea", color_discrete_sequence=['#800000'])
    st.plotly_chart(fig_time, use_container_width=True)

with tab4:
    if st.session_state.es_premium:
        st.success("Acceso total habilitado.")
        st.button("Descargar Reporte PDF")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        st.error("🛑 ACCESO RESTRINGIDO")
        st.markdown("""
            **El modo Premium incluye:**
            * Descarga de Reportes Ejecutivos para ARL.
            * Carga ilimitada de evidencias en la nube.
            * Acceso a la videoteca de capacitación de Natalia y Juan.
            * Soporte técnico prioritario por Soluciones MyM.
        """)
        if st.button("Solicitar Código Premium"):
            st.info("Contacte a JPL Prevencionistas para adquirir su suscripción.")

st.divider()
st.caption("Soluciones MyM - Innovación para JPL Prevencionistas SAS | 2026")
