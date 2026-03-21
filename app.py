import streamlit as st
import time
import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN Y ESTILO "APP MÓVIL JPL" ---
st.set_page_config(page_title="Grupo JPL SST", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');

    /* Fuente Global Chilanka */
    html, body, [class*="st-"], h1, h2, h3, p, label, .stSelectbox, .stRadio {
        font-family: 'Chilanka', cursive !important;
    }

    /* Fondo de la App Gris Muy Claro */
    .stApp { background-color: #F2F2F2; }

    /* Logo Transparente con animación */
    .logo-splash {
        display: block;
        margin: auto;
        width: 280px;
        opacity: 0.8;
        animation: fadeIn 2.5s;
    }
    @keyframes fadeIn { from {opacity: 0;} to {opacity: 0.8;} }

    /* Barra Superior Vinotinto */
    .top-bar-jpl {
        background-color: #800000; /* Vinotinto */
        padding: 20px;
        border-radius: 0 0 30px 30px;
        color: white;
        text-align: center;
        margin: -65px -20px 25px -20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }

    /* Tarjetas Blancas (Procesos I, II, III) */
    .card-proceso {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 10px solid #800000; /* Borde Vinotinto */
        color: #333;
    }

    /* Casilla Gris Ratón (Amenazas IV) */
    .box-amenazas-jpl {
        background-color: #BEBEBE; /* Gris Ratón */
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #800000;
        margin-bottom: 20px;
        color: black;
    }

    /* Botones Negros con texto Blanco */
    .stButton>button {
        border-radius: 15px;
        background-color: #000000;
        color: white !important;
        border: 1px solid #800000;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #800000;
        border: 1px solid #000000;
    }

    /* Barra de navegación inferior */
    .nav-bar-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #FFFFFF;
        padding: 12px;
        display: flex;
        justify-content: space-around;
        border-top: 2px solid #800000;
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. LÓGICA DE NAVEGACIÓN ---
if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'splash'

# --- 3. PANTALLA 1: SPLASH SCREEN (LOGO TRANSPARENTE) ---
if st.session_state.pantalla == 'splash':
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown('<img src="https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg" class="logo-splash">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#800000;'>Cargando Sistema JPL...</h2>", unsafe_allow_html=True)
    time.sleep(3) 
    st.session_state.pantalla = 'inicio'
    st.rerun()

# --- 4. PANTALLA 2: HOME (ESTILO APP) ---
elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h2>GRUPO JPL</h2><p>Gestión SST Integral</p></div>', unsafe_allow_html=True)
    
    # Tarjeta de Resumen
    st.markdown(f"""
    <div class="card-proceso">
        <p style='color:grey; margin-bottom:0;'>ESTADO DE CUMPLIMIENTO</p>
        <h2 style='margin-top:0; color:#800000;'>65% GLOBAL</h2>
        <div style='background-color:#e0e0e0; border-radius:10px; height:10px; width:100%;'>
            <div style='background-color:#800000; height:10px; width:65%; border-radius:10px;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ACCESOS RÁPIDOS")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🛡️ AUDITORÍA"):
            st.session_state.pantalla = 'auditoria'
            st.rerun()
    with c2:
        if st.button("💰 PLANES"):
            st.session_state.pantalla = 'licencias'
            st.rerun()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

# --- 5. PANTALLA 3: AUDITORÍA 60 ÍTEMS ---
elif st.session_state.pantalla == 'auditoria':
    st.markdown('<div class="top-bar-jpl"><h3>AUDITORÍA 0312</h3></div>', unsafe_allow_html=True)
    if st.button("⬅️ VOLVER AL INICIO"):
        st.session_state.pantalla = 'inicio'
        st.rerun()

    # BLOQUE I, II, III (Tarjeta Blanca/Vinotinto)
    st.markdown('<div class="card-proceso">', unsafe_allow_html=True)
    st.subheader("I, II y III: PROCESOS BASE")
    st.selectbox("1.1.1 Asignación de Responsable", ["Cumple", "No Cumple", "N/A"])
    st.selectbox("2.2.1 Evaluaciones Médicas", ["Cumple", "No Cumple", "N/A"])
    st.selectbox("3.1.1 Matriz de Peligros", ["Cumple", "No Cumple", "N/A"])
    st.markdown('</div>', unsafe_allow_html=True)

    # BLOQUE IV: AMENAZAS (Tarjeta Gris Ratón)
    st.markdown('<div class="box-amenazas-jpl">', unsafe_allow_html=True)
    st.subheader("IV. AMENAZAS (Ítems 43-47)")
    st.radio("43. Plan de Emergencias", ["Cumple", "No Cumple"], horizontal=True)
    st.radio("44. Brigadas de Respuesta", ["Cumple", "No Cumple"], horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("💾 GUARDAR AVANCE"):
        st.success("Información almacenada.")

# --- 6. PANTALLA 4: LICENCIAS ---
elif st.session_state.pantalla == 'licencias':
    st.markdown('<div class="top-bar-jpl"><h3>NUESTROS PLANES</h3></div>', unsafe_allow_html=True)
    if st.button("⬅️ VOLVER"):
        st.session_state.pantalla = 'inicio'
        st.rerun()
    
    st.markdown('<div class="card-proceso" style="text-align:center;"><h3>PLAN EMPRESA</h3><h2>$60.000</h2><p>Hasta 50 empleados</p></div>', unsafe_allow_html=True)
    if st.button("ADQUIRIR POR WHATSAPP"):
        st.info("Conectando con asesor...")

# --- BARRA DE NAVEGACIÓN FIJA ---
st.markdown(f"""
<div class="nav-bar-footer">
    <div style="text-align:center; color:#800000; font-size:12px;"><b>🏠<br>INICIO</b></div>
    <div style="text-align:center; color:#A9A9A9; font-size:12px;"><b>🛡️<br>SST</b></div>
    <div style="text-align:center; color:#A9A9A9; font-size:12px;"><b>📊<br>REPORTES</b></div>
    <div style="text-align:center; color:#A9A9A9; font-size:12px;"><b>⚙️<br>AJUSTES</b></div>
</div>
""", unsafe_allow_html=True)
