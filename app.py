import streamlit as st
import time

# --- 1. CONFIGURACIÓN Y BASE DE DATOS ---
st.set_page_config(page_title="APP JPL | SG-SST", layout="centered", initial_sidebar_state="expanded")

# Clientes con permiso de edición (Asociados/Premium)
usuarios_activos = {
    "gerardo@mym.com": "1234",
    "cliente@premium.com": "jpl2026"
}

# --- 2. ESTILOS VISUALES (Vinotinto, Gris y Marca de Agua) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat; background-attachment: fixed; background-position: center; background-size: 50%;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.96); z-index: -1;
    }

    .top-bar-jpl { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin: -65px -20px 25px -20px; }
    .card-proceso { background-color: rgba(255, 255, 255, 0.95); padding: 15px; border-radius: 20px; border-left: 10px solid #800000; margin-bottom: 15px; }
    .info-requisito { background-color: #e8e8e8; padding: 10px; border-radius: 10px; border: 1px solid #800000; font-size: 0.9em; margin-bottom: 20px; }
    .stButton>button { background-color: #000000 !important; color: white !important; border-radius: 12px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 3. CONTROL DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'splash'
if 'premium' not in st.session_state: st.session_state.premium = False

# --- 4. BARRA LATERAL (LOGIN) ---
with st.sidebar:
    st.markdown("### 🔐 ACCESO ASOCIADOS")
    if not st.session_state.premium:
        u = st.text_input("Correo")
        p = st.text_input("Clave", type="password")
        if st.button("INGRESAR"):
            if u in usuarios_activos and usuarios_activos[u] == p:
                st.session_state.premium = True
                st.rerun()
            else: st.error("Acceso denegado")
    else:
        st.success("✅ Modo Edición Activo")
        if st.button("Cerrar Sesión"):
            st.session_state.premium = False
            st.rerun()

# --- 5. LÓGICA DE PANTALLAS ---

if st.session_state.pantalla == 'splash':
    st.markdown('<div style="text-align:center; margin-top:150px;">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=250)
    st.markdown("<h1 style='color:#800000; font-size:60px;'>APP JPL</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.pantalla = 'inicio'
    st.rerun()

elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h1>APP JPL</h1></div>', unsafe_allow_html=True)
    st.markdown("### Seleccione su categoría (Res. 0312):")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Microempresas\n(< 10 emp / Riesgo I-III)"):
            st.session_state.nivel = "7"; st.session_state.pantalla = 'evaluacion'; st.rerun()
    with col2:
        if st.button("Pymes\n(11-50 emp / Riesgo I-III)"):
            st.session_state.nivel = "21"; st.session_state.pantalla = 'evaluacion'; st.rerun()
    with col3:
        if st.button("Grandes / Riesgo IV-V\n(62 Estándares)"):
            st.session_state.nivel = "62"; st.session_state.pantalla = 'evaluacion'; st.rerun()

elif st.session_state.pantalla == 'evaluacion':
    st.markdown(f'<div class="top-bar-jpl"><h3>EVALUACIÓN: {st.session_state.nivel} ESTÁNDARES</h3></div>', unsafe_allow_html=True)
    
    # Mostrar requisitos de personal según la ley
    if st.session_state.nivel == "7":
        st.markdown('<div class="info-requisito"><b>Requisito:</b> Técnico en SST con licencia y 1 año de experiencia.</div>', unsafe_allow_html=True)
    elif st.session_state.nivel == "21":
        st.markdown('<div class="info-requisito"><b>Requisito:</b> Tecnólogo en SST con licencia y 2 años de experiencia.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="info-requisito"><b>Requisito:</b> Profesional o Especialista con licencia vigente.</div>', unsafe_allow_html=True)

    if not st.session_state.premium:
        st.warning("⚠️ MODO LECTURA: Para calificar estos ítems debe ser Cliente Asociado.")

    def mostrar_item(cod, desc):
        st.markdown(f'<div class="card-proceso"><b>{cod}</b> - {desc}</div>', unsafe_allow_html=True)
        return st.selectbox("Estado:", ["Pendiente", "Cumple", "No Cumple", "N/A"], key=cod, disabled=not st.session_state.premium)

    # --- DESPLIEGUE DE ÍTEMS SEGÚN EL BOTÓN PRESIONADO ---
    if st.session_state.nivel == "7":
        mostrar_item("1.1.1", "Responsable del Sistema de Gestión de SST")
        mostrar_item("1.1.3", "Asignación de recursos para el SG-SST")
        mostrar_item("1.2.1", "Afiliación al Sistema de Seguridad Social Integral")
        mostrar_item("2.1.1", "Capacitación en SST")
        mostrar_item("3.1.1", "Plan Anual de Trabajo")
        mostrar_item("4.1.1", "Evaluaciones médicas ocupacionales")
        mostrar_item("6.1.1", "Identificación de peligros y valoración de riesgos")

    elif st.session_state.nivel == "21":
        st.info("Mostrando 21 estándares para Pymes...")
        mostrar_item("1.1.1", "Asignación de responsable")
        mostrar_item("1.1.3", "Recursos financieros y técnicos")
        # Aquí se completarían los 21 conforme a la resolución

    elif st.session_state.nivel == "62":
        st.info("Mostrando 62 estándares (Riesgo IV/V o > 50 emp)...")
        mostrar_item("1.1.1", "Responsable del SG-SST")
        mostrar_item("4.2.1", "Plan de Emergencias y Contingencias")
        # Aquí se completarían los 62 conforme a la resolución

    if st.button("⬅️ VOLVER AL INICIO"):
        st.session_state.pantalla = 'inicio'; st.rerun()
