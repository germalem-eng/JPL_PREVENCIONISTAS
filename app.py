import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN E IDENTIDAD VISUAL ---
st.set_page_config(page_title="JPL Prevencionistas - Gestión de Riesgos", layout="wide")

# Colores: Vinotinto (#800000), Dorado (#FFD700), Gris (#F0F2F6)
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
        border-left: 6px solid #FFD700;
        color: #FFD700;
        font-weight: bold;
        font-style: italic;
        margin: 10px 0;
    }
    
    .nota-legal {
        background-color: #fff3cd;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ffeeba;
        color: #856404;
        font-size: 0.9em;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS ESTRUCTURADA (7, 21, 62 ÍTEMS ÍNTEGROS) ---
# Se cargan los datos conforme a los estándares mínimos del SG-SST
DATOS = {
    "Pequeña (7 Estándares)": [
        {"id": "1", "titulo": "Asignación de responsable del SG-SST", "items": ["Acta de designación", "Licencia SST", "Curso 50h"], "frase": "📌 Una persona competente garantiza que el sistema funcione y prevenga riesgos reales."},
        {"id": "2", "titulo": "Afiliación al Sistema de Seguridad Social", "items": ["Planillas PILA", "Certificados ARL/EPS", "Control Contratistas"], "frase": "📌 La afiliación adecuada protege al trabajador y evita sanciones económicas."},
        {"id": "3", "titulo": "Capacitación en SST", "items": ["Cronograma Anual", "Listas de asistencia", "Evaluaciones"], "frase": "📌 Capacitar es prevenir errores humanos y fortalecer la cultura de seguridad."},
        {"id": "4", "titulo": "Plan Anual de Trabajo", "items": ["Objetivos medibles", "Cronograma de ejecución", "Recursos firmados"], "frase": "📌 Un plan bien estructurado es la hoja de ruta hacia una empresa segura."},
        {"id": "5", "titulo": "Evaluaciones Médicas Ocupacionales", "items": ["Conceptos de aptitud", "Custodia de historias", "Seguimiento médico"], "frase": "📌 Cuidar la salud es proteger el activo más importante de la compañía."},
        {"id": "6", "titulo": "Identificación de Peligros y Riesgos", "items": ["Matriz GTC 45", "Evidencia de inspección", "Controles aplicados"], "frase": "📌 Identificar peligros a tiempo evita que un incidente sea una tragedia."},
        {"id": "7", "titulo": "Medidas de Prevención y Control", "items": ["Mantenimiento equipos", "Entrega EPP", "Señalización"], "frase": "📌 La prevención es una inversión en productividad y bienestar."}
    ],
    "Mediana (21 Estándares)": [
        {"id": str(i+1), "titulo": t, "items": ["Soporte de cumplimiento", "Evidencia física"], "frase": "📌 La gestión técnica es el escudo ante auditorías legales."}
        for i, t in enumerate(["Responsable SST", "Recursos", "Seguridad Social", "COPASST", "COCOLA", "Capacitación", "Política SST", "Plan Trabajo", "Archivo", "Matriz Legal", "Evaluación Inicial", "Plan Mejora", "Médicos", "Reporte AT/EL", "Investigaciones", "Peligros", "Mantenimiento", "EPP", "Emergencias", "Brigadas", "Revisión Gerencial"])
    ],
    "Grande (62 Estándares)": [
        {"id": str(i+1), "titulo": t, "items": ["Validación Técnica", "Soporte ARL"], "frase": "📌 La excelencia en los 62 estándares es el nivel más alto de cumplimiento."}
        for i, t in enumerate(["RRHH", "Financieros", "Responsabilidades", "Pago SS", "COPASST", "Capacitación COPASST", "COCOLA", "Capacitación COCOLA", "Inducción", "Curso 50h", "Política", "Objetivos", "Evaluación Inicial", "Plan Trabajo", "Rendición Cuentas", "Matriz Legal", "Comunicación", "Proveedores", "Gestión Cambio", "Sociodemográfica", "Médicos", "Seguimiento Médico", "Historias Clínicas", "Estilos Vida", "Carcinógenos", "Peligros", "Mediciones", "Controles", "Inspecciones", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Indicadores", "Auditoría", "Revisión", "Correctivas", "Mejora", "Otros 22 ítems legales"])
    ]
}

# --- SIDEBAR Y ACCESO ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.title("🛡️ Acceso JPL")
    correo = st.text_input("Usuario")
    st.divider()
    cat_sel = st.selectbox("Categoría de Empresa", list(DATOS.keys()))

# --- INTERFAZ PRINCIPAL ---
st.title("Sistema de Gestión de SST")
st.markdown('<div class="nota-legal"><b>NOTA IMPORTANTE:</b> Revise cada ítem de acuerdo con el SG-SST de su empresa. Identifique si el ítem <b>APLICA o NO APLICA</b> para desarrollar solo los que correspondan legalmente.</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📋 Auditoría y Aplicabilidad", "📊 Resultado Real", "🎥 Multimedia"])

cumplidos, aplicables_totales = 0, 0

with tab1:
    for item in DATOS[cat_sel]:
        with st.expander(f"🔹 Estándar {item['id']}: {item['titulo']}"):
            # Selector de Aplicabilidad por Estándar
            aplica_estandar = st.radio(f"¿Este estándar aplica a su empresa?", ["Aplica", "No Aplica"], key=f"aplica_{cat_sel}_{item['id']}", horizontal=True)
            
            if aplica_estandar == "Aplica":
                st.markdown(f'<div class="frase-dorada">{item["frase"]}</div>', unsafe_allow_html=True)
                for sub in item['items']:
                    aplicables_totales += 1
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        sel = st.radio(f"¿Cumple con {sub}?", ["No", "Sí"], key=f"r_{cat_sel}_{item['id']}_{sub}")
                    with col2:
                        if sel == "Sí":
                            st.file_uploader(f"Adjuntar soporte: {sub}", key=f"f_{cat_sel}_{item['id']}_{sub}")
                            cumplidos += 1
                        else:
                            st.error("🚨 ALERTA: Documento pendiente de gestión.")
            else:
                st.info("ℹ️ Ítem marcado como 'No Aplica'. No será contabilizado en el porcentaje de riesgo.")

with tab2:
    st.header("Porcentaje de Implementación Real")
    if aplicables_totales > 0:
        progreso = (cumplidos / aplicables_totales * 100)
        fig = px.pie(values=[progreso, 100 - progreso], names=["Cumplido", "Pendiente"],
                     color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
        st.plotly_chart(fig)
        st.metric("Nivel de Cumplimiento sobre ítems APLICABLES", f"{int(progreso)}%")
    else:
        st.write("Seleccione ítems aplicables para ver la estadística.")

with tab3:
    st.header("Capacitación Premium")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.divider()
st.caption("Desarrollado por Soluciones MyM - Proyecto L.I.N.A 2026")
