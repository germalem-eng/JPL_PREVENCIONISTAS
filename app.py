import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

# --- 2. ESTILOS PERSONALIZADOS (VINOTINTO Y PROFESIONAL) ---
st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button {
        width: 100%; background-color: #000000; color: white !important;
        border: 2px solid #800000; font-weight: bold;
    }
    .stButton>button:hover { background-color: #800000; }
    .price-card {
        border: 2px solid #800000; padding: 20px; border-radius: 10px;
        text-align: center; background-color: #ffffff; height: 100%;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .phva-circle {
        width: 80px; height: 80px; background-color: #800000;
        color: white; border-radius: 50%; display: flex;
        align-items: center; justify-content: center;
        font-size: 28px; font-weight: bold; margin: 0 auto;
        border: 3px solid #000000;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. CONTROL DE ACCESO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div style='text-align:center; padding:30px; border:2px solid #800000; border-radius:15px;'>", unsafe_allow_html=True)
        st.header("🔐 INGRESO CORPORATIVO")
        u = st.text_input("Usuario:").lower()
        p = st.text_input("Contraseña:", type="password")
        if st.button("ACCEDER AL SISTEMA"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Credenciales incorrectas")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- 4. BARRA LATERAL (LOGO Y CONTACTO) ---
with st.sidebar:
    # Intentar cargar logo desde su GitHub
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", use_container_width=True)
    
    st.markdown("### 📞 CONTACTO DIRECTO")
    st.write("📍 **Sede:** Gestión Nacional")
    st.write("📱 **WhatsApp:** 301 601 5891")
    st.write("📧 **Email:** jplprevencionistas@gmail.com")
    st.markdown("---")
    
    opcion = st.radio("MENÚ DE GESTIÓN:", ["📊 Panel de Control", "💰 Licencias de Uso", "🛡️ Auditoría"])
    
    st.markdown("---")
    if st.button("🚪 CERRAR SESIÓN"):
        st.session_state['auth'] = False
        st.rerun()

# --- 5. SECCIONES PRINCIPALES ---

if opcion == "📊 Panel de Control":
    st.title("📈 Ciclo de Gestión PHVA")
    st.subheader("Metodología de Mejora Continua")
    
    col_p, col_h, col_v, col_a = st.columns(4)
    with col_p:
        st.markdown('<div class="phva-circle">P</div><p style="text-align:center"><b>PLANEAR</b></p>', unsafe_allow_html=True)
    with col_h:
        st.markdown('<div class="phva-circle">H</div><p style="text-align:center"><b>HACER</b></p>', unsafe_allow_html=True)
    with col_v:
        st.markdown('<div class="phva-circle">V</div><p style="text-align:center"><b>VERIFICAR</b></p>', unsafe_allow_html=True)
    with col_a:
        st.markdown('<div class="phva-circle">A</div><p style="text-align:center"><b>ACTUAR</b></p>', unsafe_allow_html=True)
    
    st.info("Bienvenido, Ingeniero Gerardo. El sistema está sincronizado con la normativa 2026.")

elif opcion == "💰 Licencias de Uso":
    st.title("💳 Planes y Licencias Mensuales")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="price-card"><h3>PEQUEÑA</h3><p>1-10 Trabajadores</p><h2 style="color:#800000">$40.000</h2><p>Mensual</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="price-card"><h3>MEDIANA</h3><p>11-50 Trabajadores</p><h2 style="color:#800000">$60.000</h2><p>Mensual</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="price-card"><h3>GRANDE</h3><p>+50 Trabajadores</p><h2 style="color:#800000">$100.000</h2><p>Mensual</p></div>', unsafe_allow_html=True)
