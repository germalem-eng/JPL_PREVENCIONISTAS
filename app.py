import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="APP JPL - Soluciones MyM", page_icon="🛡️", layout="wide")

# --- COLORES INSTITUCIONALES ---
# Vinotinto: #800000 | Gris: #F0F2F6 | Blanco: #FFFFFF | Negro: #000000
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    [data-testid="stHeader"] { background-color: #800000; }
    [data-testid="stSidebar"] { background-color: #800000; }
    .stTabs [data-baseweb="tab-list"] { background-color: #800000; }
    .stTabs [data-baseweb="tab"] { color: #FFFFFF; }
    
    /* Recuadros de Auditoría en Gris */
    .stExpander {
        background-color: #F0F2F6 !important;
        border: 1px solid #D1D1D1 !important;
        border-radius: 10px !important;
    }
    
    .frase-jpl {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #800000;
        margin-top: 10px;
        color: #000000;
    }
    .texto-vinotinto { color: #800000; font-weight: bold; }
    h1, h2, h3 { color: #800000; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS REAL (Extracto de tus Documentos) ---
DATOS = {
    "Pequeña (1-10)": [
        {"id": "1", "titulo": "Asignación de persona que diseña el SG-SST", "subs": ["Acta de designación", "Hoja de vida", "Licencia SST", "Curso 50h"], "f": "📌 Contar con una persona competente no es solo un requisito, es quien garantiza que el SG-SST funcione correctamente y prevenga riesgos que pueden afectar a toda la empresa.", "p": "Semestral"},
        {"id": "2", "titulo": "Afiliación Seguridad Social", "subs": ["Planillas mes a mes", "Verificación moras", "Control contratistas"], "f": "Protección legal y económica.", "p": "Cuatrimestral"},
        {"id": "3", "titulo": "Capacitación en SST", "subs": ["Programa/Cronograma", "Inducciones", "Evidencias"], "f": "Previene errores humanos.", "p": "Bimestral"},
        {"id": "4", "titulo": "Plan Anual de Trabajo", "subs": ["Objetivos/Metas", "Cronograma", "Recursos firmados"], "f": "Planear es anticiparse.", "p": "Anual"},
        {"id": "5", "titulo": "Evaluaciones Médicas", "subs": ["Conceptos ingreso/egreso", "Historias clínicas", "Seguimiento"], "f": "Cuidar la salud es prioridad.", "p": "Anual"},
        {"id": "6", "titulo": "Identificación de Peligros", "subs": ["Matriz GTC 45", "Participación", "Controles"], "f": "Identificar para prevenir.", "p": "Semestral"},
        {"id": "7", "titulo": "Medidas de Prevención", "subs": ["Mantenimiento", "Entrega EPP", "Actividades"], "f": "Resultados con disciplina.", "p": "Anual"}
    ],
    "Mediana (11-50)": [
        {"id": str(i+1), "titulo": t, "subs": ["Soporte Documental", "Registro Ejecución"], "f": "Gestión preventiva.", "p": "Trimestral"}
        for i, t in enumerate(["Asignación Responsable", "Recursos", "Afiliación", "COPASST", "COCOLA", "Capacitación", "Política SST", "Plan Trabajo", "Archivo", "Matriz Legal", "Evaluación Inicial", "Médicos", "Carcinógenos", "Reporte AT", "Peligros", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Auditoría", "Revisión"])
    ],
    "Grande (>50)": [
        {"id": str(i+1), "titulo": t, "subs": ["Requisito Legal", "Soporte Técnico"], "f": "Excelencia operativa.", "p": "Mensual"}
        for i, t in enumerate(["RRHH", "Financieros", "Responsabilidades", "Seguridad Social", "Pago SS", "COPASST", "Capacitación COPASST", "COCOLA", "Capacitación COCOLA", "Programa Capacitación", "Inducción", "Curso 50h", "Política", "Objetivos", "Evaluación Inicial", "Plan Trabajo", "Rendición Cuentas", "Matriz Legal", "Comunicación", "Proveedores", "Gestión Cambio", "Sociodemográfica", "Médicos", "Seguimiento Médico", "Historias Clínicas", "Estilos Vida", "Carcinógenos", "Peligros", "Mediciones", "Controles", "Inspecciones", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Indicadores", "Auditoría", "Revisión", "Correctivas", "Mejora"])
    ]
}

# --- LÓGICA DE USUARIO ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=150)
    st.title("🛡️ Acceso Clientes")
    correo = st.text_input("Correo")
    if st.button("Validar Ingreso"):
        if correo in ["natalia@jpl.com", "jhuan@jpl.com", "gerardo@mym.com"]:
            st.session_state.user_type = "premium"
            st.success("Modo Premium")
        else:
            st.session_state.user_type = "invitado"
            st.info("Modo Invitado")
    
    st.divider()
    cat = st.selectbox("Categoría de Empresa", list(DATOS.keys()))

# --- INTERFAZ PRINCIPAL ---
tab1, tab2, tab3, tab4 = st.tabs(["📋 Auditoría", "📊 Desempeño", "⏳ Cronograma", "🎥 Capacitación"])

cumplimiento_count, total_checks = 0, 0

with tab1:
    st.header(f"Gestión de Riesgos: {cat}")
    for item in DATOS[cat]:
        with st.expander(f"🔹 {item['id']}. {item['titulo']}"):
            item_checks = 0
            for s in item['subs']:
                check = st.checkbox(s, key=f"c_{cat}_{item['id']}_{s}")
                total_checks += 1
                if check: 
                    cumplimiento_count += 1
                    item_checks += 1
            
            # Alertas Dinámicas por Ítem
            if item_checks == len(item['subs']):
                st.success("✅ Cumple")
            elif item_checks > 0:
                st.warning("⚠️ Pendiente / Parcial")
            else:
                st.error("🚨 No cumple")
                
            st.markdown(f'<div class="frase-jpl"><span class="texto-vinotinto">📌 {item["f"]}</span></div>', unsafe_allow_html=True)

with tab2:
    st.header("Estadísticas de Cumplimiento")
    progreso = (cumplimiento_count / total_checks * 100) if total_checks > 0 else 0
    fig = px.pie(values=[progreso, 100-progreso], names=["Cumple", "Pendiente/No Cumple"], 
                 color_discrete_sequence=['#800000', '#D1D1D1'], hole=.4)
    st.plotly_chart(fig)
    st.metric("Nivel de Implementación", f"{int(progreso)}%")

with tab3:
    st.header("Línea de Tiempo de Gestión")
    df_t = pd.DataFrame([
        {"Tarea": "Diagnóstico Inicial", "Inicio": "2026-04-01", "Fin": "2026-04-15"},
        {"Tarea": "Diseño de Sistema", "Inicio": "2026-04-16", "Fin": "2026-06-30"},
        {"Tarea": "Fase de Ejecución", "Inicio": "2026-07-01", "Fin": "2026-12-31"}
    ])
    fig_g = px.timeline(df_t, x_start="Inicio", x_end="Fin", y="Tarea", color="Tarea",
                        color_discrete_sequence=['#800000', '#B0B0B0', '#444444'])
    st.plotly_chart(fig_g)

with tab4:
    st.header("Biblioteca de Videos JPL")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Material Premium")
    else:
        st.warning("🔒 Descarga bloqueada para invitados.")

st.divider()
if st.session_state.user_type == "premium":
    st.button("📥 Generar Reporte PDF Final")
else:
    st.caption("Soluciones MyM - Modo Visualización Activo")
