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
    .stButton>button { background-color: #000000 !important; color: white !important; font-weight: bold; width: 100%; border-radius: 0px; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 12px; margin-bottom: 10px; font-style: italic; color: #1A1A1A; }
    label { color: #000000 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS MAESTRA ---
DATA_SST = {
    "📊 1-10 Trabajadores": [
        {"id": "1.1", "item": "Asignación de responsable", "per": "Semestral", "q": "📌 La competencia garantiza el éxito."},
        {"id": "1.2", "item": "Seguridad Social", "per": "Mensual", "q": "📌 Proteger al equipo es prioridad."},
        {"id": "1.3", "item": "Capacitación en SST", "per": "Anual", "q": "📌 El conocimiento previene accidentes."},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Anual", "q": "📌 Nuestra hoja de ruta preventiva."},
        {"id": "1.5", "item": "Evaluaciones Médicas", "per": "Anual", "q": "📌 Salud vigilada, empresa productiva."},
        {"id": "1.6", "item": "Identificación de Peligros", "per": "Anual", "q": "📌 Anticiparse al riesgo es clave."},
        {"id": "1.7", "item": "Medidas de Control", "per": "Semestral", "q": "📌 Ejecutar la prevención con rigor."}
    ],
    "🏢 11-50 Trabajadores": [
        {"id": "2.1", "item": "Responsable SG-SST", "per": "Anual", "q": "📌 Liderazgo para la mejora continua."},
        {"id": "2.2", "item": "Recursos Financieros", "per": "Anual", "q": "📌 El respaldo económico de la prevención."},
        {"id": "2.3", "item": "Plan de Trabajo Anual", "per": "Anual", "q": "📌 Orden en la ejecución preventiva."},
        {"id": "2.4", "item": "Seguridad Social", "per": "Mensual", "q": "📌 Cumplimiento legal innegociable."},
        {"id": "2.5", "item": "COPASST", "per": "Anual", "q": "📌 Participación para la seguridad."},
        {"id": "2.6", "item": "Comité de Convivencia", "per": "Anual", "q": "📌 Ambientes sanos, equipos fuertes."},
        {"id": "2.7", "item": "Programa de Capacitación", "per": "Anual", "q": "📌 Crecimiento técnico en seguridad."},
        {"id": "2.8", "item": "Inducción y Reinducción", "per": "Anual", "q": "📌 Preparación desde el primer día."},
        {"id": "2.9", "item": "Curso Virtual 50 Horas", "per": "Anual", "q": "📌 Base normativa sólida."},
        {"id": "2.10", "item": "Evaluaciones Médicas", "per": "Anual", "q": "📌 Seguimiento de salud constante."},
        {"id": "2.11", "item": "Entrega de EPP", "per": "Cuatrimestral", "q": "📌 Protección real para el trabajador."},
        {"id": "2.12", "item": "Matriz de Peligros", "per": "Anual", "q": "📌 Identificación técnica de riesgos."},
        {"id": "2.13", "item": "Reporte de Accidentes", "per": "Mensual", "q": "📌 Transparencia en la siniestralidad."},
        {"id": "2.14", "item": "Investigación de ATEL", "per": "Mensual", "q": "📌 Aprender del error para no repetir."},
        {"id": "2.15", "item": "Brigada de Emergencia", "per": "Anual", "q": "📌 Respuesta inmediata ante crisis."},
        {"id": "2.16", "item": "Plan de Emergencias", "per": "Anual", "q": "📌 Estructura ante lo inesperado."},
        {"id": "2.17", "item": "Revisión por la Dirección", "per": "Anual", "q": "📌 Compromiso desde el nivel más alto."},
        {"id": "2.18", "item": "Adquisiciones", "per": "Anual", "q": "📌 Compras seguras, procesos protegidos."},
        {"id": "2.19", "item": "Mantenimiento", "per": "Anual", "q": "📌 Equipos en óptimo estado."},
        {"id": "2.20", "item": "Sistemas de Vigilancia", "per": "Anual", "q": "📌 Control epidemiológico activo."},
        {"id": "2.21", "item": "Estadísticas de SST", "per": "Mensual", "q": "📌 Medir para mejorar."}
    ],
    "🏗️ +50 / Riesgo IV-V": [
        {"id": f"3.{i}", "item": f"Estándar Técnico Superior {i}", "per": "Variable", "q": "📌 Rigor máximo para alta complejidad."} 
        for i in range(1, 61)
    ]
}

# --- 4. BARRA LATERAL (INICIO AL PRINCIPIO) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 24px;'>APLICACIÓN JPL</h1>", unsafe_allow_html=True)
    st.markdown("---")
    # Se define Inicio primero en la lista de opciones
    opciones = ["🏠 Inicio", "📊 1-10 Trabajadores", "🏢 11-50 Trabajadores", "🏗️ +50 / Riesgo IV-V", "💎 Contenido Premium"]
    menu = st.radio("Navegación:", opciones)
    st.markdown("---")
    st.caption("Soluciones MyM | Ecosistema L.I.N.A.")

# --- 5. LÓGICA DE CONTENIDO ---
if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.info("Seleccione un nivel de empresa en el menú lateral para realizar la evaluación.")

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca Premium")
    st.write("Contenido exclusivo para clientes de JPL Prevencionistas.")

else:
    # EL TÍTULO AHORA SE SINCRONIZA CORRECTAMENTE
    st.header(f"Sección Seleccionada: {menu}")
    
    items = DATA_SST.get(menu, [])
    total = len(items)
    cumple = 0

    if total > 0:
        for it in items:
            with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
                st.markdown(f"<div class='quote-box'>{it['q']}</div>", unsafe_allow_html=True)
                c1, c2 = st.columns([2, 1])
                with c1:
                    st.write(f"**Periodicidad:** {it['per']}")
                    st.text_area("Evidencias / Plan de Acción", key=f"t_{it['id']}_{menu}")
                with c2:
                    res = st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple"], key=f"s_{it['id']}_{menu}")
                    if res == "Cumple": cumple += 1
                    st.date_input("Seguimiento", key=f"d_{it['id']}_{menu}")

        # Estadística dinámica
        pct = (cumple / total) * 100
        st.sidebar.markdown("---")
        st.sidebar.metric("Cumplimiento", f"{round(pct, 1)}%")

        if st.button("🔴 FINALIZAR EVALUACIÓN"):
            st.success(f"Resultados de {menu} guardados.")
            st.balloons()
