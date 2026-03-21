import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN Y ESTILOS ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

# Inyección de fuente Chilanka y estilos corporativos
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');

    /* Aplicar Chilanka a toda la app */
    html, body, [class*="st-"], .main, h1, h2, h3, p, button {
        font-family: 'Chilanka', cursive !important;
    }

    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    .stButton>button { 
        width: 100%; 
        background-color: #000000; 
        color: white !important; 
        border: 1px solid white; 
        font-weight: bold;
        border-radius: 10px;
    }
    
    .sidebar-link { color: white !important; text-decoration: none; display: block; margin-bottom: 8px; font-size: 14px; }
    .price-card { border: 2px solid #800000; padding: 20px; border-radius: 10px; text-align: center; background-color: white; color: black; }
    .phva-circle { width: 80px; height: 80px; background-color: #800000; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: bold; margin: 0 auto; border: 3px solid black; }
    
    /* Estilo para el logo en inicio */
    .logo-container { text-align: center; margin-bottom: 20px; }
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
        st.toast(f"✅ Notificación enviada a {mi_correo}", icon="📧")
    except Exception as e:
        st.error(f"Error técnico en correo: {e}")

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
    st.markdown("### 📞 CONTACTO DIRECTO")
    st.markdown('<a href="tel:3016015891" class="sidebar-link">📞 301 601 5891</a>', unsafe_allow_html=True)
    st.markdown('<a href="mailto:jplprevencionistas@gmail.com" class="sidebar-link">✉️ jplprevencionistas@gmail.com</a>', unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("MENÚ DE GESTIÓN:", ["🏠 Inicio", "📊 Panel PHVA", "🛡️ Auditoría (60 Ítems)", "💰 Licencias"])
    st.markdown("---")
    if st.button("CERRAR SESIÓN"):
        st.session_state['auth'] = False
        st.rerun()

# --- 5. LÓGICA DE MÓDULOS ---
num_wa = "573016015891"

if menu == "🏠 Inicio":
    st.markdown("<h1 style='text-align: center; color: #800000;'>BIENVENIDO A GRUPO JPL</h1>", unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=400)
    st.subheader("Consultoría Integral en Seguridad y Salud en el Trabajo")
    st.write("""
    Esta plataforma permite gestionar de manera eficiente el Sistema de Gestión (SG-SST) bajo la normativa colombiana.
    Utilice el menú lateral para navegar entre los módulos de cumplimiento, auditoría y servicios.
    """)
    st.info("💡 Consejo: Complete la auditoría de 60 ítems para conocer su nivel de cumplimiento legal.")

elif menu == "📊 Panel PHVA":
    st.title("📊 Ciclo de Mejora Continua")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="phva-circle">P</div><p style="text-align:center"><b>PLANEAR</b></p>', unsafe_allow_html=True)
        st.button("Cronograma")
    with c2:
        st.markdown('<div class="phva-circle">H</div><p style="text-align:center"><b>HACER</b></p>', unsafe_allow_html=True)
        st.file_uploader("Cargar registros")
    with c3:
        st.markdown('<div class="phva-circle">V</div><p style="text-align:center"><b>VERIFICAR</b></p>', unsafe_allow_html=True)
        st.progress(65)
    with c4:
        st.markdown('<div class="phva-circle">A</div><p style="text-align:center"><b>ACTUAR</b></p>', unsafe_allow_html=True)
        st.text_area("Mejoras:")

elif menu == "🛡️ Auditoría (60 Ítems)":
    st.title("🛡️ Evaluación Estándares Mínimos (Res. 0312)")
    st.write("Complete los 60 ítems divididos por capítulos:")
    
    # Estructura simplificada de los 60 ítems por categorías reales
    categorias = {
        "I. RECURSOS (1-8)": ["Responsable SG-SST", "Recursos Financieros", "Seguridad Social", "COPASST", "Comité Convivencia", "Programa Capacitación", "Inducción", "Curso Virtual 50h"],
        "II. GESTIÓN DE LA SALUD (9-23)": ["Diagnóstico Salud", "Evaluaciones Médicas", "Historias Clínicas", "Reporte AT/EL", "Estadísticas Salud"],
        "III. GESTIÓN DE RIESGOS (24-42)": ["Matriz de Peligros", "Medidas de Control", "Mantenimiento Equipos", "Entrega de EPP"],
        "IV. AMENAZAS (43-47)": ["Plan Emergencias", "Brigadas SST"],
        "V. VERIFICACIÓN Y MEJORA (48-60)": ["Auditoría Anual", "Revisión Gerencial", "Plan de Mejoramiento"]
    }
    
    with st.form("audit_completa"):
        for cat, items in categorias.items():
            st.subheader(cat)
            cols = st.columns(2)
            for idx, item in enumerate(items):
                with cols[idx % 2]:
                    st.radio(f"{item}", ["Cumple", "No Cumple", "N/A"], horizontal=True, key=f"item_{item}")
        
        if st.form_submit_button("FINALIZAR AUDITORÍA Y GENERAR REPORTE"):
            st.balloons()
            st.success("Auditoría procesada. Se ha generado un plan de acción preventivo.")

elif menu == "💰 Licencias":
    st.title("💰 Planes de Afiliación")
    col_1, col_2, col_3 = st.columns(3)
    
    planes = [
        {"nombre": "PEQUEÑA", "precio": "40.000", "desc": "1-10 emp.", "wa": "Plan Pequeño"},
        {"nombre": "MEDIANA", "precio": "60.000", "desc": "11-50 emp.", "wa": "Plan Mediano"},
        {"nombre": "GRANDE", "precio": "100.000", "desc": "+50 emp.", "wa": "Plan Grande"}
    ]
    
    for i, p in enumerate([col_1, col_2, col_3]):
        with p:
            plan = planes[i]
            st.markdown(f'<div class="price-card"><h3>{plan["nombre"]}</h3><h2>${plan["precio"]}</h2><p>{plan["desc"]}</p></div>', unsafe_allow_html=True)
            if st.button(f"ADQUIRIR {plan['nombre']}"):
                alerta_socio(f"{plan['nombre']} ${plan['precio']}")
                st.markdown(f'<a href="https://wa.me/{num_wa}?text=Hola,%20deseo%20el%20{plan["wa"]}" target="_blank" style="text-decoration:none;"><button style="width:100%; background-color:#25D366; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer; font-weight:bold;">✅ ABRIR WHATSAPP</button></a>', unsafe_allow_html=True)
