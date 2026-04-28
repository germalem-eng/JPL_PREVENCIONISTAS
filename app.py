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
    
    /* Título de la App en Gris Ratón */
    .titulo-sidebar {
        color: #4F4F4F; /* Gris Ratón */
        font-weight: bold;
        font-size: 1.2em;
        margin-bottom: 10px;
    }

    /* Cuadro de Usuario con texto en Azul */
    .usuario-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        color: #00BFFF; /* Azul brillante para resaltar */
        font-weight: bold;
        border: 1px solid #00BFFF;
    }

    .stExpander {
        background-color: #F0F2F6 !important;
        border: 1px solid #D1D1D1 !important;
        border-radius: 10px !important;
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
    
    h1, h2, h3 { color: #800000; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTRUCTURA DE CATEGORÍAS (Basada en la tabla legal de multas subida) ---
DATOS = {
    "Micropyme (Nivel I: < 10 Emp)": {
        "items": [
            {"id": "1", "titulo": "Asignación de responsable del SG-SST", "evidencias": ["Acta de designación", "Licencia SST", "Curso 50h"], "frase": "📌 Contar con una persona competente garantiza que el sistema funcione y prevenga riesgos reales."},
            {"id": "2", "titulo": "Afiliación al Sistema de Seguridad Social", "evidencias": ["Planillas PILA", "Certificados ARL/EPS"], "frase": "📌 La afiliación adecuada protege al trabajador y evita sanciones económicas."},
            {"id": "3", "titulo": "Capacitación en SST", "evidencias": ["Cronograma", "Asistencias"], "frase": "📌 Capacitar es fortalecer la cultura de seguridad en todos los niveles."},
            {"id": "4", "titulo": "Plan Anual de Trabajo", "evidencias": ["Objetivos", "Recursos"], "frase": "📌 Un plan bien estructurado es la hoja de ruta hacia una empresa segura."},
            {"id": "5", "titulo": "Evaluaciones Médicas", "evidencias": ["Conceptos aptitud", "Seguimiento"], "frase": "📌 Cuidar la salud es proteger el activo más importante de la compañía."},
            {"id": "6", "titulo": "Identificación de Riesgos", "evidencias": ["Matriz GTC 45", "Controles"], "frase": "📌 Identificar peligros a tiempo evita que un incidente sea una tragedia."},
            {"id": "7", "titulo": "Medidas de Control", "evidencias": ["Mantenimiento", "Entrega EPP"], "frase": "📌 La prevención es una inversión en productividad y bienestar."}
        ]
    },
    "Mipyme (Nivel II: 11 - 50 Emp)": {
        "items": [{"id": str(i+1), "titulo": f"Estándar Técnico {i+1}", "evidencias": ["Documento Soporte", "Registro Ejecución"], "frase": "📌 La gestión técnica es el escudo ante auditorías legales."} for i in range(21)]
    },
    "Corporación Nivel I (51 - 200 Emp)": {
        "items": [{"id": str(i+1), "titulo": f"Estándar Corporativo {i+1}", "evidencias": ["Evidencia Técnica", "Validación ARL"], "frase": "📌 La excelencia en la gestión protege su capital humano y patrimonio legal."} for i in range(62)]
    },
    "Corporación Nivel II (> 200 Emp)": {
        "items": [{"id": str(i+1), "titulo": f"Estándar Alta Complejidad {i+1}", "evidencias": ["Auditoría Externa", "Soporte Maestro"], "frase": "📌 En la gran escala, cada detalle de seguridad es una garantía de continuidad corporativa."} for i in range(62)]
    }
}

# --- SIDEBAR ACTUALIZADO ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.markdown('<div class="titulo-sidebar">APP JPL PREVENCIONISTAS</div>', unsafe_allow_html=True)
    
    categoria = st.selectbox("Clasificación Organizacional", list(DATOS.keys()))
    
    st.divider()
    # Cuadro de usuario con texto blanco
    st.markdown('<div class="usuario-box">Usuario: JPL prevencionistas (Admin)</div>', unsafe_allow_html=True)

# --- CUERPO DE LA APP ---
st.title(f"Panel de Auditoría: {categoria}")
st.info("NOTA: Identifique si cada ítem APLICA o NO APLICA según el SG-SST de la empresa.")

tab1, tab2, tab3 = st.tabs(["📋 Auditoría y Evidencias", "📊 Gráficas de Control", "🎥 Soporte"])

cumplidos, aplicables = 0, 0

with tab1:
    for item in DATOS[categoria]['items']:
        with st.expander(f"🔹 {item['id']}. {item['titulo']}"):
            aplica = st.radio("¿Este requerimiento aplica?", ["Sí", "No"], key=f"ap_{categoria}_{item['id']}", horizontal=True)
            
            if aplica == "Sí":
                st.markdown(f'<div class="frase-dorada">{item["frase"]}</div>', unsafe_allow_html=True)
                for ev in item['evidencias']:
                    aplicables += 1
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        sel = st.radio(f"Cumple {ev}", ["No", "Sí"], key=f"sel_{categoria}_{item['id']}_{ev}")
                    with col2:
                        if sel == "Sí":
                            st.file_uploader(f"Cargar {ev}", key=f"f_{categoria}_{item['id']}_{ev}")
                            cumplidos += 1
                        else:
                            st.error("🚨 Pendiente de evidencia.")
            else:
                st.info("ℹ️ Ítem marcado como 'No Aplica'.")

with tab2:
    st.header("Análisis de Cumplimiento Real")
    if aplicables > 0:
        progreso = (cumplidos / aplicables * 100)
        fig = px.pie(values=[progreso, 100-progreso], names=["Cumplido", "Pendiente"], 
                     color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
        st.plotly_chart(fig, use_container_width=True)
        st.metric("Implementación Actual", f"{int(progreso)}%")
    else:
        st.warning("Seleccione ítems aplicables para generar estadísticas.")

with tab3:
    st.header("Material de Capacitación")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.divider()
st.caption("Soluciones MyM - Innovación para JPL Prevencionistas SAS | 2026")
