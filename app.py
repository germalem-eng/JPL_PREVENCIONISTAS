import streamlit as st
import time

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Grupo JPL SST", layout="centered", initial_sidebar_state="collapsed")

# --- 2. ESTILOS CSS (Vinotinto, Gris Ratón y Marca de Agua) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    /* Marca de Agua JPL */
    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        background-size: 60%;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.94); z-index: -1;
    }

    /* Diseño de Tarjetas */
    .top-bar-jpl { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin: -65px -20px 25px -20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.3); }
    .card-proceso { background-color: rgba(255, 255, 255, 0.92); padding: 15px; border-radius: 20px; box-shadow: 0px 2px 8px rgba(0,0,0,0.1); margin-bottom: 15px; border-left: 10px solid #800000; }
    
    /* BLOQUE GRIS RATÓN PARA AMENAZAS */
    .box-amenazas-jpl { background-color: #BEBEBE; padding: 15px; border-radius: 20px; border: 2px solid #800000; margin-bottom: 15px; color: black; }

    .stButton>button { background-color: #000000 !important; color: white !important; border-radius: 12px; border: 1px solid #800000; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 3. NAVEGACIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'splash'

if st.session_state.pantalla == 'splash':
    st.markdown('<div style="text-align:center; margin-top:150px;">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=250)
    st.markdown("<h1 style='color:#800000;'>GRUPO JPL</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    time.sleep(3)
    st.session_state.pantalla = 'inicio'
    st.rerun()

elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h2>SST - GRUPO JPL</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="card-proceso"><h3>Bienvenido</h3><p>Gestión de la Resolución 0312 de 2019</p></div>', unsafe_allow_html=True)
    
    if st.button("🛡️ INICIAR AUDITORÍA (60 ÍTEMS)"):
        st.session_state.pantalla = 'sst'
        st.rerun()
    if st.button("💰 PLANES EMPRESARIALES"):
        st.session_state.pantalla = 'licencias'
        st.rerun()

elif st.session_state.pantalla == 'sst':
    st.markdown('<div class="top-bar-jpl"><h3>AUDITORÍA RES. 0312</h3></div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["PLANEAR", "HACER", "VERIF/ACTUAR"])
    
    with tab1:
        st.markdown('<div class="card-proceso"><h4>I. RECURSOS (Ítems 1-8)</h4>', unsafe_allow_html=True)
        st.selectbox("1.1.1 Responsable del Sistema", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("1.1.3 Asignación de Recursos", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("1.2.1 Programa de Capacitación", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="card-proceso"><h4>II y III. SALUD Y RIESGOS (Ítems 9-42)</h4>', unsafe_allow_html=True)
        st.selectbox("2.1.1 Descripción Sociodemográfica", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("3.1.1 Identificación de Peligros", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

        # CASILLA GRIS RATÓN PARA AMENAZAS
        st.markdown('<div class="box-amenazas-jpl"><h4>IV. AMENAZAS (Ítems 43-47)</h4>', unsafe_allow_html=True)
        st.radio("43. Plan de Emergencias", ["Cumple", "No Cumple"], horizontal=True)
        st.radio("44. Brigada de Emergencia", ["Cumple", "No Cumple"], horizontal=True)
        st.radio("46. Simulacros Anuales", ["Cumple", "No Cumple"], horizontal=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="card-proceso"><h4>V, VI, VII. MEJORA (Ítems 48-60)</h4>', unsafe_allow_html=True)
        st.selectbox("5.1.1 Auditoría Anual", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("6.1.1 Plan de Mejoramiento", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ VOLVER"):
        st.session_state.pantalla = 'inicio'
        st.rerun()

elif st.session_state.pantalla == 'licencias':
    st.markdown('<div class="top-bar-jpl"><h3>PLANES</h3></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    planes = [("PEQUEÑA", "$40k"), ("MEDIANA", "$60k"), ("GRANDE", "$100k")]
    for i, col in enumerate([c1, c2, c3]):
        with col:
            st.markdown(f'<div class="card-proceso"><b>{planes[i][0]}</b><br>{planes[i][1]}</div>', unsafe_allow_html=True)
            st.button("Pedir", key=f"p{i}")
    
    if st.button("⬅️ VOLVER"):
        st.session_state.pantalla = 'inicio'
        st.rerun()

# --- BARRA INFERIOR ---
if st.session_state.pantalla != 'splash':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    c_nav = st.columns(3)
    with c_nav[0]: 
        if st.button("🏠"): st.session_state.pantalla = 'inicio'; st.rerun()
    with c_nav[1]: 
        if st.button("🛡️"): st.session_state.pantalla = 'sst'; st.rerun()
    with c_nav[2]: 
        if st.button("📊"): st.info("Reporte pronto")
