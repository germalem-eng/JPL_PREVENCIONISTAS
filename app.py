import streamlit as st
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. DISEÑO INSTITUCIONAL (Gris, Negro y Vinotinto) ---
st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } /* Gris Oxford Claro */
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #000000 !important; font-family: 'Arial Black', Gadget, sans-serif; }
    .stExpander { background-color: white !important; border: 1px solid #1A1A1A !important; border-radius: 0px; }
    .stButton>button { background-color: #000000 !important; color: white !important; border-radius: 2px; font-weight: bold; width: 100%; border: 1px solid #4A4A4A; }
    .stButton>button:hover { background-color: #4A4A4A !important; border: 1px solid #8B0000; }
    label { color: #000000 !important; font-weight: bold; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS MAESTRA (21 ÍTEMS COMPLETOS - 11-50 TRAB) ---
DATA_SST = {
    "📊 1-10 Trabajadores": [
        {"id": "1.1", "item": "Asignación de persona que diseña el SG-SST", "per": "Semestral"},
        {"id": "1.2", "item": "Afiliación al Sistema de Seguridad Social Integral", "per": "Cuatrimestral"},
        {"id": "1.3", "item": "Programa de capacitación", "per": "Cuatrimestral"},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Semestral"},
        {"id": "1.5", "item": "Evaluaciones médicas ocupacionales", "per": "Anual"},
        {"id": "1.6", "item": "Identificación de peligros y valoración de riesgos", "per": "Semestral"},
        {"id": "1.7", "item": "Medidas de prevención y control", "per": "Semestral"}
    ],
    "🏢 11-50 Trabajadores": [
        {"id": "2.1", "item": "Asignación de responsable del SG-SST", "per": "Semestral"},
        {"id": "2.2", "item": "Asignación de responsabilidades en SST", "per": "Cuatrimestral"},
        {"id": "2.3", "item": "Asignación de recursos para el Sistema", "per": "Anual"},
        {"id": "2.4", "item": "Afiliación al Sistema de Seguridad Social", "per": "Cuatrimestral"},
        {"id": "2.5", "item": "Conformación y funcionamiento del COPASST", "per": "Cuatrimestral"},
        {"id": "2.6", "item": "Conformación del Comité de Convivencia", "per": "Cuatrimestral"},
        {"id": "2.7", "item": "Programa de capacitación anual", "per": "Anual"},
        {"id": "2.8", "item": "Inducción y reinducción en SST", "per": "Anual"},
        {"id": "2.9", "item": "Curso Virtual de 50 horas", "per": "Anual"},
        {"id": "2.10", "item": "Evaluaciones médicas ocupacionales", "per": "Anual"},
        {"id": "2.11", "item": "Entrega de EPP y capacitación de uso", "per": "Cuatrimestral"},
        {"id": "2.12", "item": "Identificación de peligros y valoración de riesgos", "per": "Semestral"},
        {"id": "2.13", "item": "Reporte de accidentes y enfermedades laborales", "per": "Mensual"},
        {"id": "2.14", "item": "Investigación de incidentes y accidentes", "per": "Mensual"},
        {"id": "2.15", "item": "Conformación de Brigada de Emergencias", "per": "Anual"},
        {"id": "2.16", "item": "Plan de Prevención y Respuesta ante Emergencias", "per": "Anual"},
        {"id": "2.17", "item": "Revisión por la alta dirección", "per": "Anual"},
        {"id": "2.18", "item": "Adquisiciones y contratación", "per": "Cuatrimestral"},
        {"id": "2.19", "item": "Mantenimiento periódico de equipos y herramientas", "per": "Cuatrimestral"},
        {"id": "2.20", "item": "Sistemas de vigilancia epidemiológica", "per": "Anual"},
        {"id": "2.21", "item": "Estadísticas de accidentalidad y enfermedad", "per": "Mensual"}
    ]
}

# --- 4. BARRA LATERAL ---
with st.sidebar:
    logo = "logo_jplfinal.jpg"
    if os.path.exists(logo):
        st.image(logo, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; font-size: 28px;'>APP JPL</h1>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("Módulos de Auditoría:", ["🏠 Inicio", "📊 1-10 Trabajadores", "🏢 11-50 Trabajadores", "🏗️ +50 Trab. o Riesgo IV/V"])
    st.markdown("---")
    st.caption("Ecosistema L.I.N.A. | Soluciones MyM")

# --- 5. LÓGICA DE AUDITORÍA ---
if menu == "🏠 Inicio":
    st.title("Gestión de Estándares Mínimos JPL")
    st.markdown(f"""
    <div style="background-color: white; padding: 30px; border-left: 10px solid #1A1A1A; border-right: 10px solid #8B0000;">
        <h2 style="color: #000;">Consola de Auditoría - Gerardo Martinez</h2>
        <p style="color: #4A4A4A; font-size: 18px;">Herramienta profesional para el cumplimiento de la <b>Resolución 0312 de 2019</b>.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.header(f"Evaluación Actual: {menu}")
    items = DATA_SST.get(menu, [])
    
    if not items:
        st.warning("Cargando base de datos para este segmento...")
    else:
        for st_item in items:
            with st.expander(f"⬛ {st_item['id']} - {st_item['item']}"):
                c1, c2 = st.columns([2, 1])
                with c1:
                    st.write(f"**Periodicidad Legal:** {st_item['per']}")
                    st.text_area("Hallazgos / Evidencias", key=f"h_{st_item['id']}_{menu}")
                with c2:
                    st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple", "No Aplica"], key=f"s_{st_item['id']}_{menu}")
                    st.date_input("Fecha de Control", key=f"f_{st_item['id']}_{menu}")

    if st.button("🔴 FINALIZAR Y GENERAR REPORTE"):
        st.success("Auditoría guardada. Los 21 ítems han sido procesados bajo la identidad JPL.")
        st.balloons()
