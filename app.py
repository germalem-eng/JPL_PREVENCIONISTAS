import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="APP JPL - Soluciones MyM", page_icon="🛡️", layout="wide")

# Estilos CSS (Rojo JPL y Dorado)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .frase-jpl {
        background-color: #1a1a1a; padding: 15px; border-radius: 8px;
        border-left: 5px solid #FFD700; margin-top: 10px;
    }
    .texto-dorado { color: #FFD700; font-style: italic; font-weight: bold; }
    [data-testid="stSidebar"] { background-color: #8B0000; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS REAL (7, 21 y 62 Estándares) ---
DATOS = {
    "Pequeña (1-10)": [
        {"id": "1", "titulo": "Asignación de persona que diseña el SG-SST", "subs": ["Acta de designación", "Hoja de vida", "Licencia en SST", "Curso 50 horas"], "f": "Garantiza que el SG-SST funcione correctamente.", "p": "Semestral"},
        {"id": "2", "titulo": "Afiliación al Sistema de Seguridad Social Integral", "subs": ["Planillas de pago mes a mes", "Verificación ausencia de moras", "Control de contratistas"], "f": "Protege al trabajador y evita sanciones económicas.", "p": "Cuatrimestral"},
        {"id": "3", "titulo": "Capacitación en SST", "subs": ["Programa y cronograma", "Inducción/Reinducción", "Evidencias (asistencia/evaluación)"], "f": "Una empresa que capacita, previene errores humanos.", "p": "Bimestral"},
        {"id": "4", "titulo": "Plan Anual de Trabajo", "subs": ["Objetivos y metas", "Cronograma de actividades", "Recursos (financieros/técnicos)"], "f": "Planear es anticiparse al riesgo.", "p": "Anual"},
        {"id": "5", "titulo": "Evaluaciones Médicas Ocupacionales", "subs": ["Conceptos médicos", "Custodia de historias", "Seguimiento a recomendaciones"], "f": "Cuidar la salud es proteger el activo más importante.", "p": "Anual"},
        {"id": "6", "titulo": "Identificación de Peligros y Valoración de Riesgos", "subs": ["Matriz de riesgos", "Participación de trabajadores", "Medidas de control"], "f": "Identificar riesgos permite prevenir accidentes.", "p": "Semestral"},
        {"id": "7", "titulo": "Medidas de Prevención y Control", "subs": ["Ejecución de actividades", "Mantenimiento de equipos", "Entrega de EPP"], "f": "La prevención se convierte en resultados reales.", "p": "Anual"}
    ],
    "Mediana (11-50)": [
        {"id": str(i+1), "titulo": t, "subs": ["Soporte Documental", "Evidencia de Ejecución", "Validación Responsable"], "f": "La gestión organizada evita riesgos.", "p": "Trimestral"}
        for i, t in enumerate([
            "Asignación Responsable", "Recursos Financieros", "Afiliación SS", "COPASST", "COCOLA", "Capacitación",
            "Política SST", "Plan Trabajo", "Archivo Documental", "Matriz Legal", "Evaluación Inicial", 
            "Evaluaciones Médicas", "Carcinógenos", "Reporte AT/EL", "Identificación Peligros", "Mantenimiento", 
            "Entrega EPP", "Plan Emergencias", "Brigada", "Auditoría", "Revisión Gerencial"
        ])
    ],
    "Grande (>50)": [
        {"id": str(i+1), "titulo": t, "subs": ["Requisito Legal", "Soporte Técnico", "Validación Gerencia"], "f": "La excelencia en SST protege la productividad.", "p": "Mensual"}
        for i, t in enumerate([
            "Recursos Humanos", "Recursos Financieros", "Asignación Responsabilidades", "Afiliación SS", "Pago SS",
            "Conformación COPASST", "Capacitación COPASST", "Conformación COCOLA", "Capacitación COCOLA", "Programa Capacitación",
            "Inducción y Reinducción", "Curso 50h", "Política SST", "Objetivos SST", "Evaluación Inicial", "Plan de Trabajo",
            "Rendición Cuentas", "Matriz Legal", "Mecanismos Comunicación", "Archivo Documental", "Proveedores y Contratistas",
            "Gestión del Cambio", "Descripción Sociodemográfica", "Evaluaciones Médicas", "Seguimiento Médico", "Historias Clínicas",
            "Estilos Vida Saludable", "Sustancias Carcinógenas", "Identificación de Peligros", "Mediciones Ambientales",
            "Medidas de Control", "Inspecciones", "Mantenimiento Equipos", "Entrega de EPP", "Plan de Emergencias", "Brigada de Emergencia",
            "Indicadores SST", "Auditoría Anual", "Revisión Gerencial", "Acciones Correctivas", "Acciones de Mejora"
            # Se puede extender hasta los 62 completos según el Word
        ])
    ]
}

# --- LOGICA USUARIO ---
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

# --- INTERFAZ ---
tab1, tab2, tab3 = st.tabs(["📋 Auditoría SST", "📊 Gráficas", "⏳ Cronograma"])

with tab1:
    st.header(f"Gestión: {cat}")
    cumplimiento_count = 0
    total_checks = 0
    
    for item in DATOS[cat]:
        with st.expander(f"🔹 {item['id']}. {item['titulo']}"):
            st.caption(f"Vigencia: {item['p']}")
            for s in item['subs']:
                check = st.checkbox(s, key=f"c_{cat}_{item['id']}_{s}")
                total_checks += 1
                if check: cumplimiento_count += 1
            
            st.markdown(f'<div class="frase-jpl"><span class="texto-dorado">📌 {item["f"]}</span></div>', unsafe_allow_html=True)

with tab2:
    st.header("Análisis de Desempeño")
    progreso = (cumplimiento_count / total_checks * 100) if total_checks > 0 else 0
    
    fig = px.pie(values=[progreso, 100-progreso], names=["Cumplido", "Pendiente"],
                 color_discrete_sequence=['#FFD700', '#444444'], title="Porcentaje de Implementación")
    st.plotly_chart(fig)

with tab3:
    st.header("Línea de Tiempo de Ejecución")
    df_t = pd.DataFrame([
        {"Fase": "Diagnóstico", "Inicio": "2026-04-01", "Fin": "2026-04-15"},
        {"Fase": "Diseño", "Inicio": "2026-04-16", "Fin": "2026-05-30"},
        {"Fase": "Ejecución", "Inicio": "2026-06-01", "Fin": "2026-12-31"}
    ])
    fig_g = px.timeline(df_t, x_start="Inicio", x_end="Fin", y="Fase", color="Fase")
    st.plotly_chart(fig_g)

# --- PREMIUM ---
st.divider()
if st.session_state.user_type == "premium":
    st.success("💎 Funciones de Descarga habilitadas para Reportes y Videos.")
else
