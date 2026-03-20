import streamlit as st
import os
import base64
from datetime import datetime

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA | Gestión MyM", layout="wide")

def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# RUTAS DE IDENTIDAD (Asegúrese de tener sus archivos en Logos/)
logo_original_b64 = get_base64("Logos/Logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 2. ESTILOS Y RELOJ DINÁMICO (JP/JS) ---
st.html(f"""
<style>
    /* Forzado de Modo Claro y Fondo MyM */
    .stApp {{
        background-color: #ffffff !important;
        background-image: linear-gradient(rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0.96)), 
                          url("data:image/jpeg;base64,{fondo_b64}") !important;
        background-size: cover !important;
    }}

    /* BARRA PLATEADA SUPERIOR (LIMPIA) */
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 8px 40px; background: linear-gradient(180deg, #f5f5f5 0%, #cccccc 100%) !important;
        border-bottom: 3px solid #999; box-shadow: 0px 3px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }}

    #reloj-live {{
        font-family: 'Courier New', monospace; font-weight: bold; color: #1a1a1a; 
        font-size: 15px; background: rgba(255,255,255,0.7); padding: 5px 15px;
        border-radius: 4px; border: 1px solid #888;
    }}

    .social-btn {{
        background: #ffffff; color: #1a1a1a !important; padding: 5px 15px; 
        border-radius: 4px; text-decoration: none; font-weight: bold; 
        margin-left: 10px; font-size: 11px; border: 1px solid #999;
        font-family: sans-serif;
    }}
    
    .social-btn:hover {{ background: #00d4ff; color: white !important; }}

    /* CABECERA: LOGO ORIGINAL MyM 2007 */
    .cabecera-fila {{ display: flex; align-items: center; gap: 45px; padding: 20px 50px; }}
    .logo-original {{
        width: 280px; height: 280px; border-radius: 50% !important;
        border: 5px solid #00d4ff !important; 
        box-shadow: 0px 10px 25px rgba(0,0,0,0.1) !important;
        object-fit: cover;
    }}
    
    h1, h2, p, label {{ font-family: 'Comic Sans MS', cursive !important; color: #1a1a1a !important; }}
</style>

<script>
    function actualizarReloj() {{
        const ahora = new Date();
        const fecha = ahora.toLocaleDateString('es-CO');
        const hora = ahora.toLocaleTimeString('es-CO', {{ hour12: false }});
        document.getElementById('reloj-live').innerHTML = "📅 " + fecha + " | 🕒 " + hora;
    }}
    setInterval(actualizarReloj, 1000);
</script>
""")

# --- 3. BARRA PLATEADA (SISTEMA ACTIVO) ---
st.html(f"""
<div class="nav-bar-silver">
    <div id="reloj-live">Sincronizando L.I.N.A...</div>
    <div>
        <a href="#" class="social-btn">FACEBOOK</a>
        <a href="#" class="social-btn">INSTAGRAM</a>
        <a href="#" class="social-btn">TIKTOK</a>
        <a href="#" class="social-btn">YOUTUBE</a>
        <a href="https://wa.me/573000000000" class="social-btn" style="color: #128C7E; border-color: #128C7E;">WHATSAPP</a>
    </div>
</div>
""")

# --- 4. CABECERA IDENTIDAD MyM ---
logo_html = f'<img src="data:image/jpeg;base64,{logo_original_b64}" class="logo-original">' if logo_original_b64 else ""
st.html(f"""
<div class="cabecera-fila">
    {logo_html}
    <div>
        <h1 style="font-size: 100px; text-shadow: 4px 4px 0px #00d4ff; margin: 0; line-height: 0.8;">L.I.N.A.</h1>
        <p style="font-size: 18px; font-weight: bold; margin-top: 15px;">LABORATORIO DE INTELIGENCIA Y NUEVOS ALGORITMOS</p>
        <h2 style="color: #008fb3 !important; font-size: 20px; border-top: 1.5px solid #00d4ff; display: inline-block; padding-top: 8px;">
            🛠️ SOLUCIONES TECNOLÓGICAS M & M | DESDE 2007
        </h2>
    </div>
</div>
""")

st.markdown("---")

# --- 5. PANEL OPERATIVO (ESTADO ANTERIOR RESTAURADO) ---
tab1, tab2, tab3 = st.tabs(["📊 COMERCIAL", "📂 REPOSITORIO DE IMÁGENES", "🛒 VENTAS"])

with tab1:
    col_a, col_b = st.columns([1.5, 1])
    with col_a:
        with st.container(border=True):
            st.subheader("Cotizador")
            st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Técnica", "Creación Web/App"])
            st.text_input("Equipo / Marca:")
            st.button("Generar Cotización")
    with col_b:
        with st.container(border=True):
            st.subheader("Agendamiento")
            st.date_input("Fecha Tentativa:")
            st.text_area("Descripción detallada del requerimiento:", height=100)
            st.button("🚀 Enviar Solicitud a L.I.N.A.")

with tab2:
    st.subheader("📂 Registro Visual de Servicios")
    st.write("Galería técnica de proyectos y reparaciones.")
    col_img1, col_img2, col_img3 = st.columns(3)
    with col_img1: st.info("🔧 Mantenimiento PC/Servidor")
    with col_img2: st.success("💻 Software & Algoritmos")
    with col_img3: st.warning("🤖 Hardware Robótica")
    
    st.divider()
    st.write("**Cargar nueva evidencia técnica:**")
    st.file_uploader("Subir foto de trabajo realizado", type=['jpg', 'png'])

with tab3:
    st.subheader("Tienda MyM: Equipos Disponibles")
    st.metric(label="HP Compaq dc5800 (Refurbished)", value="$1,150,000 COP")
    st.write("Optimizado para alto rendimiento y durabilidad.")

# --- 6. FOOTER ---
st.markdown("---")
st.caption(f"L.I.N.A. V20.0 | Ingeniería de Soluciones Tecnológicas M & M © 2026")