import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN Y ESTILOS ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');

    /* Aplicar Chilanka de forma global */
    html, body, [class*="st-"], .main, h1, h2, h3, p, button, label, select, input {
        font-family: 'Chilanka', cursive !important;
    }

    /* Sidebar Institucional */
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Botones Corporativos */
    .stButton>button { 
        width: 100%; 
        background-color: #000000; 
        color: white !important; 
        border: 1px solid white; 
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #444444; border: 1px solid #800000; }

    /* Logo con transparencia */
    .logo-transparente {
        opacity: 0.80;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 300px;
    }

    /* ESTILOS DE CASILLAS (BOXES) */
    .box-procesos {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #800000;
        margin-bottom: 20px;
        color: #333;
    }

    .box-amenazas {
        background-color: #e0e0e0; /* Gris Ratón Claro */
        padding: 20px;
        border-radius: 12px;
        border: 2px dashed #800000;
        margin-bottom: 20px;
        color: #000;
    }

    .price-card { border: 2px solid #800000; padding: 15px; border-radius: 10px; text-align: center; background: white; color: black; }
</style>
""", unsafe_allow_html=True)

# --- 2. NOTIFICACIONES ---
def alerta_socio(plan_nombre):
    mi_correo = "germalem@gmail.com"
    clave_google = "gwjjbwsnynpndaon" 
    msg = MIMEText(f"Ing. Gerardo, hay un nuevo interesado en el {plan_nombre}")
    msg['Subject'] = f"🚀 ALERTA JPL - {plan_nombre}"
    msg['From'] = mi_correo
    msg['To'] = mi_correo
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(mi_correo, clave_google)
        server.sendmail(mi_correo, mi_correo, msg.as_string())
        server.quit()
        st.toast("Notificación enviada al Ing. Gerardo", icon="📧")
    except: pass

# --- 3. ACCESO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", use_container_width=True)
        with st.container(border=True):
            st.header("🔐 ACCESO JPL")
            u = st.text_input("Usuario").lower()
            p = st.text_input("Clave", type="password")
            if st.button("INGRESAR"):
                if u == "gerardo" and p == "mym2007":
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Credenciales incorrectas")
    st.stop()

# --- 4. NAVEGACIÓN ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg")
    st.markdown("---")
    menu = st.sidebar.radio("MENÚ DE GESTIÓN", ["🏠 Inicio", "🛡️ Auditoría 60 Ítems", "💰 Licencias"])
    if st.button("SALIR"):
        st.session_state['auth'] = False
        st.rerun()

# --- 5. MÓDULOS ---
num_wa = "573016015891"

if menu == "🏠 Inicio":
    st.markdown('<img src="https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg" class="logo-transparente">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#800000;'>GRUPO JPL</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Consultoría Especializada en SST</h3>", unsafe_allow_html=True)
    st.write("Bienvenido al entorno digital para la administración de la Resolución 0312 de 2019.")

elif menu == "🛡️ Auditoría 60 Ítems":
    st.title("🛡️ Auditoría Completa - Res. 0312")
    
    with st.form("audit_completa"):
        
        # --- BLOQUE I: RECURSOS ---
        st.markdown('<div class="box-procesos">', unsafe_allow_html=True)
        st.subheader("I. RECURSOS (Ítems 1-8)")
        c1, c2 = st.columns(2)
        with c1:
            st.selectbox("1.1.1 Responsable del SG-SST", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("1.1.3 Asignación de Recursos", ["Cumple", "No Cumple", "N/A"])
        with c2:
            st.selectbox("1.1.5 Pago Seguridad Social", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("1.2.1 Programa de Capacitación", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

        # --- BLOQUE II: SALUD ---
        st.markdown('<div class="box-procesos">', unsafe_allow_html=True)
        st.subheader("II. GESTIÓN DE LA SALUD (Ítems 9-23)")
        c3, c4 = st.columns(2)
        with c3:
            st.selectbox("2.1.1 Descripción Sociodemográfica", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("2.2.1 Evaluaciones Médicas", ["Cumple", "No Cumple", "N/A"])
        with c4:
            st.selectbox("2.3.1 Reporte de AT y EL", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("2.4.1 Registro de Estadísticas", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

        # --- BLOQUE III: RIESGOS ---
        st.markdown('<div class="box-procesos">', unsafe_allow_html=True)
        st.subheader("III. GESTIÓN DE RIESGOS (Ítems 24-42)")
        c5, c6 = st.columns(2)
        with c5:
            st.selectbox("3.1.1 Identificación de Peligros", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("3.2.1 Inspecciones de Seguridad", ["Cumple", "No Cumple", "N/A"])
        with c6:
            st.selectbox("3.3.1 Mantenimiento de Equipos", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("3.4.1 Entrega de EPP", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

        # --- BLOQUE IV: AMENAZAS (GRIS RATÓN) ---
        st.markdown('<div class="box-amenazas">', unsafe_allow_html=True)
        st.subheader("IV. AMENAZAS (Ítems 43-47)")
        st.write("⚠️ *Preparación ante Emergencias*")
        c7, c8 = st.columns(2)
        with c7:
            st.radio("43. Plan de Emergencias", ["Cumple", "No Cumple"], horizontal=True)
            st.radio("44. Conformación de Brigada", ["Cumple", "No Cumple"], horizontal=True)
        with c8:
            st.radio("45. Capacitación en Emergencias", ["Cumple", "No Cumple"], horizontal=True)
            st.radio("46. Realización de Simulacros", ["Cumple", "No Cumple"], horizontal=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # --- BLOQUE V: MEJORA ---
        st.markdown('<div class="box-procesos">', unsafe_allow_html=True)
        st.subheader("V. VERIFICACIÓN Y MEJORA (Ítems 48-60)")
        st.selectbox("5.1.1 Auditoría Anual", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("6.1.1 Plan de Mejoramiento", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

        if st.form_submit_button("💾 GUARDAR AUDITORÍA"):
            st.success("Evaluación guardada con éxito.")

elif menu == "💰 Licencias":
    st.title("💰 Planes de Afiliación")
    col_p = st.columns(3)
    planes = [("PEQUEÑA", "40.000"), ("MEDIANA", "60.000"), ("GRANDE", "100.000")]
    for i, p in enumerate(col_p):
        with p:
            st.markdown(f'<div class="price-card"><h3>{planes[i][0]}</h3><h2>${planes[i][1]}</h2></div>', unsafe
