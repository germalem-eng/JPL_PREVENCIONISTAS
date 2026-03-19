import streamlit as st
import os
import base64
from datetime import datetime

# --- 1. CONFIGURACIÓN DE LA APP ---
st.set_page_config(page_title="App Grupo JPL | Acceso Seguro", layout="wide", initial_sidebar_state="expanded")

def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

logo_b64 = get_base64("Logos/Logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 2. ESTILOS DE APLICACIÓN (AJUSTE ROJO) ---
st.html(f"""
<style>
    .stApp {{ background-color: #f4f7f6 !important; }}
    
    /* Barra Superior Estilo Software */
    .app-header {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 30px; background: linear-gradient(180deg, #f0f0f0 0%, #bdbdbd 100%);
        border-bottom: 2px solid #555; position: sticky; top: 0; z-index: 99;
    }}
    #reloj-app {{ font-family: 'Courier New', monospace; font-weight: bold; color: #111; }}

    /* FORMULARIO DE LOGIN */
    .login-box {{
        background: white; padding: 40px; border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1); border-top: 5px solid #d32f2f;
    }}
    
    /* --- CAMBIO SOLICITADO: MENÚ LATERAL EN ROJO --- */
    [data-testid="stSidebar"] {{
        background-color: #b71c1c !important; /* Rojo Intenso */
    }}
    
    /* Color del texto y radio buttons en el menú lateral para que resalten en blanco */
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {{
        color: white !important;
        font-weight: bold !important;
    }}
    
    /* Estilo para los botones dentro del sidebar */
    [data-testid="stSidebar"] button {{
        background-color: #ffffff !important;
        color: #b71c1c !important;
        border-radius: 8px !important;
    }}

    h1, h2, h3, p, label {{ font-family: 'Comic Sans MS', cursive !important; color: #111 !important; }}
</style>

<script>
    function updateClock() {{
        const now = new Date();
        document.getElementById('reloj-app').innerHTML = now.toLocaleTimeString('es-CO', {{ hour12: false }});
    }}
    setInterval(updateClock, 1000);
</script>
""")

# --- 3. MÓDULO DE SEGURIDAD (LOGIN) ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

def check_login():
    if st.session_state['usuario'].lower() == "gerardo" and st.session_state['clave'] == "mym2007":
        st.session_state['autenticado'] = True
    else:
        st.error("❌ Credenciales incorrectas para el Grupo JPL")

if not st.session_state['autenticado']:
    st.html('<div style="height: 50px;"></div>')
    col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
    with col_l2:
        st.html('<div class="login-box">')
        if logo_b64:
            st.image(f"data:image/jpeg;base64,{logo_b64}", width=150)
        st.title("🛡️ Grupo JPL")
        st.subheader("Acceso SST")
        st.text_input("Usuario:", key="usuario")
        st.text_input("Contraseña:", type="password", key="clave")
        st.button("Ingresar a la App", on_click=check_login, use_container_width=True)
        st.html('</div>')
    st.stop()

# --- 4. CUERPO DE LA APP (POST-LOGIN) ---

st.html(f"""
<div class="app-header">
    <div style="font-weight: bold; color: #b71c1c;">🛡️ GRUPO JPL | COMMAND CENTER v2.1</div>
    <div id="reloj-app">00:00:00</div>
</div>
""")

with st.sidebar:
    st.html('<h2 style="color:white !important;">Menú de Gestión</h2>')
    menu = st.radio("MÓDULOS:", ["📊 Dashboard", "📝 Res. 0312", "📁 Documentos", "🔔 Alertas"])
    st.markdown("---")
    if st.button("Cerrar Sesión"):
        st.session_state['autenticado'] = False
        st.rerun()

# --- LÓGICA DE MÓDULOS ---
if menu == "📊 Dashboard":
    st.header("Tablero de Mandos SST")
    c1, c2, c3 = st.columns(3)
    c1.metric("Estándares Verificados", "18/60", "Faltan 42")
    c2.metric("Próxima Dotación", "Abril", "15 días")
    c3.metric("Comités", "Al día", "Marzo")
    
    st.divider()
    st.error("**ALERTA DE LEY:** Se requiere actualizar la firma de la política anual.")

elif menu == "📝 Res. 0312":
    st.header("Checklist: Resolución 0312")
    st.info("Seleccione los ítems cumplidos para el Grupo JPL")
    with st.container(border=True):
        st.checkbox("Asignación de Responsable (Licencia)")
        st.checkbox("Recursos Financieros")
        st.checkbox("Afiliación Social Integral")
        st.button("Actualizar Base de Datos")

elif menu == "📁 Documentos":
    st.header("Archivo Digital")
    st.file_uploader("Cargar RUT, CC o Actas", type=['pdf', 'jpg'])

elif menu == "🔔 Alertas":
    st.header("Tiempos de Notificación")
    st.slider("Días de pre-aviso (Dotación):", 1, 60, 30)
    st.slider("Días de pre-aviso (Comités):", 1, 15, 5)

# --- 5. FOOTER ---
st.markdown("---")
st.caption("Grupo JPL | Alianza MyM & Juan Prieto © 2026")