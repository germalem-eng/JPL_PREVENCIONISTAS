import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN E IMAGEN CORPORATIVA ---
st.set_page_config(page_title="JPL Prevencionistas - Auditoría SG-SST", layout="wide")

# Colores institucionales: Vinotinto (#800000), Gris claro (#F0F2F6), Blanco y Dorado (#FFD700)
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    .stTabs [data-baseweb="tab-list"] { background-color: #800000; }
    .stTabs [data-baseweb="tab"] { color: white; }
    
    .stExpander { background-color: #F0F2F6 !important; border-radius: 10px; border: 1px solid #D1D1D1; }
    
    .frase-dorada {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #FFD700;
        color: #FFD700;
        font-weight: bold;
        font-style: italic;
        margin: 10px 0;
    }
    
    .texto-vinotinto { color: #800000; font-weight: bold; }
    h1, h2, h3 { color: #800000; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS ESTRUCTURADA (Sin restricciones de 7, 21 y 62) ---
DATOS = {
    "Pequeña (7 Estándares)": [
        {"id": "1", "titulo": "Asignación de persona que diseña el SG-SST", "items": ["Acta de designación", "Hoja de vida", "Licencia SST", "Curso 50h"], "frase": "📌 Contar con una persona competente garantiza que el sistema funcione correctamente y prevenga riesgos que pueden afectar a toda la empresa."},
        {"id": "2", "titulo": "Afiliación al Sistema de Seguridad Social Integral", "items": ["Planillas mes a mes", "Verificación de moras", "Control contratistas"], "frase": "📌 Una afiliación adecuada protege al trabajador y evita responsabilidades económicas para la empresa."},
        {"id": "3", "titulo": "Capacitación en SST", "items": ["Cronograma", "Inducciones", "Evidencias asistencia"], "frase": "📌 Una empresa que capacita, previene errores humanos y fortalece la cultura de seguridad en todos los niveles."},
        {"id": "4", "titulo": "Plan Anual de Trabajo", "items": ["Objetivos/Metas", "Cronograma", "Recursos firmados"], "frase": "📌 Planear es anticiparse; un plan bien estructurado es la hoja de ruta hacia una empresa segura."},
        {"id": "5", "titulo": "Evaluaciones Médicas Ocupacionales", "items": ["Conceptos ingreso/egreso", "Historias clínicas", "Seguimiento"], "frase": "📌 Cuidar la salud de los trabajadores es proteger el activo más importante y asegurar la continuidad del negocio."},
        {"id": "6", "titulo": "Identificación de Peligros y Valoración de Riesgos", "items": ["Matriz GTC 45", "Participación trabajadores", "Controles"], "frase": "📌 Identificar los peligros a tiempo evita que un incidente se convierta en una tragedia."},
        {"id": "7", "titulo": "Medidas de Prevención y Control", "items": ["Mantenimiento", "Entrega EPP", "Inspecciones"], "frase": "📌 La prevención es una inversión que se traduce en productividad y bienestar para todos."}
    ],
    "Mediana (21 Estándares)": [
        # Aquí se desglosan los 21 ítems técnicos (COPASST, COCOLA, Brigadas, etc.)
        {"id": str(i+1), "titulo": t, "items": ["Soporte Documental", "Registro Ejecución"], "frase": "📌 La gestión técnica detallada es el escudo ante auditorías legales."}
        for i, t in enumerate(["Asignación Responsable", "Recursos", "Afiliación", "COPASST", "COCOLA", "Capacitación", "Política SST", "Plan Trabajo", "Archivo", "Matriz Legal", "Evaluación Inicial", "Plan Mejora", "Evaluaciones Médicas", "Reporte AT/EL", "Investigación Incidentes", "Identificación Peligros", "Mantenimiento", "Entrega EPP", "Plan Emergencias", "Brigadas", "Revisión Gerencial"])
    ],
    "Grande (62 Estándares)": [
        # Estructura para los 62 estándares con sus respectivos desgloses
        {"id": str(i+1), "titulo": t, "items": ["Evidencia Técnica", "Validación ARL"], "frase": "📌 La excelencia en el cumplimiento posiciona a la empresa en el más alto nivel nacional."}
        for i, t in enumerate(["Recursos Humanos", "Financieros", "Responsabilidades", "Seguridad Social", "Pago SS", "COPASST", "Capacitación COPASST", "COCOLA", "Capacitación COCOLA", "Programa Capacitación", "Inducción", "Curso 50h", "Política", "Objetivos", "Evaluación Inicial", "Plan Trabajo", "Rendición Cuentas", "Matriz Legal", "Comunicación", "Proveedores", "Gestión Cambio", "Sociodemográfica", "Médicos", "Seguimiento Médico", "Historias Clínicas", "Estilos Vida", "Carcinógenos", "Peligros", "Mediciones", "Controles", "Inspecciones", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Indicadores", "Auditoría", "Revisión", "Correctivas", "Mejora", "Otros ítems de cumplimiento"])
    ]
}

# --- LÓGICA DE USUARIO ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.title("🛡️ Panel de Auditoría")
    correo = st.text_input("Usuario (Correo)")
    if st.button("Ingresar"):
        if correo in ["natalia@jpl.com", "jhuan@jpl.com", "gerardo@mym.com"]:
            st.session_state.user_type = "premium"
            st.success("Acceso Premium")
        else:
            st.session_state.user_type = "invitado"
    
    st.divider()
    cat = st.selectbox("Categoría de Empresa", list(DATOS.keys()))

# --- INTERFAZ ---
tab1, tab2, tab3 = st.tabs(["📋 Auditoría y Evidencias", "📊 Desempeño Real", "🎥 Capacitación"])

cumplimiento_pts, total_pts = 0, 0

with tab1:
    st.header(f"Gestión de Estándares: {cat}")
    for item in DATOS[cat]:
        with st.expander(f"🔹 {item['id']}. {item['titulo']}"):
            st.markdown(f'<div class="frase-dorada">{item["frase"]}</div>', unsafe_allow_html=True)
            
            puntos_item = 0
            for sub in item['items']:
                total_pts += 1
                col1, col2 = st.columns([1, 2])
                with col1:
                    sel = st.radio(f"¿Cumple con {sub}?", ["No", "Sí"], key=f"r_{cat}_{item['id']}_{sub}")
                with col2:
                    if sel == "Sí":
                        st.file_uploader(f"Subir soporte: {sub}", key=f"f_{cat}_{item['id']}_{sub}")
                        cumplimiento_pts += 1
                        puntos_item += 1
                    else:
                        st.error("🚨 DOCUMENTO PENDIENTE")
            
            # Alerta final del ítem
            if puntos_item == len(item['items']):
                st.success("✅ COMPLETO")
            elif puntos_item > 0:
                st.warning("⚠️ EN PROCESO")
            else:
                st.error("🚨 INCUMPLIMIENTO")

with tab2:
    st.header("Estadísticas de Cumplimiento")
    progreso = (cumplimiento_pts / total_pts * 100) if total_pts > 0 else 0
    fig = px.pie(values=[progreso, 100-progreso], names=["Soportado", "Pendiente"], 
                 color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
    st.plotly_chart(fig)
    st.metric("Implementación Actual", f"{int(progreso)}%")

with tab3:
    st.header("Multimedia y Capacitación")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Reporte Final PDF")

st.divider()
st.caption("Soluciones MyM - Innovación para JPL Prevencionistas SAS")
