import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="APP JPL - Soluciones MyM", page_icon="🛡️", layout="wide")

# Forzar lectura de manifiesto para el logo (Solución al barquito rojo)
st.markdown('<link rel="manifest" href="https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/manifest.json">', unsafe_allow_html=True)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { color: white; }
    .st-emotion-cache-16idsys p { font-size: 1.1rem; }
    .frase-jpl {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #FFD700;
        margin-top: 10px;
    }
    .texto-dorado { color: #FFD700; font-style: italic; font-weight: bold; }
    [data-testid="stSidebar"] { background-color: #8B0000; } /* Rojo JPL */
    .stButton>button { width: 100%; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS (MUESTRA ESTRUCTURADA DE TUS DOCS) ---
# Aquí organizamos los sub-ítems que disparan las alertas
DATOS_SST = {
    "Pequeña (1-10)": [
        {
            "id": "1.1",
            "titulo": "Asignación de persona que diseña el SG-SST",
            "sub_items": ["Acta de designación", "Hoja de Vida", "Licencia SST Vigente", "Curso 50 Horas"],
            "motivacion": "Contar con una persona competente garantiza que el SG-SST funcione y prevenga riesgos.",
            "periodo": "Semestral"
        },
        {
            "id": "1.2",
            "titulo": "Afiliación al Sistema de Seguridad Social Integral",
            "sub_items": ["Planillas de pago al día", "Ausencia de moras ARL/EPS", "Control de contratistas"],
            "motivacion": "Una afiliación adecuada protege al trabajador y evita sanciones económicas.",
            "periodo": "Cuatrimestral"
        }
    ],
    "Mediana (11-50)": [
        # Aquí se cargan los 21 ítems de tu segundo Word
        {"id": "2.1", "titulo": "Asignación de responsabilidades en SST", "sub_items": ["Rep. Legal", "Responsable SST", "COPASST", "Brigada"], "motivacion": "Definir responsabilidades claras permite una gestión organizada.", "periodo": "Cuatrimestral"}
    ],
    "Grande (>50 o Riesgo IV/V)": [
        # Aquí se cargan los 62 ítems de tu tercer Word
        {"id": "3.1", "titulo": "Recursos para el Sistema de Gestión", "sub_items": ["Presupuesto Técnico", "Recurso Humano", "Acta Firmada Gerencia"], "motivacion": "La asignación adecuada de recursos garantiza la ejecución del sistema.", "periodo": "Trimestral"}
    ]
}

# --- LÓGICA DE USUARIO ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.tipo_usuario = "invitado"

# --- MENÚ LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=150)
    st.title("Acceso Clientes")
    
    email = st.text_input("Correo Electrónico")
    if st.button("Validar Ingreso (Tipo Banco)"):
        # Lista de tus 32 clientes (simulada aquí)
        clientes_premium = ["natalia@jpl.com", "gerardo@mym.com"] 
        if email in clientes_premium:
            st.session_state.autenticado = True
            st.session_state.tipo_usuario = "premium"
            st.success(f"Bienvenido Cliente Premium")
        else:
            st.session_state.autenticado = True
            st.session_state.tipo_usuario = "invitado"
            st.info("Ingresando como Invitado")

    st.divider()
    categoria = st.selectbox("Seleccione Categoría de Empresa", list(DATOS_SST.keys()))

# --- CUERPO PRINCIPAL ---
st.title(f"Gestión SST - {categoria}")
st.write(f"Modo: **{st.session_state.tipo_usuario.upper()}**")

# Mapeo de la categoría seleccionada
items_a_mostrar = DATOS_SST[categoria]

# Barra de cumplimiento general
cumplimiento_total = 0
total_subs = 0

for item in items_a_mostrar:
    with st.expander(f"🔹 {item['id']} - {item['titulo']}"):
        st.caption(f"Periodicidad: {item['periodo']}")
        
        # Checklist de sub-ítems
        checks = []
        for sub in item['sub_items']:
            c = st.checkbox(sub, key=f"check_{item['id']}_{sub}")
            checks.append(c)
            total_subs += 1
            if c: cumplimiento_total += 1
        
        # Alerta dinámica dentro del ítem
        progreso_item = sum(checks) / len(checks)
        if progreso_item == 1.0:
            st.success("✅ Cumplimiento Total")
        elif progreso_item > 0:
            st.warning(f"⚠️ Parcial: {int(progreso_item*100)}% - Falta documentación")
        else:
            st.error("🚨 Alerta: Sin registros de cumplimiento")
            
        # Frase Motivacional Estilo JPL
        st.markdown(f"""
            <div class="frase-jpl">
                <span class="texto-dorado">📌 {item['motivacion']}</span>
            </div>
        """, unsafe_allow_html=True)

# --- SECCIÓN PREMIUM (MONETIZACIÓN) ---
st.divider()
st.header("💎 Zona de Descargas y Multimedia")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Reportes en PDF")
    if st.session_state.tipo_usuario == "premium":
        st.button("📥 Descargar Informe Completo (PDF)")
    else:
        st.button("🔒 Descargar Reporte (Solo Premium)", disabled=True)
        st.info("Los invitados pueden ver alertas pero no descargar el reporte legal.")

with col2:
    st.subheader("Capacitación (Videos)")
    # Simulación de video de TikTok/YouTube
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Reemplazar por link real de JPL
    
    if st.session_state.tipo_usuario == "premium":
        st.button("📥 Descargar Video para Proyectar")
    else:
        st.warning("Hazte Premium para descargar material de apoyo.")

# Pie de página
st.markdown("---")
st.caption("Desarrollado por Soluciones MyM - Proyecto L.I.N.A 2026")
