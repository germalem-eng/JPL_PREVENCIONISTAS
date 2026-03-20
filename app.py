import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

# --- 2. ESTILOS (Vinotinto Profesional) ---
st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
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

# --- 3. ACCESO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<div style='text-align:center; padding:20px; border:2px solid #800000; border-radius:15px;'>", unsafe_allow_html=True)
        st.header("🔐 INGRESO JPL")
        u = st.text_input("Usuario:").lower()
        p = st.text_input("Clave:", type="password")
        if st.button("ENTRAR"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Error de acceso")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- 4. MENÚ LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg")
    st.markdown("---")
    menu = st.radio("MENÚ:", ["📊 Panel de Control", "🛡️ Auditoría 60 Ítems", "💰 Licencias de Uso"])
    st.markdown("---")
    if st.button("🚪 CERRAR SESIÓN"):
        st.session_state['auth'] = False
        st.rerun()

# --- 5. CONTENIDO ---
num_wa = "573016015891"

if menu == "📊 Panel de Control":
    st.title("📊 Panel Interactivo PHVA")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="phva-circle">P</div><p style="text-align:center"><b>PLANEAR</b></p>', unsafe_allow_html=True)
        if st.button("Ver Plan"): st.info("📅 Generando cronograma...")
    with c2:
        st.markdown('<div class="phva-circle">H</div><p style="text-align:center"><b>HACER</b></p>', unsafe_allow_html=True)
        st.file_uploader("Cargar Evidencia")
    with c3:
        st.markdown('<div class="phva-circle">V</div><p style="text-align:center"><b>VERIFICAR</b></p>', unsafe_allow_html=True)
        if st.button("Auditar"): st.warning("🔍 Analizando brechas...")
    with c4:
        st.markdown('<div class="phva-circle">A</div><p style="text-align:center"><b>ACTUAR</b></p>', unsafe_allow_html=True)
        st.text_area("Mejora Continua:")

elif menu == "🛡️ Auditoría 60 Ítems":
    st.title("🛡️ Auditoría Resolución 0312")
    with st.form("audit"):
        st.selectbox("¿Recursos financieros asignados?", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("¿Afiliación a Seguridad Social?", ["Cumple", "No Cumple", "N/A"])
        if st.form_submit_button("Guardar Avance"): st.success("¡Datos registrados!")

elif menu == "💰 Licencias de Uso":
    st.title("💰 Planes de Afiliación")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="price-card"><h3>PEQUEÑA</h3><p>1-10 emp.</p><h2>$40.000</h2></div>', unsafe_allow_html=True)
        st.link_button("ADQUIRIR 40K", f"https://wa.me/{num_wa}?text=Hola%20JPL,%20quiero%20información%20del%20Plan%20Pequeña%20($40k)")

    with col2:
        st.markdown('<div class="price-card"><h3>MEDIANA</h3><p>11-50 emp.</p><h2>$60.000</h2></div>', unsafe_allow_html=True)
        st.link_button("ADQUIRIR 60K", f"https://wa.me/{num_wa}?text=Hola%20JPL,%20quiero%20información%20del%20Plan%20Mediana%20($60k)")

    with col3:
        st.markdown('<div class="price-card"><h3>GRANDE</h3><p>51+ emp.</p><h2>$100.000</h2></div>', unsafe_allow_html=True)
        st.link_button("ADQUIRIR 100K", f"https://wa.me/{num_wa}?text=Hola%20JPL,%20quiero%20información%20del%20Plan%20Grande%20($100k)")
