import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN Y ESTILOS ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');

    /* Aplicar Chilanka a toda la app */
    html, body, [class*="st-"], .main, h1, h2, h3, p, button, label {
        font-family: 'Chilanka', cursive !important;
    }

    /* Sidebar con color institucional */
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Botones estilo JPL */
    .stButton>button { 
        width: 100%; 
        background-color: #000000; 
        color: white !important; 
        border: 1px solid white; 
        font-weight: bold;
        border-radius: 10px;
    }

    /* Logo con transparencia */
    .logo-transparente {
        opacity: 0.85;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 350px;
    }

    /* Casilla Gris Ratón para Amenazas */
    .amenazas-box {
        background-color: #e0e0e0;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #bcbcbc;
        color: #333333;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .price-card { border: 2px solid #800000; padding: 20px; border-radius: 10px; text-align: center; background-color: white; color: black; }
    .phva-circle { width: 70px; height: 70px; background-color: #800000; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; margin: 0 auto; border: 2px solid black; }
</style>
""", unsafe_allow_html=True)

# --- 2. FUNCIÓN DE NOTIFICACIÓN ---
def alerta_socio(plan_nombre):
    mi_correo = "germalem@gmail.com"
    clave_google = "gwjjbwsnynpndaon" 
    msg = MIMEText(f"Ing. Gerardo, un cliente está interesado en el Plan: {plan_nombre}")
    msg['Subject'] = f"🚀 NUEVO INTERESADO JPL - {plan_nombre}"
    msg['From'] = mi_correo
    msg['To'] = mi_correo
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(mi_correo, clave_google)
        server.sendmail(mi_correo, mi_correo, msg.as_string())
        server.quit()
        st.toast(f"✅ Notificación enviada", icon="📧")
    except Exception as e:
        st.error(f"Error técnico: {e}")

# --- 3. SISTEMA DE ACCESO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", use_container_width=True)
        st.markdown("<div style='text-align:center; border:2px solid #800000; padding:20px; border-radius:15px;'>", unsafe_allow_html=True)
        st.header("🔐 INGRESO CORPORATIVO")
        u = st.text_input("Usuario:").lower()
        p = st.text_input("Clave:", type="password")
        if st.button("ENTRAR"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Acceso denegado")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg")
    st.markdown("### 📞 CONTACTO")
    st.markdown("---")
    menu = st.radio("MENÚ:", ["🏠 Inicio", "📊 PHVA", "🛡️ Auditoría 60 Ítems", "💰 Licencias"])
    if st.button("CERRAR SESIÓN"):
        st.session_state['auth'] = False
        st.rerun()

# --- 5. LÓGICA DE MÓDULOS ---
num_wa = "573016015891"

if menu == "🏠 Inicio":
    st.markdown("<h1 style='text-align: center; color: #800000;'>GRUPO JPL</h1>", unsafe_allow_html=True)
    # Logo con efecto de transparencia aplicado vía HTML class
    st.markdown('<img src="https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg" class="logo-transparente">', unsafe_allow_html=True)
    st.subheader("Consultoría en Seguridad y Salud en el Trabajo")
    st.write("Bienvenido al sistema de gestión digital de la Resolución 0312 de 2019.")

elif menu == "📊 PHVA":
    st.title("📊 Ciclo de Mejora")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="phva-circle">P</div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="phva-circle">H</div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="phva-circle">V</div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="phva-circle">A</div>', unsafe_allow_html=True)

elif menu == "🛡️ Auditoría 60 Ítems":
    st.title("🛡️ Auditoría Resolución 0312")
    
    with st.form("audit_form"):
        st.subheader("I. RECURSOS, II. SALUD y III. RIESGOS")
        st.info("Complete los ítems de gestión base.")
        col_std = st.columns(2)
        with col_std[0]:
            st.selectbox("1. Responsable del Sistema", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("2. Recursos Financieros", ["Cumple", "No Cumple", "N/A"])
        with col_std[1]:
            st.selectbox("3. Afiliación Seguridad Social", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("4. Identificación de Peligros", ["Cumple", "No Cumple", "N/A"])

        # CASILLA ESPECIAL GRIS PARA AMENAZAS
        st.markdown('<div class="amenazas-box">', unsafe_allow_html=True)
        st.subheader("IV. AMENAZAS (Ítems 43-47)")
        col_amen = st.columns(2)
        with col_amen[0]:
            st.radio("43. Plan de Prevención Emergencias", ["Cumple", "No Cumple"], horizontal=True)
            st.radio("44. Brigada de Emergencia", ["Cumple", "No Cumple"], horizontal=True)
        with col_amen[1]:
            st.radio("45. Capacitación Emergencias", ["Cumple", "No Cumple"], horizontal=True)
            st.radio("46. Simulacros Anuales", ["Cumple", "No Cumple"], horizontal=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("V. VERIFICACIÓN Y MEJORA")
        st.selectbox("60. Plan de Mejoramiento", ["Cumple", "No Cumple", "N/A"])

        if st.form_submit_button("GUARDAR EVALUACIÓN"):
            st.success("Evaluación guardada correctamente.")

elif menu == "💰 Licencias":
    st.title("💰 Planes")
    c_p = st.columns(3)
    p_data = [("PEQUEÑA", "40k"), ("MEDIANA", "60k"), ("GRANDE", "100k")]
    for i, col in enumerate(c_p):
        with col:
            st.markdown(f'<div class="price-card"><h3>{p_data[i][0]}</h3><h2>{p_data[i][1]}</h2></div>', unsafe_allow_html=True)
            if st.button(f"Comprar {p_data[i][0]}"):
                alerta_socio(p_data[i][0])
                st.write("Abriendo WhatsApp...")
