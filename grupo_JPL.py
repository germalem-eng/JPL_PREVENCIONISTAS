import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

# --- 2. ESTILOS AVANZADOS ---
st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .login-box {
        padding: 40px; border-radius: 15px;
        background-color: #f8f9fa; border: 2px solid #800000;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    .app-header {
        padding: 15px; background-color: #000000;
        border-bottom: 5px solid #800000; color: #FFFFFF;
        text-align: center; font-size: 22px; font-weight: bold;
    }
    /* Estilo para los cuadros de precios */
    .price-card {
        border: 2px solid #800000; padding: 20px; border-radius: 10px;
        text-align: center; background-color: #fff; height: 100%;
    }
    .buy-btn {
        display: block; width: 100%; padding: 10px; margin-top: 10px;
        background-color: #800000; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: bold;
    }
    /* Estilo para la línea de tiempo */
    .phva-container {
        display: flex; justify-content: space-between;
        margin: 20px 0; padding: 20px;
        background-color: #f8f9fa; border-radius: 10px; border: 1px solid #800000;
    }
    .circle {
        width: 60px; height: 60px; background-color: #800000;
        color: white; border-radius: 50%; display: flex;
        align-items: center; justify-content: center;
        margin: 0 auto 10px; font-weight: bold; font-size: 24px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. ACCESO PERSONALIZADO ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown('<div class="login-box"><h1 style="color: #800000;">GRUPO JPL</h1><p>Gestión de Riesgos SST</p></div>', unsafe_allow_html=True)
        u = st.text_input("👤 Usuario:").strip().lower()
        p = st.text_input("🔑 Clave:", type="password").strip()
        if st.button("🔓 ENTRAR"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['autenticado'] = True
                st.rerun()
            else: st.error("Acceso denegado")
    st.stop()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.markdown("### 📞 CONTACTO OFICIAL")
    st.write("📍 Gestión Nacional | 📱 301 601 5891")
    st.write("📧 jplprevencionistas@gmail.com")
    st.markdown("---")
    menu = st.radio("MENÚ:", ["📊 Panel de Control", "💰 Licencias de Uso"])
    if st.button("🚪 SALIR (CERRAR SESIÓN)"):
        st.session_state['autenticado'] = False
        st.rerun()

# --- 5. CONTENIDO ---
st.markdown('<div class="app-header">SISTEMA INTEGRAL DE GESTIÓN SST - GRUPO JPL</div>', unsafe_allow_html=True)

if menu == "📊 Panel de Control":
    st.header("📈 Ciclo de Mejora Continua (PHVA)")
    st.markdown("""
    <div class="phva-container">
        <div style="text-align:center"><div class="circle">P</div><b>PLANEAR</b></div>
        <div style="text-align:center"><div class="circle">H</div><b>HACER</b></div>
        <div style="text-align:center"><div class="circle">V</div><b>VERIFICAR</b></div>
        <div style="text-align:center"><div class="circle">A</div><b>ACTUAR</b></div>
    </div>
    """, unsafe_allow_html=True)
    st.info("Bienvenido de nuevo, Ingeniero Gerardo.")

elif menu == "💰 Licencias de Uso":
    st.header("💳 Tarifas de Licencia Mensual")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="price-card"><h3>Pequeña</h3><p>1-10 emp.</p><h2>$40.000</h2>
        <a href="https://wa.me/573016015891?text=Licencia%2040k" class="buy-btn">ADQUIRIR</a></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="price-card" style="background-color: #fff9f9;"><h3>Mediana</h3><p>11-50 emp.</p><h2>$60.000</h2>
        <a href="https://wa.me/573016015891?text=Licencia%2060k" class="buy-btn">ADQUIRIR</a></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="price-card"><h3>Grande</h3><p>51+ emp.</p><h2>$100.000</h2>
        <a href="https://wa.me/573016015891?text=Licencia%20100k" class="buy-btn">ADQUIRIR</a></div>""", unsafe_allow_html=True)
