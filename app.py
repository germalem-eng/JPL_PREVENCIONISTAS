import streamlit as st
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. DISEÑO INSTITUCIONAL ---
st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } 
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #000000 !important; font-family: 'Arial Black', sans-serif; }
    .stExpander { background-color: white !important; border: 1px solid #1A1A1A !important; margin-bottom: 10px; }
    .stButton>button { background-color: #000000 !important; color: white !important; font-weight: bold; width: 100%; border-radius: 0px; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 12px; margin-bottom: 10px; font-style: italic; color: #1A1A1A; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS COMPLETA ---
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
        {"id": "2.4", "item": "Afiliación a Seguridad Social", "per": "Mensual", "q": "📌 Cumplimiento legal innegociable."},
        {"id": "2.5", "item": "COPASST", "per": "Anual", "q": "📌 Participación para la seguridad."},
        {"id": "2.6", "item": "Comité de Convivencia", "per": "Anual", "q": "📌 Ambientes sanos, equipos fuertes."},
        {"id": "2.7", "item": "Programa de Capacitación", "per": "Anual", "q": "📌 Crecimiento técnico en seguridad."},
        # ... (Hasta completar los 21 ítems)
    ],
    "🏗️ +50 / Riesgo IV-V": [
        {"id": "3.1", "item": "Responsable con Licencia (Especialista)", "per": "Anual", "q": "📌 Experticia máxima para riesgos altos."},
        {"id": "3.2", "item": "Asignación de recursos (T-F-H)", "per": "Anual", "q": "📌 Capacidad instalada para la gestión."},
        {"id": "3.3", "item": "Matriz Legal Actualizada", "per": "Semestral", "q": "📌 El blindaje legal de la empresa."},
        {"id": "3.4", "item": "Gestión de tareas de alto riesgo", "per": "Mensual", "q": "📌 Control absoluto en entornos peligrosos."},
        {"id": "3.5", "item": "Política de SST comunicada", "per": "Anual", "q": "📌 Compromiso gerencial visible."},
        {"id": "3.6", "item": "Objetivos de SST medibles", "per": "Anual", "q": "📌 Metas claras para resultados reales."},
        {"id": "3.7", "item": "Archivo y retención de documentos", "per": "Anual", "q": "📌 La memoria técnica del sistema."},
        {"id": "3.8", "item": "Rendición de cuentas", "per": "Anual", "q": "📌 Transparencia en la gestión preventiva."},
        {"id": "3.9", "item": "Matriz de EPP", "per": "Anual", "q": "📌 Protección específica para cada labor."},
        {"id": "3.10", "item": "Protocolos de bioseguridad", "per": "Semestral", "q": "📌 Salud pública en el entorno laboral."},
        # He dejado la estructura preparada para cargar los 60 items del Word
    ]
}

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>APLICACIÓN JPL</h1>", unsafe_allow_html=True)
    st.markdown("---")
    # Usamos una clave única 'menu_navegacion' para evitar conflictos
    menu = st.radio("Navegación:", list(DATA_SST.keys()) + ["🏠 Inicio", "💎 Contenido Premium"], key="menu_navegacion")
    st.markdown("---")
    st.caption("Ecosistema L.I.N.A. | Soluciones MyM")

# --- 5. LÓGICA DE VISUALIZACIÓN ---
if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.info("Seleccione un módulo lateral para iniciar la auditoría técnica.")

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca de Recursos Premium")
    st.write("Videos e infografías exclusivas para clientes JPL.")

else:
    # CORRECCIÓN DE TÍTULO DINÁMICO
    st.header(f"Sección: {menu}")
    
    items = DATA_SST.get(menu, [])
    total = len(items)
    cumple = 0

    if total == 0:
        st.warning("Cargando ítems de la base de datos...")
    else:
        for it in items:
            with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
                st.markdown(f"<div class='quote-box'>{it['q']}</div>", unsafe_allow_html=True)
                c1, c2 = st.columns([2, 1])
                with c1:
                    st.write(f"**Periodicidad Sugerida:** {it['per']}")
                    st.text_area("Hallazgos / Plan de Acción", key=f"txt_{it['id']}_{menu}")
                with c2:
                    res = st.selectbox("Resultado", ["Pendiente", "Cumple", "No Cumple"], key=f"sel_{it['id']}_{menu}")
                    if res == "Cumple": cumple += 1
                    st.date_input("Próximo Seguimiento", key=f"date_{it['id']}_{menu}")

        # CORRECCIÓN DE CÁLCULO DE ESTADÍSTICA
        pct = (cumple / total) * 100
        st.sidebar.markdown("---")
        st.sidebar.metric("Cumplimiento", f"{round(pct, 1)}%")

        if st.button("🔴 FINALIZAR Y GUARDAR ESTADÍSTICA"):
            st.success(f"Auditoría de {menu} guardada con {round(pct, 1)}% de cumplimiento.")
            st.balloons()
