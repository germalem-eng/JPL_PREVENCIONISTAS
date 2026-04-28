import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="APP JPL - Soluciones MyM", page_icon="🛡️", layout="wide")

# Estilos CSS ( Vinotinto JPL y Dorado)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .frase-jpl {
        background-color: #1a1a1a; padding: 15px; border-radius: 8px;
        border-left: 5px solid #FFD700; margin-top: 10px;
    }
    .texto-dorado { color: #FFD700; font-style: italic; font-weight: bold; }
    [data-testid="stSidebar"] { background-color: #8B0000; color: white; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #1a1a1a; border-radius: 5px; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS REAL (7, 21 y 62 Estándares) ---
DATOS = {
    "Pequeña (1-10)": [
        {"id": "1", "titulo": "Asignación de persona que diseña el SG-SST", "subs": ["Acta de designación", "Hoja de vida", "Licencia en SST", "Curso 50 horas"], "f": "Garantiza que el SG-SST funcione correctamente.", "p": "Semestral"},
        {"id": "2", "titulo": "Afiliación al Sistema de Seguridad Social Integral", "subs": ["Planillas de pago mes a mes", "Verificación ausencia de moras", "Control de contratistas"], "f": "Protege al trabajador y evita sanciones.", "p": "Cuatrimestral"},
        {"id": "3", "titulo": "Capacitación en SST", "subs": ["Programa y cronograma", "Inducción/Reinducción", "Evidencias de asistencia"], "f": "Una empresa que capacita, previene errores.", "p": "Bimestral"},
        {"id": "4", "titulo": "Plan Anual de Trabajo", "subs": ["Objetivos y metas", "Cronograma de actividades", "Recursos firmados"], "f": "Planear es anticiparse al riesgo.", "p": "Anual"},
        {"id": "5", "titulo": "Evaluaciones Médicas Ocupacionales", "subs": ["Conceptos médicos", "Custodia de historias", "Seguimiento"], "f": "Cuidar la salud es proteger el activo.", "p": "Anual"},
        {"id": "6", "titulo": "Identificación de Peligros", "subs": ["Matriz GTC 45", "Participación trabajadores", "Medidas de control"], "f": "Identificar permite prevenir.", "p": "Semestral"},
        {"id": "7", "titulo": "Medidas de Prevención y Control", "subs": ["Mantenimiento equipos", "Entrega de EPP", "Actividades de control"], "f": "La prevención son resultados reales.", "p": "Anual"}
    ],
    "Mediana (11-50)": [
        {"id": str(i+1), "titulo": t, "subs": ["Soporte Documental", "Evidencia", "Validación"], "f": "Gestión organizada.", "p": "Trimestral"}
        for i, t in enumerate(["Asignación Responsable", "Recursos Financieros", "Afiliación SS", "COPASST", "COCOLA", "Capacitación", "Política SST", "Plan Trabajo", "Archivo", "Matriz Legal", "Evaluación Inicial", "Médicos", "Carcinógenos", "Reporte AT", "Peligros", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Auditoría", "Revisión"])
    ],
    "Grande (>50)": [
        {"id": str(i+1), "titulo": t, "subs": ["Requisito Legal", "Soporte Técnico", "Validación"], "f": "Excelencia operativa.", "p": "Mensual"}
        for i, t in enumerate(["Recursos Humanos", "Financieros", "Responsabilidades", "Seguridad Social", "Pago SS", "COPASST", "Capacitación COPASST", "COCOLA", "Capacitación COCOLA", "Programa Capacitación", "Inducción", "Curso 50h", "Política", "Objetivos", "Evaluación Inicial", "Plan Trabajo", "Rendición Cuentas", "Matriz Legal", "Comunicación", "Proveedores", "Gestión Cambio", "Sociodemográfica", "Médicos", "Seguimiento Médico", "Historias Clínicas", "Estilos Vida", "Carcinógenos", "Peligros", "Mediciones", "Controles", "Inspecciones", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Indicadores", "Auditoría", "Revisión", "Correctivas", "Mejora"])
    ]
}

# --- LÓGICA DE SESIÓN ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
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

# --- INTERFAZ DE PESTAÑAS ---
tab1, tab2, tab3, tab4 = st.tabs(["📋 Auditoría", "📊 Desempeño", "⏳ Cronograma", "🎥 Videos Premium"])

with tab1:
    st.header(f"Gestión: {cat}")
    cumplimiento_count, total_checks = 0, 0
    for item in DATOS[cat]:
        with st.expander(f"🔹 {item['id']}. {item['titulo']}"):
            for s in item['subs']:
                check = st.checkbox(s, key=f"c_{cat}_{item['id']}_{s}")
                total_checks += 1
                if check: cumplimiento_count += 1
            st.markdown(f'<div class="frase-jpl"><span class="texto-dorado">📌 {item["f"]}</span></div>', unsafe_allow_html=True)

with tab2:
    st.header("Análisis de Implementación")
    progreso = (cumplimiento_count / total_checks * 100) if total_checks > 0 else 0
    fig = px.pie(values=[progreso, 100-progreso], names=["Cumplido", "Pendiente"], color_discrete_sequence=['#FFD700', '#444444'], hole=.4)
    st.plotly_chart(fig)
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Reporte PDF")
    else:
        st.info("🔒 Descarga de reporte disponible en Versión Premium.")

with tab3:
    st.header("Cronograma de Trabajo")
    df_t = pd.DataFrame([{"Fase": "Diagnóstico", "Inicio": "2026-04-01", "Fin": "2026-04-15"}, {"Fase": "Diseño", "Inicio": "2026-04-16", "Fin": "2026-05-30"}])
    st.plotly_chart(px.timeline(df_t, x_start="Inicio", x_end="Fin", y="Fase", color="Fase"))

with tab4:
    st.header("Biblioteca Multimedia JPL")
    st.write("Videos de capacitación para tu empresa:")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Reemplazar con link real
    
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Video para Proyectar")
    else:
        st.warning("📺 Puedes ver los videos, pero la descarga es exclusiva para Clientes Premium.")

st.divider()
st.caption("Soluciones MyM - Proyecto L.I.N.A 2026")
