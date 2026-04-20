import streamlit as st
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. ESTILO INSTITUCIONAL (Gris Oxford, Negro y Vinotinto) ---
st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } /* Gris Fondo */
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #000000 !important; font-family: 'Arial Black', sans-serif; }
    .stExpander { background-color: white !important; border: 1px solid #1A1A1A !important; border-radius: 0px; margin-bottom: 10px; }
    .stButton>button { background-color: #000000 !important; color: white !important; font-weight: bold; width: 100%; border-radius: 0px; }
    .stButton>button:hover { background-color: #4A4A4A !important; border: 1px solid #8B0000; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 15px; margin-bottom: 15px; font-style: italic; color: #1A1A1A; border-radius: 4px; }
    label { color: #000000 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS MAESTRA (Resolución 0312) ---
DATA_SST = {
    "📊 1-10 Trabajadores": [
        {"id": "1.1", "item": "Asignación de persona que diseña el SG-SST", "per": "Semestral", "quote": "📌 Contar con una persona competente no es solo un requisito, es quien garantiza que el SG-SST funcione correctamente."},
        {"id": "1.2", "item": "Afiliación al Sistema de Seguridad Social Integral", "per": "Cuatrimestral", "quote": "📌 Una afiliación adecuada protege al trabajador y evita sanciones económicas para la empresa."},
        {"id": "1.3", "item": "Programa de capacitación", "per": "Cuatrimestral", "quote": "📌 Una empresa que capacita, previene errores humanos y fortalece su cultura preventiva."},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Semestral", "quote": "📌 El plan de trabajo es la hoja de ruta para alcanzar los objetivos de seguridad del año."},
        {"id": "1.5", "item": "Evaluaciones médicas ocupacionales", "per": "Anual", "quote": "📌 Conocer el estado de salud de los trabajadores permite asignar tareas seguras y productivas."},
        {"id": "1.6", "item": "Identificación de peligros y valoración de riesgos", "per": "Semestral", "quote": "📌 Identificar riesgos a tiempo es la única forma de evitar que se conviertan en accidentes."},
        {"id": "1.7", "item": "Medidas de prevención y control", "per": "Semestral", "quote": "📌 La prevención es la mejor inversión que una empresa puede hacer por su gente."}
    ],
    "🏢 11-50 Trabajadores": [
        {"id": "2.1", "item": "Asignación de responsable del SG-SST", "per": "Semestral", "quote": "📌 El liderazgo en SST asegura la continuidad y mejora del sistema."},
        {"id": "2.2", "item": "Asignación de responsabilidades en SST", "per": "Cuatrimestral", "quote": "📌 Definir responsabilidades claras permite una gestión organizada y efectiva."},
        {"id": "2.3", "item": "Asignación de recursos para el Sistema", "per": "Anual", "quote": "📌 El presupuesto es el respaldo real del compromiso de la gerencia con la salud."},
        {"id": "2.4", "item": "Afiliación al Sistema de Seguridad Social", "per": "Cuatrimestral", "quote": "📌 Cumplir con la seguridad social es el primer paso de una empresa responsable."},
        {"id": "2.5", "item": "Conformación y funcionamiento del COPASST", "per": "Cuatrimestral", "quote": "📌 El COPASST es el puente de comunicación entre trabajadores y empleador."},
        {"id": "2.6", "item": "Conformación del Comité de Convivencia", "per": "Cuatrimestral", "quote": "📌 Un ambiente laboral sano previene el acoso y mejora la productividad."},
        {"id": "2.7", "item": "Programa de capacitación anual", "per": "Anual", "quote": "📌 La formación continua actualiza las defensas de la empresa ante los riesgos."},
        {"id": "2.8", "item": "Inducción y reinducción en SST", "per": "Anual", "quote": "📌 Todo trabajador nuevo debe conocer sus riesgos desde el primer minuto."},
        {"id": "2.9", "item": "Curso Virtual de 50 horas", "per": "Anual", "quote": "📌 El conocimiento normativo es la base legal de nuestra operación."},
        {"id": "2.10", "item": "Evaluaciones médicas ocupacionales", "per": "Anual", "quote": "📌 El seguimiento médico previene enfermedades laborales a largo plazo."},
        {"id": "2.11", "item": "Entrega de EPP y capacitación", "per": "Cuatrimestral", "quote": "📌 El EPP es la última barrera, pero debe usarse correctamente."},
        {"id": "2.12", "item": "Identificación de peligros y valoración de riesgos", "per": "Semestral", "quote": "📌 Una matriz viva es la mejor herramienta del prevencionista."},
        {"id": "2.13", "item": "Reporte de accidentes y enfermedades", "per": "Mensual", "quote": "📌 Reportar a tiempo permite aprender de los errores y no repetirlos."},
        {"id": "2.14", "item": "Investigación de incidentes y accidentes", "per": "Mensual", "quote": "📌 Investigar la causa raíz evita que el accidente vuelva a ocurrir."},
        {"id": "2.15", "item": "Conformación de Brigada de Emergencias", "per": "Anual", "quote": "📌 Estar preparados es la diferencia entre un susto y una tragedia."},
        {"id": "2.16", "item": "Plan de Prevención ante Emergencias", "per": "Anual", "quote": "📌 Saber qué hacer ante el fuego o el sismo salva vidas."},
        {"id": "2.17", "item": "Revisión por la alta dirección", "per": "Anual", "quote": "📌 El compromiso gerencial se demuestra en la revisión de resultados."},
        {"id": "2.18", "item": "Adquisiciones y contratación", "per": "Cuatrimestral", "quote": "📌 Comprar seguro y contratar seguro es gestionar el riesgo externo."},
        {"id": "2.19", "item": "Mantenimiento periódico de equipos", "per": "Cuatrimestral", "quote": "📌 Una máquina bien mantenida no causa accidentes."},
        {"id": "2.20", "item": "Sistemas de vigilancia epidemiológica", "per": "Anual", "quote": "📌 Vigilar la salud colectiva permite tomar medidas preventivas globales."},
        {"id": "2.21", "item": "Estadísticas de accidentalidad", "per": "Mensual", "quote": "📌 Lo que no se mide no se controla, lo que no se controla no mejora."}
    ],
    "🏗️ +50 / Riesgo IV-V": [
        {"id": "3.1", "item": "Asignación de responsable con Licencia (Especialista)", "per": "Semestral", "quote": "📌 En alto riesgo, la experticia profesional es innegociable."},
        {"id": "3.2", "item": "Matriz legal actualizada", "per": "Anual", "quote": "📌 El cumplimiento legal es el escudo de la organización."}
        # Se añadirán los 60 ítems progresivamente para no saturar la carga inicial
    ]
}

# --- 4. BARRA LATERAL ---
with st.sidebar:
    logo = "logo_jplfinal.jpg"
    if os.path.exists(logo):
        st.image(logo, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; font-size: 32px;'>APP JPL</h1>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("Menú Principal:", ["🏠 Inicio", "📊 1-10 Trabajadores", "🏢 11-50 Trabajadores", "🏗️ +50 / Riesgo IV-V", "💎 Contenido Premium"])
    st.markdown("---")
    st.caption("Soluciones MyM | L.I.N.A. Engine")

# --- 5. LÓGICA DE AUDITORÍA ---
if menu == "🏠 Inicio":
    st.title("Gestión de Estándares Mínimos JPL")
    st.markdown(f"""
    <div style="background-color: white; padding: 30px; border-left: 15px solid #000000; border-right: 15px solid #8B0000;">
        <h2 style="color: #000;">Bienvenido a APP JPL</h2>
        <p style="color: #4A4A4A; font-size: 19px;">Plataforma de auditoría técnica bajo la <b>Resolución 0312 de 2019</b>.</p>
        <p style="color: #666;">Seleccione un módulo lateral para iniciar el diagnóstico y visualizar estadísticas de cumplimiento.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca Premium JPL")
    st.info("Espacio exclusivo para clientes: Infografías, Videos y Alertas.")
    st.write("- [Video] Inducción SST 2026")
    st.write("- [Infografía] Alertas Contables en SST")

else:
    st.header(f"Sección: {menu}")
    items = DATA_SST.get(menu, [])
    
    cumple = 0
    total = len(items)

    for st_item in items:
        with st.expander(f"⬛ ÍTEM {st_item['id']} - {st_item['item']}"):
            st.markdown(f"<div class='quote-box'>{st_item['quote']}</div>", unsafe_allow_html=True)
            c1, c2 = st.columns([2, 1])
            with c1:
                st.write(f"**Periodicidad:** {st_item['per']}")
                st.text_area("Hallazgos", key=f"h_{st_item['id']}_{menu}")
            with c2:
                res = st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple", "No Aplica"], key=f"s_{st_item['id']}_{menu}")
                if res == "Cumple": cumple += 1
                st.date_input("Seguimiento", key=f"f_{st_item['id']}_{menu}")

    # --- ESTADÍSTICA DE CUMPLIMIENTO ---
    if total > 0:
        porcentaje = (cumple / total) * 100
        st.sidebar.markdown("---")
        st.sidebar.metric("Cumplimiento Actual", f"{round(porcentaje, 1)}%")
        
    if st.button("🔴 FINALIZAR REPORTE"):
        st.success(f"Reporte de {menu} guardado con {round(porcentaje, 1)}% de cumplimiento.")
        st.balloons()
