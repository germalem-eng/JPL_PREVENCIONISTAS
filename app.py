import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="APP JPL - Soluciones MyM", page_icon="🛡️", layout="wide")

# --- ESTILOS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .frase-jpl {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #FFD700;
        margin-top: 10px;
    }
    .texto-dorado { color: #FFD700; font-style: italic; font-weight: bold; }
    [data-testid="stSidebar"] { background-color: #8B0000; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS ESTRUCTURADA ---
# Categoría 1: 7 Estándares
P_7 = [
    {"id": "1", "titulo": "Asignación de diseñador SG-SST", "subs": ["Acta de designación", "Hoja de vida", "Licencia SST", "Curso 50 horas"], "f": "Contar con una persona competente garantiza que el sistema funcione.", "p": "Semestral"},
    {"id": "2", "titulo": "Afiliación Seguridad Social", "subs": ["Planillas de pago", "Verificación de moras", "Control contratistas"], "f": "La afiliación protege al trabajador y evita sanciones.", "p": "Cuatrimestral"},
    {"id": "3", "titulo": "Capacitación en SST", "subs": ["Programa y Cronograma", "Inducción/Reinducción", "Evidencias"], "f": "Una empresa que capacita previene errores.", "p": "Bimestral"},
    {"id": "4", "titulo": "Plan Anual de Trabajo", "subs": ["Objetivos y metas", "Cronograma", "Recursos firmados"], "f": "Planear es anticiparse al riesgo.", "p": "Anual"},
    {"id": "5", "titulo": "Evaluaciones Médicas", "subs": ["Exámenes ingreso/egreso", "Custodia historias", "Seguimiento"], "f": "Cuidar la salud es proteger el activo más importante.", "p": "Anual"},
    {"id": "6", "titulo": "Identificación de Peligros", "subs": ["Matriz de riesgos", "Participación empleados", "Controles"], "f": "Identificar riesgos permite prevenir accidentes.", "p": "Semestral"},
    {"id": "7", "titulo": "Medidas de Prevención", "subs": ["Ejecución actividades", "Mantenimiento", "Entrega EPP"], "f": "La prevención se convierte en resultados reales.", "p": "Anual"}
]

# Categoría 2: 21 Estándares
M_21 = [
    {"id": str(i+1), "titulo": t, "subs": ["Documento soporte", "Registro ejecución", "Validación"], "f": "Gestión organizada para evitar riesgos.", "p": "Trimestral"}
    for i, t in enumerate([
        "Asignación Responsable", "Recursos Financieros", "Afiliación", "COPASST", "COCOLA", "Capacitación",
        "Política SST", "Plan Trabajo", "Archivo", "Matriz Legal", "Evaluación Inicial", "Evaluaciones Médicas",
        "Carcinógenos", "Reporte AT/EL", "Identificación Peligros", "Mantenimiento", "EPP", "Plan Emergencias",
        "Brigada", "Auditoría", "Revisión Gerencial"
    ])
]

# Categoría 3: 62 Estándares
G_62 = []
nombres_62 = [
    "Asignación Diseñador", "Asignación Responsabilidades", "Asignación Recursos", "Seguridad Social",
    "Alto Riesgo", "COPASST", "COCOLA", "Capacitación", "Inducción", "Política", "Objetivos", 
    "Evaluación Inicial", "Plan Trabajo", "Archivo", "Rendición Cuentas", "Matriz Legal", 
    "Comunicación", "Proveedores", "Gestión Cambio", "Sociodemográfica", "Medicina Trabajo"
]
for i in range(62):
    nombre = nombres_62[i] if i < len(nombres_62) else f"Estándar N° {i+1}"
    G_62.append({
        "id": str(i+1), "titulo": nombre, "subs": ["Evidencia", "Firma", "Soporte"], "f": "La excelencia en SST es productividad.", "p": "Mensual"
    })

DATOS = {"Pequeña (1-10)": P_7, "Mediana (11-50)": M_21, "Grande (>50)": G_62}

# --- LOGICA USUARIO ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=150)
    st.title("🛡️ Panel JPL")
    correo = st.text_input("Correo del Cliente")
    if st.button("Validar Acceso"):
        if correo in ["natalia@jpl.com", "jhuan@jpl.com", "gerardo@mym.com"]:
            st.session_state.user_type = "premium"
            st.success("Acceso Premium")
        else:
            st.session_state.user_type = "invitado"
            st.info("Modo Invitado")
    
    st.divider()
    cat = st.selectbox("Categoría de Empresa", list(DATOS.keys()))

# --- INTERFAZ ---
st.header(f"Gestión: {cat}")
st.write(f"Estado: **{st.session_state.user_type.upper()}**")

for item in DATOS[cat]:
    with st.expander(f"📌 {item['id']}. {item['titulo']}"):
        st.caption(f"Periodicidad: {item['p']}")
        checks = [st.checkbox(s, key=f"c_{cat}_{item['id']}_{s}") for s in item['subs']]
        
        if all(checks): st.success("✅ Cumplimiento Total")
        elif any(checks): st.warning("⚠️ Parcial - Falta evidencia")
        else: st.error("🚨 Sin gestión")
        
        st.markdown(f'<div class="frase-jpl"><span class="texto-dorado">📌 {item["f"]}</span></div>', unsafe_allow_html=True)

# --- PREMIUM ---
st.divider()
st.subheader("💎 Funciones Premium")
c1, c2 = st.columns(2)

with c1:
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Reporte PDF")
    else:
        st.button("🔒 PDF Bloqueado", disabled=True)

with c2:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Video")
    else:
        st.warning("Descarga solo para Premium.")
