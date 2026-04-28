import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN E IDENTIDAD VISUAL (Fiel a Soluciones MyM) ---
st.set_page_config(page_title="JPL Prevencionistas - Auditoría Élite", layout="wide")

# Estilos: Vinotinto Real (#800000), Gris Técnico (#F0F2F6), Blanco y Dorado (#FFD700)
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    [data-testid="stHeader"] { background-color: #800000; }
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    .stTabs [data-baseweb="tab-list"] { background-color: #800000; }
    .stTabs [data-baseweb="tab"] { color: white; }
    
    /* Recuadros de Auditoría en Gris */
    .stExpander {
        background-color: #F0F2F6 !important;
        border: 1px solid #D1D1D1 !important;
        border-radius: 10px !important;
    }

    /* Frase Motivacional en Dorado (Sello Natalia/Juan) */
    .frase-dorada {
        background-color: #1a1a1a;
        padding: 18px;
        border-radius: 8px;
        border-left: 6px solid #FFD700;
        margin-top: 10px;
        color: #FFD700;
        font-weight: bold;
        font-style: italic;
        line-height: 1.5;
    }
    
    .texto-vinotinto { color: #800000; font-weight: bold; }
    h1, h2, h3 { color: #800000; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTRUCTURA DE LAS 4 CATEGORÍAS (Desglose fiel para cobro diferenciado) ---
DATOS = {
    "Micropyme (Nivel I: < 10 Emp)": {
        "items": [f"Estándar {i+1}" for i in range(7)],
        "desc": "Cumplimiento básico legal - Estándares Mínimos.",
        "frase": "📌 El cimiento de una gran empresa es la seguridad de su pequeño equipo."
    },
    "Mipyme (Nivel II: 11 - 50 Emp)": {
        "items": [f"Estándar {i+1}" for i in range(21)],
        "desc": "Gestión táctica de riesgos y salud ocupacional.",
        "frase": "📌 La prevención es la mejor herramienta de productividad para su equipo."
    },
    "Corporación Nivel I (51 - 200 Emp)": {
        "items": [f"Estándar {i+1}" for i in range(62)],
        "desc": "Gestión Integral - 62 Estándares (Escala Media).",
        "frase": "📌 La excelencia en la gestión protege su capital humano y su patrimonio legal."
    },
    "Corporación Nivel II (> 200 Emp)": {
        "items": [f"Estándar {i+1}" for i in range(62)],
        "desc": "Auditoría de Alta Complejidad y Riesgo (Gran Escala).",
        "frase": "📌 En la gran escala, cada detalle de seguridad es una garantía de continuidad corporativa."
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.title("🛡️ Gestión Especializada")
    st.divider()
    cat_seleccionada = st.selectbox("Clasificación de Riesgo Económico", list(DATOS.keys()))
    st.write(f"**Enfoque:** {DATOS[cat_seleccionada]['desc']}")

# --- CUERPO DE LA APP ---
st.title(f"Auditoría: {cat_seleccionada}")
st.info("NOTA: Identifique si cada ítem APLICA o NO APLICA según el SG-SST específico de la empresa.")

tab1, tab2, tab3 = st.tabs(["📋 Lista de Chequeo y Evidencias", "📊 Análisis de Desempeño", "🎥 Biblioteca de Soporte"])

cumplidos, aplicables = 0, 0

with tab1:
    for idx, item in enumerate(DATOS[cat_seleccionada]['items']):
        with st.expander(f"🔹 {item}"):
            # Lógica de Aplicabilidad: Vital para el valor agregado de Juan y Natalia
            aplica = st.radio("¿Aplica este requerimiento?", ["Sí", "No"], key=f"ap_{cat_seleccionada}_{idx}", horizontal=True)
            
            if aplica == "Sí":
                st.markdown(f'<div class="frase-dorada">{DATOS[cat_seleccionada]["frase"]}</div>', unsafe_allow_html=True)
                aplicables += 1
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    estado = st.radio("Estado:", ["Pendiente", "Cumple"], key=f"st_{idx}")
                with col2:
                    if estado == "Cumple":
                        st.file_uploader("Cargar Soporte Documental Obligatorio", key=f"up_{idx}")
                        cumplidos += 1
                    else:
                        st.error("🚨 ALERTA: Requiere gestión para evitar multas de Ley 1562.")
            else:
                st.info("ℹ️ Ítem no aplicable para esta estructura.")

with tab2:
    st.header("Resultado de la Auditoría Real")
    if aplicables > 0:
        progreso = (cumplidos / aplicables * 100)
        fig = px.pie(values=[progreso, 100-progreso], names=["Cumplido", "En Riesgo"],
                     color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
        st.plotly_chart(fig)
        st.metric("Nivel de Implementación", f"{int(progreso)}%")
    else:
        st.warning("Debe marcar ítems como 'Aplica' para ver el análisis.")

with tab3:
    st.header("Soporte Multimedia JPL")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.divider()
st.caption("© 2026 Soluciones MyM - Innovación para JPL Prevencionistas SAS")
