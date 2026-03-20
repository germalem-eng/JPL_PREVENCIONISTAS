import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

# --- 2. ESTILOS AVANZADOS (Vinotinto y Negro Profesional) ---
st.markdown("""
<style>
    /* Estilo del Sidebar */
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Caja de Login */
    .login-box {
        padding: 40px; border-radius: 15px;
        background-color: #f8f9fa; border: 2px solid #800000;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Botón Salir Estilizado */
    .stButton>button {
        width: 100%; border-radius: 5px; height: 3em;
        background-color: #000000; color: white !important;
        border: 1px solid #800000; font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #800000; border: 1px solid #000000;
    }

    /* Encabezado */
    .app-header {
        padding: 15px; background-color: #000000;
        border-bottom: 5px solid #800000; color: #FFFFFF;
        text-align: center; font-size: 22px; font-weight: bold;
    }
    
    .social-link {
        display: block; padding: 10px; margin: 5px 0;
        border-radius: 5px; text-align: center;
        font-weight: bold; text-decoration: none; color: white !important;
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
        st.markdown("""
        <div class="login-box">
            <h1 style='color: #800000; margin-bottom:0;'>GRUPO JPL</h1>
            <p style='color: #555;'>Sistema de Gestión de Riesgos</p>
            <hr>
        </div>
        """, unsafe_allow_html=True)
        
        # Formulario limpio
        u = st.text_input("👤 Usuario identificador:").strip().lower()
        p = st.text_input("🔑 Contraseña de acceso:", type="password").strip()
        
        if st.button("🔓 ENTRAR AL SISTEMA"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("Acceso denegado. Verifique sus credenciales.")
    st.stop()

# --- 4. BARRA LATERAL (DATOS COMPLETOS) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/Logo_robot_2007.jpg", width=150)
    st.markdown("### 📞 CONTACTO OFICIAL")
    st.write("📍 **Dirección:** Gestión Nacional")
    st.write("📧 **Email:** jplprevencionistas@gmail.com")
    st.write("📱 **Tel:** 301 601 5891")
    st.markdown("---")
    
    menu = st.radio("MENÚ DE GESTIÓN:", ["📊 Panel de Control", "🛡️ Evaluación 60 Ítems", "💰 Licencias de Uso", "🔔 Alertas"])
    
    st.markdown("---")
    st.markdown('<a href="https://wa.me/573016015891" class="social-link" style="background-color: #25D366;">WhatsApp Soporte</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://facebook.com/jplprevencionistas" class="social-link" style="background-color: #1877F2;">Facebook Oficial</a>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚪 SALIR (CERRAR SESIÓN)"):
        st.session_state['autenticado'] = False
        st.rerun()

# --- 5. CUERPO PRINCIPAL ---
st.markdown('<div class="app-header">SISTEMA INTEGRAL DE GESTIÓN SST - GRUPO JPL</div>', unsafe_allow_html=True)

if menu == "📊 Panel de Control":
    st.header("📈 Dashboard de Gestión")
    # Aquí va la línea de tiempo PHVA que te pasé antes...
    st.success("Bienvenido de nuevo, Ingeniero Gerardo.")

elif menu == "💰 Licencias de Uso":
    st.header("💳 Tarifas del Servicio")
    c1, c2, c3 = st.columns(3)
    with c1: st.info("Pequeña: $40.000")
    with c2: st.warning("Mediana: $60.000")
    with c3: st.error("Grande: $100.000")
