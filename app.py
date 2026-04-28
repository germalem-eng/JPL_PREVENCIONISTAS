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

# --- BASE DE DATOS DE MULTAS Y ESTÁNDARES ---
INFO_LEGAL = {
    "Micropyme (<10 Emp)": {"multa": "24 SMMMLV", "n_items": 7, "prefix": "Estándar Mínimo"},
    "Mipyme (11-50 Emp)": {"multa": "150 SMMMLV", "n_items": 21, "prefix": "Estándar Técnico"},
    "Corporación I (51-200 Emp)": {"multa": "400 SMMMLV", "n_items": 62, "prefix": "Gestión Corporativa"},
    "Corporación II (>200 Emp)": {"multa": "1000 SMMMLV", "n_items": 62, "prefix": "Alta Complejidad"}
}

# Frases motivacionales que rotarán
FRASES = [
    "📌 La seguridad es el cimiento de la productividad corporativa.",
    "📌 Un entorno seguro es un entorno eficiente y rentable.",
    "📌 La prevención hoy evita la crisis de mañana.",
    "📌 El cumplimiento legal es la mejor inversión para su patrimonio."
]

# --- SISTEMA DE SESIÓN ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "es_premium" not in st.session_state:
    st.session_state.es_premium = False

# --- ACCESO ---
if not st.session_state.autenticado:
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
        st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
        token = st.text_input("Clave Dinámica (Premium)", type="password")
        if st.button("Validar Acceso Premium"):
            if token == "2026JPL":
                st.session_state.autenticado = True
                st.session_state.es_premium = True
                st.rerun()
        if st.button("Continuar como Invitado"):
            st.session_state.autenticado = True
            st.session_state.es_premium = False
            st.rerun()
    st.stop()

# --- PANEL LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS SAS</div>', unsafe_allow_html=True)
    
    categoria = st.selectbox("Clasificación de Empresa", list(INFO_LEGAL.keys()))
    st.divider()
    
    user_label = "JPL PREVENCIONISTAS S.A.S (Admin)" if st.session_state.es_premium else "ACCESO DEMOSTRATIVO"
    st.markdown(f'<div class="usuario-box">Usuario: {user_label}</div>', unsafe_allow_html=True)
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- CONTENIDO ---
st.title(f"Módulo de Auditoría - {categoria}")
st.write(f"Criterio: {INFO_LEGAL[categoria]['n_items']} estándares aplicables.")

tab1, tab2, tab3, tab4 = st.tabs(["📋 Auditoría de Ítems", "📊 Dashboard", "📅 Cronograma", "🎥 Videoteca Premium"])

# Contador dinámico para gráficas
cumplidos = 0
total_activos = INFO_LEGAL[categoria]['n_items']

with tab1:
    st.info("Revise la aplicabilidad de cada estándar. La carga de evidencias requiere cuenta activa.")
    for i in range(1, total_activos + 1):
        with st.expander(f"🔹 {INFO_LEGAL[categoria]['prefix']} {i}"):
            st.markdown(f'<div class="frase-dorada">{FRASES[i % len(FRASES)]}</div>', unsafe_allow_html=True)
            aplica = st.radio("¿Aplica?", ["Sí", "No"], key=f"check_{categoria}_{i}", horizontal=True)
            if aplica == "Sí":
                if st.session_state.es_premium:
                    st.file_uploader(f"Cargar soporte estándar {i}")
                    if st.checkbox("Marcar como cumplido", key=f"cumple_{i}"):
                        cumplidos += 1
                else:
                    st.warning("🔒 El modo invitado permite visualizar pero no gestionar evidencias.")

with tab2:
    st.header("Análisis de Riesgo y Cumplimiento")
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        # Gráfica de cumplimiento
        fig = px.pie(values=[cumplidos, total_activos-cumplidos], names=["Cumplido", "Pendiente"], 
                     color_discrete_sequence=['#800000', '#D3D3D3'], hole=.5)
        st.plotly_chart(fig, use_container_width=True)
    
    with col_g2:
        st.markdown(f"""
            <div class="alerta-multa">
                ⚠️ RIESGO ECONÓMICO CALCULADO:<br><br>
                Bajo la Ley 1562, el incumplimiento en su categoría conlleva multas de hasta:<br>
                <span style="font-size: 1.2em;">{INFO_LEGAL[categoria]['multa']}</span>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.header("Línea de Tiempo de Ejecución")
    df = pd.DataFrame([
        dict(Tarea="Fase de Diagnóstico", Inicio='2026-04-01', Fin='2026-04-15'),
        dict(Tarea="Fase de Implementación", Inicio='2026-04-16', Fin='2026-06-30')
    ])
    fig_line = px.timeline(df, x_start="Inicio", x_end="Fin", y="Tarea", color_discrete_sequence=['#800000'])
    st.plotly_chart(fig_line, use_container_width=True)

with tab4:
    if st.session_state.es_premium:
        st.success("Acceso total a la videoteca y descarga de reportes habilitado.")
        st.button("Descargar Reporte Final (PDF)")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Video de ejemplo
    else:
        st.error("🛑 Acceso Restringido")
        st.write("Para descargar su informe de auditoría y acceder a los videos de capacitación, debe activar su licencia Premium.")
        if st.button("Contactar Asesor"):
            st.info("Enviando solicitud a JPL Prevencionistas...")

st.divider()
st.caption("Soluciones MyM - Innovación para el sector Corporativo | 2026")
