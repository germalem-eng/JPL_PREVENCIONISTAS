import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN Y ESTILOS ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button { width: 100%; background-color: #000000; color: white !important; border: 1px solid white; font-weight: bold; }
    .sidebar-link { color: white !important; text-decoration: none; display: block; margin-bottom: 8px; font-size: 14px; }
    .price-card { border: 2px solid #800000; padding: 20px; border-radius: 10px; text-align: center; background-color: white; height: 100%; }
    .phva-circle { width: 70px; height: 70px; background-color: #800000; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; margin: 0 auto; border: 2px solid black; }
</style>
""", unsafe_allow_html=True)

# --- 2. FUNCIÓN DE NOTIFICACIÓN (CON SUS 16 LETRAS) ---
def alerta_socio(plan_nombre):
    mi_correo = "germalem@gmail.com"
    clave_google = "pelmjgainynleacx" 
    
    msg = MIMEText(f"Ing. Gerardo, un cliente está interesado en el Plan: {plan_nombre}")
    msg['Subject'] = f"🚀 NUEVO INTERESADO JPL - {plan_nombre}"
    msg['From'] = mi_correo
    msg['To'] = mi_correo
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(mi_correo, clave_google)
        server.sendmail(mi_correo, mi_correo, msg.as_string())
        server.quit()
        st.toast(f"✅ Notificación enviada a {mi_correo}", icon="📧")
    except Exception as e:
        st.error(f"Error técnico en correo: {e}")

# --- 3. SISTEMA DE ACCESO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br><div style='text-align:center; border:2px solid #800000; padding:20px; border-radius:15px;'>", unsafe_allow_html=True)
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

# --- 4. BARRA LATERAL (CONTACTO Y MENÚ) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg")
    st.markdown("### 📞 CONTACTO DIRECTO")
    st.markdown('<a href="tel:3016015891" class="sidebar-link">📞 Llamar: 301 601 5891</a>', unsafe_allow_html=True)
    st.markdown('<a href="mailto:jplprevencionistas@gmail.com" class="sidebar-link">✉️ mail: jplprevencionistas@gmail.com</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://facebook.com/jplprevencionistas" target="_blank" class="sidebar-link">🌐 Jplprevencionistas</a>', unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("MENÚ DE GESTIÓN:", ["📊 Panel de Control", "🛡️ Auditoría 60 Ítems", "💰 Licencias de Uso"])
    st.markdown("---")
    if st.button("CERRAR SESIÓN"):
        st.session_state['auth'] = False
        st.rerun()

# --- 5. LÓGICA DE MÓDULOS ---
num_wa = "573016015891"

if menu == "📊 Panel de Control":
    st.title("📊 Ciclo PHVA Interactivo")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="phva-circle">P</div><p style="text-align:center"><b>PLANEAR</b></p>', unsafe_allow_html=True)
        if st.button("Ver Cronograma"): st.success("📅 Plan de trabajo 2026 activo.")
    with c2:
        st.markdown('<div class="phva-circle">H</div><p style="text-align:center"><b>HACER</b></p>', unsafe_allow_html=True)
        st.file_uploader("Cargar registros SST")
    with c3:
        st.markdown('<div class="phva-circle">V</div><p style="text-align:center"><b>VERIFICAR</b></p>', unsafe_allow_html=True)
        st.write("Estado de cumplimiento:")
        st.progress(65)
    with c4:
        st.markdown('<div class="phva-circle">A</div><p style="text-align:center"><b>ACTUAR</b></p>', unsafe_allow_html=True)
        st.text_area("Acciones preventivas:")

elif menu == "🛡️ Auditoría 60 Ítems":
    st.title("🛡️ Auditoría Resolución 0312")
    with st.form("audit_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            st.selectbox("¿Recursos financieros asignados?", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("¿Seguridad Social al día?", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("¿Capacitación SST ejecutada?", ["Cumple", "No Cumple", "N/A"])
        with col_b:
            st.selectbox("¿Evaluaciones médicas vigentes?", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("¿Matriz de peligros actualizada?", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("¿COPASST conformado?", ["Cumple", "No Cumple", "N/A"])
        if st.form_submit_button("GENERAR REPORTE"):
            st.success("Auditoría guardada exitosamente.")

elif menu == "💰 Licencias de Uso":
    st.title("💰 Planes de Afiliación")
    st.info("Al dar clic en adquirir, un asesor se contactará para la vinculación.")
    
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.markdown('<div class="price-card"><h3>PEQUEÑA</h3><h2>$40.000</h2><p>1-10 emp.</p></div>', unsafe_allow_html=True)
        if st.button("ADQUIRIR 40K"):
            alerta_socio("Pequeña $40.000")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://wa.me/{num_wa}?text=Hola,%20deseo%20afiliarme%20al%20Plan%20Pequeño\'" />', unsafe_allow_html=True)
    with col_2:
        st.markdown('<div class="price-card"><h3>MEDIANA</h3><h2>$60.000</h2><p>11-50 emp.</p></div>', unsafe_allow_html=True)
        if st.button("ADQUIRIR 60K"):
            alerta_socio("Mediana $60.000")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://wa.me/{num_wa}?text=Hola,%20deseo%20afiliarme%20al%20Plan%20Mediano\'" />', unsafe_allow_html=True)
    with col_3:
        st.markdown('<div class="price-card"><h3>GRANDE</h3><h2>$100.000</h2><p>+50 emp.</p></div>', unsafe_allow_html=True)
        if st.button("ADQUIRIR 100K"):
            alerta_socio("Grande $100.000")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://wa.me/{num_wa}?text=Hola,%20deseo%20afiliarme%20al%20Plan%20Grande\'" />', unsafe_allow_html=True)
