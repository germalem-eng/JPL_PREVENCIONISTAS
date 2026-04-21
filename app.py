import streamlit as st
import os

# --- 1. CONFIGURACIÓN E IDENTIDAD ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. ESTILO CORPORATIVO AVANZADO (L.I.N.A. Engine) ---
st.markdown("""
    <style>
    /* 1. Fondo y Tipografía General */
    .stApp {
        background-color: #D9D9D9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 2. Barra Lateral (Sidebar) Personalizada */
    [data-testid="stSidebar"] {
        background-color: #8B0000 !important; /* Vinotinto */
        border-right: 5px solid #1A1A1A; /* Negro */
    }
    
    /* Color de texto en Sidebar */
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: white !important;
    }

    /* 3. Ocultar menús de "Página Web" para que parezca App Nativa */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 4. Tarjetas de Ítems (Expanders) */
    .stExpander {
        background-color: white !important;
        border-radius: 15px !important;
        border: 1px solid #1A1A1A !important;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1) !important;
        margin-bottom: 15px !important;
    }

    /* 5. Frases de Motivación (Diseño especial) */
    .motivation-box {
        background: linear-gradient(90deg, #8B0000 0%, #1A1A1A 100%);
        color: #FFD700 !important; /* Dorado */
        padding: 15px;
        border-radius: 10px;
        font-style: italic;
        margin-bottom: 15px;
        border-left: 8px solid #FFD700;
        font-weight: 500;
    }

    /* 6. Botones Premium y Formularios */
    .stButton>button {
        background-color: #1A1A1A !important;
        color: #FFD700 !important;
        border: 2px solid #FFD700 !important;
        border-radius: 10px !important;
        width: 100%;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #FFD700 !important;
        color: #1A1A1A !important;
    }

    /* 7. Barra de Progreso (Línea de Tiempo) */
    .stProgress > div > div > div > div {
        background-color: #8B0000 !important;
    }

    /* 8. Zona Premium Bloqueada */
    .premium-lock {
        background-color: #1A1A1A;
        color: #FFD700;
        padding: 30px;
        border-radius: 20px;
        border: 3px solid #8B0000;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
    }
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
    st.title("Bienvenido a APP JPL")
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
