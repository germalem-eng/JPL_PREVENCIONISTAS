import streamlit as st
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. DISEÑO INSTITUCIONAL (Gris, Negro, Vinotinto) ---
st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } 
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #000000 !important; font-family: 'Arial Black', sans-serif; }
    .stExpander { background-color: white !important; border: 1px solid #1A1A1A !important; margin-bottom: 10px; }
    .stButton>button { background-color: #000000 !important; color: white !important; font-weight: bold; border-radius: 0px; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 12px; margin-bottom: 10px; font-style: italic; color: #1A1A1A; }
    label { color: #000000 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS MAESTRA ---
# Aquí integramos los 60 items del tercer Word y los anteriores
DATA_SST = {
    "📊 1-10 Trabajadores": [
        {"id": "1.1", "item": "Asignación de persona que diseña el SG-SST", "per": "Semestral", "q": "📌 Contar con una persona competente garantiza que el sistema funcione."},
        {"id": "1.2", "item": "Afiliación al Sistema de Seguridad Social", "per": "Cuatrimestral", "q": "📌 Una afiliación adecuada protege al trabajador y evita sanciones."},
        {"id": "1.3", "item": "Programa de capacitación", "per": "Cuatrimestral", "q": "📌 Una empresa que capacita, previene errores humanos."},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Semestral", "q": "📌 El plan de trabajo es la hoja de ruta para alcanzar los objetivos."},
        {"id": "1.5", "item": "Evaluaciones médicas ocupacionales", "per": "Anual", "q": "📌 Conocer el estado de salud permite asignar tareas seguras."},
        {"id": "1.6", "item": "Identificación de peligros y riesgos", "per": "Semestral", "q": "📌 Identificar riesgos a tiempo evita accidentes."},
        {"id": "1.7", "item": "Medidas de prevención y control", "per": "Semestral", "q": "📌 La prevención es la mejor inversión por su gente."}
    ],
    "🏢 11-50 Trabajadores": [
        {"id": "2.1", "item": "Asignación de responsable del SG-SST", "per": "Semestral", "q": "📌 El liderazgo en SST asegura la continuidad."},
        {"id": "2.2", "item": "Asignación de responsabilidades", "per": "Cuatrimestral", "q": "📌 Definir responsabilidades permite una gestión organizada."},
        {"id": "2.3", "item": "Asignación de recursos", "per": "Anual", "q": "📌 El presupuesto es el respaldo real del compromiso."},
        {"id": "2.4", "item": "Afiliación a Seguridad Social", "per": "Cuatrimestral", "q": "📌 Cumplir es el primer paso de una empresa responsable."},
        {"id": "2.5", "item": "COPASST", "per": "Cuatrimestral", "q": "📌 El COPASST es el puente de comunicación laboral."},
        {"id": "2.6", "item": "Comité de Convivencia", "per": "Cuatrimestral", "q": "📌 Un ambiente sano previene el acoso."},
        {"id": "2.7", "item": "Programa de capacitación anual", "per": "Anual", "q": "📌 La formación actualiza las defensas ante riesgos."},
        {"id": "2.8", "item": "Inducción y reinducción", "per": "Anual", "q": "📌 Todo trabajador debe conocer sus riesgos desde el inicio."},
        {"id": "2.9", "item": "Curso Virtual de 50 horas", "per": "Anual", "q": "📌 El conocimiento normativo es la base legal."},
        {"id": "2.10", "item": "Evaluaciones médicas ocupacionales", "per": "Anual", "q": "📌 El seguimiento previene enfermedades a largo plazo."},
        {"id": "2.11", "item": "Entrega de EPP", "per": "Cuatrimestral", "q": "📌 El EPP es la última barrera, úselo bien."},
        {"id": "2.12", "item": "Matriz de Riesgos", "per": "Semestral", "q": "📌 Una matriz viva es la mejor herramienta."},
        {"id": "2.13", "item": "Reporte de ATEL", "per": "Mensual", "q": "📌 Reportar permite aprender y no repetir."},
        {"id": "2.14", "item": "Investigación de Accidentes", "per": "Mensual", "q": "📌 Investigar la causa raíz evita la repetición."},
        {"id": "2.15", "item": "Brigada de Emergencias", "per": "Anual", "q": "📌 Estar preparados salva vidas."},
        {"id": "2.16", "item": "Plan de Emergencias", "per": "Anual", "q": "📌 Saber qué hacer ante el fuego salva vidas."},
        {"id": "2.17", "item": "Revisión por la dirección", "per": "Anual", "q": "📌 El compromiso se demuestra en los resultados."},
        {"id": "2.18", "item": "Adquisiciones y contratación", "per": "Cuatrimestral", "q": "📌 Comprar seguro es gestionar el riesgo."},
        {"id": "2.19", "item": "Mantenimiento de equipos", "per": "Cuatrimestral", "q": "📌 Una máquina mantenida no falla."},
        {"id": "2.20", "item": "Vigilancia epidemiológica", "per": "Anual", "q": "📌 Vigilar la salud colectiva permite prevención."},
        {"id": "2.21", "item": "Estadísticas de accidentalidad", "per": "Mensual", "q": "📌 Lo que no se mide no se controla."}
    ],
    "🏗️ +50 / Riesgo IV-V": [
        # Aquí se cargan los 60 items del tercer Word
        {"id": "3.1", "item": "Responsable SG-SST (Profesional/Especialista)", "per": "Semestral", "q": "📌 En alto riesgo, la experticia es innegociable."},
        {"id": "3.2", "item": "Asignación de recursos (H, T, F)", "per": "Anual", "q": "📌 El respaldo financiero asegura la alta complejidad."},
        {"id": "3.3", "item": "Matriz legal", "per": "Anual", "q": "📌 El cumplimiento legal es el escudo organizacional."},
        {"id": "3.4", "item": "Gestión de tareas de alto riesgo", "per": "Mensual", "q": "📌 El control riguroso en alturas o confinados no tiene margen de error."},
        # ... (Agregar el resto de los 60 items del archivo Word 3)
    ]
}

# --- 4. BARRA LATERAL ---
with st.sidebar:
    if os.path.exists("logo_jplfinal.jpg"): st.image("logo_jplfinal.jpg", use_container_width=True)
    st.markdown("<h1 style='text-align: center;'>APP JPL</h1>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("Navegación:", ["🏠 Inicio", "📊 1-10 Trabajadores", "🏢 11-50 Trabajadores", "🏗️ +50 / Riesgo IV-V", "💎 Contenido Premium"])
    st.markdown("---")
    st.caption("Soluciones MyM | L.I.N.A. Engine")

# --- 5. LÓGICA DE AUDITORÍA ---
if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.markdown(f"""
    <div style="background-color: white; padding: 30px; border-left: 15px solid #000; border-right: 15px solid #8B0000;">
        <h3>Sistema de Gestión de Estándares Mínimos</h3>
        <p>Plataforma oficial para la auditoría de la Resolución 0312. Use el menú lateral para gestionar cada nivel de empresa.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca de Recursos")
    st.info("Infografías, Videos y Alertas para Clientes Premium.")
    st.write("📁 **Videos de Inducción**")
    st.write("📊 **Infografías para Contabilidad**")

else:
    st.header(f"Sección: {menu}")
    items = DATA_SST.get(menu, [])
    cumple = 0
    total
