import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

# --- 2. ESTILOS INSTITUCIONALES (Vinotinto, Gris, Blanco y Negro) ---
st.markdown("""
<style>
    /* Sidebar Vinotinto profundo con letras blancas */
    [data-testid="stSidebar"] {
        background-color: #800000 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Fondo de la App */
    .stApp { background-color: #FFFFFF; }

    /* Encabezado Negro Estilo JPL */
    .app-header {
        padding: 15px; background-color: #000000;
        border-bottom: 4px solid #800000; color: #FFFFFF;
        text-align: center; font-size: 20px; font-weight: bold;
    }

    /* Línea de Tiempo PHVA */
    .phva-container {
        display: flex; justify-content: space-between;
        margin: 20px 0; padding: 20px;
        background-color: #f8f9fa; border-radius: 10px;
        border: 1px solid #ddd;
    }
    .step { text-align: center; flex: 1; }
    .circle {
        width: 50px; height: 50px; background-color: #800000;
        color: white; border-radius: 50%; display: flex;
        align-items: center; justify-content: center;
        margin: 0 auto 10px; font-weight: bold; font-size: 20px;
    }
    
    /* Botones de Redes Sociales */
    .social-btn {
        display: block; padding: 12px; margin: 8px 0;
        text-align: center; border-radius: 8px;
        text-decoration: none; font-weight: bold; color: white !important;
    }
    
    /* Estilo para los botones de compra */
    .buy-btn {
        display: inline-block; padding: 10px 20px;
        background-color: #800000; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. ACCESO AL SISTEMA ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### 🔐 INGRESO GRUPO JPL")
        u = st.text_input("Usuario:").strip().lower()
        p = st.text_input("Clave:", type="password").strip()
        if st.button("ACCEDER"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("Credenciales Incorrectas")
    st.stop()

# --- 4. BARRA LATERAL (MENÚ VINOTINTO) ---
with st.sidebar:
    st.markdown("## 🛡️ GRUPO JPL")
    st.markdown("---")
    menu = st.radio(
        "MENÚ DE GESTIÓN:",
        ["📊 Panel de Control", "🛡️ Evaluación 60 Ítems", "💰 Licencias de Uso", "🔔 Alertas de Ley"]
    )
    st.markdown("---")
    
    st.markdown("### 📱 CONTACTO DIRECTO")
    # Botones con iconos y colores oficiales
    st.markdown('<a href="https://wa.me/573016015891" class="social-btn" style="background-color: #25D366;">🟢 WhatsApp de Soporte</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://facebook.com/jplprevencionistas" class="social-btn" style="background-color: #1877F2;">🔵 Facebook Oficial</a>', unsafe_allow_html=True)
    
    st.markdown("---")
    if st.button("SALIR DEL SISTEMA"):
        st.session_state['autenticado'] = False
        st.rerun()

# --- 5. CONTENIDO POR MÓDULO ---
st.markdown('<div class="app-header">SISTEMA INTEGRAL DE GESTIÓN SST - GRUPO JPL</div>', unsafe_allow_html=True)

if menu == "📊 Panel de Control":
    st.header("📈 Ciclo de Mejora Continua (PHVA)")
    
    # Línea de Tiempo Visual
    st.markdown("""
    <div class="phva-container">
        <div class="step"><div class="circle">P</div><b>PLANEAR</b><br><small>Recursos y Políticas</small></div>
        <div class="step" style="color:#888; font-size: 30px; padding-top: 5px;">➔</div>
        <div class="step"><div class="circle">H</div><b>HACER</b><br><small>Gestión de Riesgos</small></div>
        <div class="step" style="color:#888; font-size: 30px; padding-top: 5px;">➔</div>
        <div class="step"><div class="circle">V</div><b>VERIFICAR</b><br><small>Auditoría Interna</small></div>
        <div class="step" style="color:#888; font-size: 30px; padding-top: 5px;">➔</div>
        <div class="step"><div class="circle">A</div><b>ACTUAR</b><br><small>Mejora Continua</small></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Estado de Clientes Actuales")
    col1, col2 = st.columns(2)
    col1.metric("Clientes en Gestión Directa", "32", "Gratis / Fidelizados")
    col2.info("💡 **Aviso:** Este sistema está configurado para la autogestión de nuevos clientes bajo licencia mensual.")

elif menu == "💰 Licencias de Uso":
    st.header("💳 Adquisición de Licencias Mensuales")
    st.write("Seleccione el tamaño de su empresa para activar el servicio:")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div style="border: 1px solid #ddd; padding: 15px; border-radius: 10px; text-align: center;">
            <h3>Pequeña</h3>
            <p>1 a 10 empleados</p>
            <h2 style="color: #800000;">$40.000</h2>
            <p>COP / Mes</p>
            <a href="https://wa.me/573016015891?text=Hola%20Grupo%20JPL,%20quiero%20adquirir%20la%20Licencia%20Pequeña%20($40k)" class="buy-btn">COMPRAR</a>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div style="border: 1px solid #800000; padding: 15px; border-radius: 10px; text-align: center; background-color: #fcfcfc;">
            <h3>Mediana</h3>
            <p>11 a 50 empleados</p>
            <h2 style="color: #800000;">$60.000</h2>
            <p>COP / Mes</p>
            <a href="https://wa.me/573016015891?text=Hola%20Grupo%20JPL,%20quiero%20adquirir%20la%20Licencia%20Mediana%20($60k)" class="buy-btn">COMPRAR</a>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div style="border: 1px solid #ddd; padding: 15px; border-radius: 10px; text-align: center;">
            <h3>Grande</h3>
            <p>Más de 51 empleados</p>
            <h2 style="color: #800000;">$100.000</h2>
            <p>COP / Mes</p>
            <a href="https://wa.me/573016015891?text=Hola%20Grupo%20JPL,%20quiero%20adquirir%20la%20Licencia%20Grande%20($100k)" class="buy-btn">COMPRAR</a>
        </div>
        """, unsafe_allow_html=True)

elif menu == "🛡️ Evaluación 60 Ítems":
    st.header("🛡️ Auditoría Resolución 0312")
    st.write("Control exhaustivo de estándares mínimos.")
    # Estructura simplificada para visualización
    st.multiselect("Filtrar por Ciclo:", ["Planear", "Hacer", "Verificar", "Actuar"])
    st.info("Módulo de carga de evidencias disponible para usuarios con licencia activa.")

elif menu == "🔔 Alertas de Ley":
    st.header("🔔 Calendario de Alertas Automáticas")
    st.error("🚨 **MENSUAL:** Recordatorio cierre de actas COPASST.")
    st.warning("⚠️ **CUATRIMESTRAL:** Revisión de indicadores de accidentalidad.")
    st.info("📅 **ANUAL:** Actualización de plan de capacitación.")
