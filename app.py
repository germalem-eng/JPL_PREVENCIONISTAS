import streamlit as st
import os

# --- 1. CONFIGURACIÓN E IDENTIDAD ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. ESTILO CORPORATIVO (SOLUCIÓN DE VISIBILIDAD) ---
st.markdown("""
    <style>
    /* 1. Ocultar solo el encabezado y pie de página de Streamlit */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {display: none !important;}

    /* 2. FORZAR QUE EL CONTENIDO SEA VISIBLE Y NO ESTÉ TAPADO */
    .main .block-container {
        padding-top: 2rem !important;
    }

    /* 3. Asegurar que el menú lateral (Sidebar) se vea */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        visibility: visible !important;
    }

    /* 4. Intentar ocultar los botones flotantes de la derecha */
    .stAppDeployButton {display: none !important;}
    </style>
    """, unsafe_allow_html=True)
# --- 3. BASE DE DATOS (7, 21 Y 60 ÍTEMS CON FRASES DE MOTIVACIÓN) ---
DATA_SST = {
    "📊 1-10 Trabajadores (Pequeña)": [
        {"id": "1.1", "item": "Responsable SG-SST", "q": "🛡️ 'El liderazgo es la base de una cultura segura.'"},
        {"id": "1.2", "item": "Seguridad Social", "q": "🛡️ 'La tranquilidad de tu equipo es la estabilidad de tu empresa.'"},
        {"id": "1.3", "item": "Capacitación", "q": "🛡️ 'Un trabajador entrenado es un trabajador protegido.'"},
        {"id": "1.4", "item": "Plan de Trabajo", "q": "🛡️ 'Planear hoy es prevenir mañana.'"},
        {"id": "1.5", "item": "Evaluaciones Médicas", "per": "Anual", "q": "🛡️ 'La salud es el activo más valioso.'"},
        {"id": "1.6", "item": "Peligros y Riesgos", "per": "Anual", "q": "🛡️ 'Identificar es el primer paso para controlar.'"},
        {"id": "1.7", "item": "Medidas de Control", "per": "Anual", "q": "🛡️ 'La prevención es una inversión, no un gasto.'"}
    ],
    "🏢 11-50 Trabajadores (Mediana)": [
        {"id": f"2.{i}", "item": f"Estándar Mediana {i}", "q": "🚀 'La mejora continua nos hace grandes.'"} for i in range(1, 22)
    ],
    "🏗️ +50 / Riesgo IV-V (Grande)": [
        {"id": f"3.{i}", "item": f"Estándar Superior {i}", "q": "🏆 'La excelencia en seguridad es nuestro estándar.'"} for i in range(1, 61)
    ]
}

# --- 4. BARRA LATERAL (LOGIN Y NAVEGACIÓN) ---
with st.sidebar:
    if os.path.exists("logo_jplfinal.jpg"):
        st.image("logo_jplfinal.jpg", use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>APLICACIÓN JPL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # LOGIN PARA DESCARGAS Y PREMIUM
    st.markdown("### 🔑 Acceso Premium")
    pass_user = st.text_input("Contraseña Cliente:", type="password")
    is_premium = (pass_user == "JPL2026")
    
    st.markdown("---")
    opciones = ["🏠 Inicio", "📊 1-10 Trabajadores (Pequeña)", "🏢 11-50 Trabajadores (Mediana)", "🏗️ +50 / Riesgo IV-V (Grande)", "💎 Contenido Premium"]
    menu = st.radio("Menú Principal:", opciones)
    st.caption("Soluciones MyM | L.I.N.A.")

# --- 5. LÓGICA DE CONTENIDO ---
if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL.")
    st.info("Utilice el menú lateral para navegar. Las funciones de descarga requieren acceso Premium.")

elif menu == "💎 Contenido Premium":
    if is_premium:
        st.header("💎 Zona de Descargas y Recursos")
        st.success("Acceso Concedido")
        st.button("📥 Descargar Estadísticas Globales (PDF)")
        st.button("📄 Descargar Plan de Mejora")
    else:
        st.markdown("<div class='premium-lock'><h3>🔓 Contenido Bloqueado</h3><p>Ingrese su clave en el panel lateral para descargar sus reportes.</p></div>", unsafe_allow_html=True)

else:
    # SECCIÓN DE EVALUACIÓN
    st.header(f"Sección: {menu}")
    
    # --- LÍNEA DE TIEMPO / ESTADÍSTICA EN TIEMPO REAL ---
    items = DATA_SST.get(menu, [])
    total = len(items)
    
    # Inicializar estado si no existe
    if 'respuestas' not in st.session_state: st.session_state.respuestas = {}
    
    cumple = 0
    for i in range(total):
        key = f"{menu}_{i}"
        if key in st.session_state.respuestas and st.session_state.respuestas[key] == "Cumple":
            cumple += 1
            
    progreso = (cumple / total) if total > 0 else 0
    
    st.subheader("📈 Línea de Cumplimiento en Tiempo Real")
    st.progress(progreso)
    st.write(f"Cumplimiento actual: **{round(progreso*100, 1)}%**")
    
    if progreso < 0.5: st.warning("⚠️ El cumplimiento está por debajo del estándar mínimo.")
    
    st.markdown("---")

    # MOSTRAR ÍTEMS CON MOTIVACIÓN
    for i, it in enumerate(items):
        with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
            # Frase de motivación del Word
            st.markdown(f"<div class='motivation-box'>{it['q']}</div>", unsafe_allow_html=True)
            
            c1, c2 = st.columns([2, 1])
            with c1:
                st.text_area("Evidencia observada", key=f"obs_{it['id']}_{menu}")
            with c2:
                estado = st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple"], key=f"sel_{it['id']}_{menu}")
                st.session_state.respuestas[f"{menu}_{i}"] = estado

    # ALERTAS ESPECIALES (Solo para la Grande, pero el login es para todas)
    if "Grande" in menu:
        st.sidebar.markdown("---")
        st.sidebar.error("🚨 ALERTAS: Contabilidad / Ambiental")
