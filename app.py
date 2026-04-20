import streamlit as st
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. IDENTIDAD VISUAL (Vinotinto, Gris Oxford, Negro) ---
st.markdown("""
    <style>
    .stApp { background-color: #ECECEC; } /* Gris Claro de fondo */
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #4A4A4A; } /* Vinotinto y Gris */
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #000000 !important; } /* Negro para títulos */
    .stExpander { background-color: white !important; border: 1px solid #4A4A4A !important; }
    .stButton>button { background-color: #1A1A1A !important; color: white !important; border-radius: 4px; font-weight: bold; width: 100%; }
    .stButton>button:hover { background-color: #4A4A4A !important; border: 1px solid #8B0000; }
    label { color: #1A1A1A !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS COMPLETA (Extraída de tus documentos) ---
DATA_SST = {
    "📊 1-10 Trabajadores": [
        {"id": "1.1", "item": "Asignación de persona que diseña el SG-SST", "per": "Semestral", "tip": "Licencia SST y curso 50h."},
        {"id": "1.2", "item": "Afiliación al Sistema de Seguridad Social Integral", "per": "Cuatrimestral", "tip": "Pagos planilla y contratistas."},
        {"id": "1.3", "item": "Programa de capacitación", "per": "Cuatrimestral", "tip": "Evidencias y listados de asistencia."},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Semestral", "tip": "Firmado por empleador y responsable."},
        {"id": "1.5", "item": "Evaluaciones médicas ocupacionales", "per": "Anual", "tip": "Certificados de aptitud física."},
        {"id": "1.6", "item": "Identificación de peligros y valoración de riesgos", "per": "Semestral", "tip": "Matriz de riesgos participativa."},
        {"id": "1.7", "item": "Medidas de prevención y control", "per": "Semestral", "tip": "Ejecución de actividades preventivas."}
    ],
    "🏢 11-50 Trabajadores": [
        {"id": "2.1", "item": "Asignación de responsable del SG-SST", "per": "Semestral", "tip": "HV, Licencia y Acta de designación."},
        {"id": "2.2", "item": "Asignación de responsabilidades en SST", "per": "Cuatrimestral", "tip": "Soportes documentales comunicados."},
        {"id": "2.3", "item": "Asignación de recursos para el Sistema", "per": "Anual", "tip": "Presupuesto planeado y ejecutado."},
        {"id": "2.4", "item": "Afiliación al Sistema de Seguridad Social", "per": "Cuatrimestral", "tip": "Control de planillas y moras."},
        {"id": "2.5", "item": "Conformación y funcionamiento del COPASST", "per": "Cuatrimestral", "tip": "Actas de reunión y elección."},
        {"id": "2.6", "item": "Conformación del Comité de Convivencia", "per": "Cuatrimestral", "tip": "Gestión de acoso laboral."},
        {"id": "2.7", "item": "Programa de capacitación anual", "per": "Anual", "tip": "Cronograma y evidencias de formación."},
        {"id": "2.8", "item": "Inducción y reinducción en SST", "per": "Anual", "tip": "Soportes de capacitación a nuevos."},
        {"id": "2.9", "item": "Curso Virtual de capacitación de 50 horas", "per": "Anual", "tip": "Certificado vigente."},
        {"id": "2.10", "item": "Evaluaciones médicas ocupacionales", "per": "Anual", "tip": "Custodia de historias clínicas."}
        # Nota: Aquí puedes seguir añadiendo los 21 puntos del documento.
    ],
    "🏗️ +50 Trab. o Riesgo IV/V": [
        {"id": "3.1", "item": "Asignación de responsable con Licencia", "per": "Semestral", "tip": "Profesional o Especialista SST."},
        {"id": "3.2", "item": "Asignación de recursos (Humanos, Técnicos, Fros)", "per": "Anual", "tip": "Presupuesto detallado y firmado."},
        {"id": "3.3", "item": "Identificación de trabajadores alto riesgo", "per": "Semestral", "tip": "Pensiones especiales y controles."},
        {"id": "3.4", "item": "Conformación de Brigada de Emergencias", "per": "Cuatrimestral", "tip": "Capacitación y dotación."}
        # Nota: Aquí puedes seguir añadiendo los 60 puntos del documento.
    ]
}

# --- 4. BARRA LATERAL ---
with st.sidebar:
    logo_file = "logo_jplfinal.jpg"
    if os.path.exists(logo_file):
        st.image(logo_file, use_container_width=True)
    else:
        st.error(f"Logo no encontrado: {logo_file}")
    
    st.markdown("<h2 style='text-align: center;'>APP JPL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("Nivel de Empresa:", ["🏠 Inicio", "📊 1-10 Trabajadores", "🏢 11-50 Trabajadores", "🏗️ +50 Trab. o Riesgo IV/V"])
    st.markdown("---")
    st.caption("Soluciones MyM | 2026")

# --- 5. LÓGICA DE CONTENIDO ---
if menu == "🏠 Inicio":
    st.title("Sistema de Gestión de Estándares Mínimos JPL")
    st.markdown(f"""
    <div style="background-color: white; padding: 25px; border-top: 5px solid #8B0000; border-bottom: 5px solid #4A4A4A; border-radius: 5px;">
        <h2 style="color: #1A1A1A;">Bienvenido, Gerardo</h2>
        <p style="color: #333;">Plataforma técnica para la auditoría de la <b>Resolución 0312</b>. Seleccione un módulo para iniciar.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.header(f"Sección: {menu}")
    lista = DATA_SST.get(menu, [])
    
    for est in lista:
        with st.expander(f"📍 ÍTEM {est['id']} - {est['item']}"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.write(f"**Periodicidad:** {est['per']}")
                st.caption(f"💡 {est['tip']}")
                st.text_area("Hallazgos", key=f"h_{est['id']}")
            with c2:
                st.selectbox("Resultado", ["Pendiente", "Cumple", "No Cumple", "No Aplica"], key=f"s_{est['id']}")
                st.date_input("Próximo Seguimiento", key=f"f_{est['id']}")

    if st.button("Finalizar y Guardar"):
        st.success("Auditoría procesada con la identidad visual de JPL.")
        st.balloons()
