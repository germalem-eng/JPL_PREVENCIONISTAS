import streamlit as st
import time

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Grupo JPL SST", layout="centered")

# --- 2. ESTILOS CSS AVANZADOS (COLORES JPL + FONDO TRANSPARENTE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    
    /* Fuente Global */
    html, body, [class*="st-"], h1, h2, h3, p, label { 
        font-family: 'Chilanka', cursive !important; 
    }

    /* FONDO DE PANTALLA CON LOGO TRANSPARENTE (MARCA DE AGUA) */
    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        background-size: 60%; /* Tamaño del logo de fondo */
        opacity: 1;
    }
    
    /* Capa de transparencia para el fondo */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.93); /* Ajusta el 0.93 para más o menos transparencia del fondo */
        z-index: -1;
    }

    /* Pantalla de Carga (Splash) */
    .splash-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
    }

    /* Estilos de Tarjetas y Bloques */
    .top-bar-jpl { 
        background-color: #800000; 
        padding: 20px; 
        border-radius: 0 0 30px 30px; 
        color: white; 
        text-align: center; 
        margin: -65px -20px 25px -20px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }

    .card-proceso { 
        background-color: rgba(255, 255, 255, 0.9); /* Blanco semi-transparente */
        padding: 15px; 
        border-radius: 20px; 
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1); 
        margin-bottom: 15px; 
        border-left: 10px solid #800000; 
    }

    .box-amenazas-jpl { 
        background-color: rgba(190, 190, 190, 0.9); /* Gris Ratón semi-transparente */
        padding: 15px; 
        border-radius: 20px; 
        border: 2px solid #800000; 
        margin-bottom: 15px; 
        color: black; 
    }

    /* Botones Negros */
    .stButton>button {
        background-color: #000000 !important;
        color: white !important;
        border-radius: 12px;
        border: 1px solid #800000;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE NAVEGACIÓN ---
if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'splash'

# --- 4. PANTALLA 1: SPLASH SCREEN LIMPIO ---
if st.session_state.pantalla == 'splash':
    container = st.empty() # Espacio temporal para limpiar la pantalla
    with container.container():
        st.markdown('<div class="splash-container">', unsafe_allow_html=True)
        st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=300)
        st.markdown("<h2 style='color:#800000;'>GRUPO JPL</h2>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    time.sleep(3) # Espera 3 segundos
    st.session_state.pantalla = 'inicio'
    st.rerun()

# --- 5. PANTALLA 2: INICIO (PANTALLAZO DE LA APP) ---
elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h2>SST - GRUPO JPL</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-proceso"><h3>Bienvenido</h3><p>Gestión de Resolución 0312 de 2019</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🛡️ AUDITORÍA"):
            st.session_state.pantalla = 'sst'
            st.rerun()
    with col2:
        if st.button("💰 PLANES"):
            st.session_state.pantalla = 'licencias'
            st.rerun()

# --- 6. PANTALLA 3: SST (60 ÍTEMS) ---
elif st.session_state.pantalla == 'sst':
    st.markdown('<div class="top-bar-jpl"><h3>ESTÁNDARES MÍNIMOS</h3></div>', unsafe_allow_html=True)
    
    # Bloque de Procesos I, II, III
    st.markdown('<div class="card-proceso"><h4>I, II, III: RECURSOS Y RIESGOS</h4>', unsafe_allow_html=True)
    st.selectbox("1.1.1 Responsable asignado", ["Cumple", "No Cumple", "N/A"])
    st.selectbox("3.1.1 Matriz de Peligros", ["Cumple", "No Cumple", "N/A"])
    st.markdown('</div>', unsafe_allow_html=True)

    # Bloque Especial Gris Ratón - Amenazas
    st.markdown('<div class="box-amenazas-jpl"><h4>IV. AMENAZAS (Ítems 43-47)</h4>', unsafe_allow_html=True)
    st.radio("43. Plan de Emergencias", ["Cumple", "No Cumple"], horizontal=True)
    st.radio("46. Simulacros", ["Cumple", "No Cumple"], horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("⬅️ VOLVER"):
        st.session_state.pantalla = 'inicio'
        st.rerun()

# --- 7. PANTALLA 4: LICENCIAS (3 PLANES) ---
elif st.session_state.pantalla == 'licencias':
    st.markdown('<div class="top-bar-jpl"><h3>NUESTROS PLANES</h3></div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card-proceso"><b>PEQUEÑA</b><br>$40.000</div>', unsafe_allow_html=True)
        st.button("Pedir 40k", key="p1")
    with c2:
        st.markdown('<div class="card-proceso"><b>MEDIANA</b><br>$60.000</div>', unsafe_allow_html=True)
        st.button("Pedir 60k", key="p2")
    with c3:
        st.markdown('<div class="card-proceso"><b>GRANDE</b><br>$100.000</div>', unsafe_allow_html=True)
        st.button("Pedir 100k", key="p3")
        
    if st.button("⬅️ VOLVER"):
        st.session_state.pantalla = 'inicio'
        st.rerun()

# --- BARRA DE NAVEGACIÓN INFERIOR (ESTILO WOM) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
fixed_nav = st.container()
with fixed_nav:
    nav_cols = st.columns(3)
    with nav_cols[0]:
        if st.button("🏠 INICIO"): 
            st.session_state.pantalla = 'inicio'
            st.rerun()
    with nav_cols[1]:
        if st.button("🛡️ SST"): 
            st.session_state.pantalla = 'sst'
            st.rerun()
    with nav_cols[2]:
        if st.button("📊 REPORTES"): 
            st.info("Próximamente")
