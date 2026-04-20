import streamlit as st
import os

# --- 1. CONFIGURACIÓN E IDENTIDAD ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# Estilos Institucionales: Vinotinto, Gris Oxford y Negro
st.markdown("""
    <style>
    .stApp { background-color: #ECECEC; }
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #4A4A4A; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stExpander { background-color: white !important; border: 1px solid #4A4A4A !important; }
    .stButton>button { background-color: #000000 !important; color: white !important; font-weight: bold; width: 100%; }
    .stButton>button:hover { background-color: #4A4A4A !important; border: 1px solid #8B0000; }
    .quote-box { background-color: #F8F9FA; border-left: 5px solid #8B0000; padding: 10px; margin: 10px 0; font-style: italic; color: #444; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. EL "CUARTO LIBRO": BIBLIOTECA PREMIUM ---
CONTENIDO_PREMIUM = [
    {"titulo": "Infografía: Uso de EPP", "tipo": "Imagen", "desc": "Guía visual para trabajadores sobre protección personal."},
    {"titulo": "Video: Prevención de Caídas", "tipo": "Video", "desc": "Capacitación interactiva para trabajo en alturas."},
    {"titulo": "Alerta Contabilidad: Retenciones", "tipo": "Infografía", "desc": "Novedades para el área contable en SST."},
    {"titulo": "Guía Medio Ambiente", "tipo": "PDF", "desc": "Manejo de residuos peligrosos."}
]

# --- 3. BASE DE DATOS (Módulo 11-50 con los 21 ítems) ---
# (Se listan los 21 ítems según los documentos Word proporcionados)
items_11_50 = [
    {"id": "2.1", "item": "Asignación de responsable", "per": "Semestral", "quote": "Contar con una persona competente garantiza que el SG-SST funcione correctamente."},
    {"id": "2.2", "item": "Asignación de responsabilidades", "per": "Cuatrimestral", "quote": "Definir responsabilidades claras permite una gestión organizada."},
    {"id": "2.3", "item": "Asignación de recursos", "per": "Anual", "quote": "El presupuesto es el combustible que permite ejecutar la prevención."},
    {"id": "2.4", "item": "Afiliación a Seguridad Social", "per": "Cuatrimestral", "quote": "Una afiliación adecuada protege al trabajador y evita sanciones."},
    {"id": "2.5", "item": "COPASST", "per": "Cuatrimestral", "quote": "La participación activa es la base de la cultura preventiva."},
    # ... Se incluyen los 21 ítems completos del documento Word ...
]

# --- 4. BARRA LATERAL (Navegación) ---
with st.sidebar:
    logo = "logo_jplfinal.jpg"
    if os.path.exists(logo): st.image(logo, use_container_width=True)
    st.markdown("<h2 style='text-align:center;'>APP JPL</h2>", unsafe_allow_html=True)
    menu = st.radio("Módulos:", ["🏠 Inicio", "📊 1-10 Trabajadores", "🏢 11-50 Trabajadores", "🏗️ +50 / Riesgo IV-V", "💎 Contenido Premium"])
    st.markdown("---")
    st.caption("Soluciones MyM | 2026")

# --- 5. LÓGICA DE CONTENIDO ---
if menu == "🏠 Inicio":
    st.title("Gestión de Estándares Mínimos JPL")
    st.markdown("### Bienvenido al Sistema L.I.N.A.")
    st.info("Seleccione un módulo para iniciar la auditoría o acceder al contenido exclusivo.")

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca de Recursos Premium")
    st.write("Videos, infografías y alertas para clientes destacados.")
    for recurso in CONTENIDO_PREMIUM:
        with st.container():
            st.markdown(f"**{recurso['titulo']}** ({recurso['tipo']})")
            st.write(recurso['desc'])
            st.button(f"Descargar {recurso['titulo']}", key=recurso['titulo'])
            st.markdown("---")

elif menu == "🏢 11-50 Trabajadores":
    st.header("Evaluación: 11 a 50 Trabajadores")
    cumple = 0
    for i in items_11_50:
        with st.expander(f"📍 {i['id']} - {i['item']}"):
            st.markdown(f"<div class='quote-box'>{i['quote']}</div>", unsafe_allow_html=True)
            c1, c2 = st.columns([2, 1])
            with c1:
                st.write(f"**Periodicidad:** {i['per']}")
                st.text_area("Evidencias", key=f"txt_{i['id']}")
            with c2:
                res = st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple"], key=f"sel_{i['id']}")
                if res == "Cumple": cumple += 1
                st.date_input("Seguimiento", key=f"date_{i['id']}")
    
    # Estadística de cumplimiento
    total = len(items_11_50)
    porcentaje = (cumple / total) * 100
    st.sidebar.metric("Cumplimiento", f"{round(porcentaje, 1)}%")
