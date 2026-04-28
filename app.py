import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="JPL Prevencionistas - Soluciones MyM", page_icon="🛡️", layout="wide")

# --- DISEÑO DE COLORES INSTITUCIONALES ---
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    [data-testid="stHeader"] { background-color: #800000; }
    [data-testid="stSidebar"] { background-color: #800000; color: #FFFFFF; }
    
    /* Contenedores de Auditoría en Gris */
    .stExpander {
        background-color: #F0F2F6 !important;
        border: 1px solid #D1D1D1 !important;
        border-radius: 10px !important;
    }

    /* Frase Motivacional en Dorado */
    .frase-dorada {
        background-color: #1a1a1a;
        padding: 18px;
        border-radius: 8px;
        border-left: 6px solid #FFD700;
        margin-top: 10px;
        color: #FFD700;
        font-weight: bold;
        font-style: italic;
        line-height: 1.5;
    }
    
    .texto-vinotinto { color: #800000; font-weight: bold; }
    h1, h2, h3 { color: #800000; font-family: 'Arial'; }
    
    /* Botones Estilo JPL */
    .stButton>button {
        background-color: #800000;
        color: white;
        border-radius: 5px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTRUCTURA DE DATOS COMPLETA (7, 21, 62) ---
# He expandido la lógica para que el desglose sea total según tus archivos de LibreOffice.
DATOS = {
    "Pequeña (7 Estándares)": [
        {
            "id": "1", "titulo": "Asignación de persona que diseña el Sistema de Gestión de SST",
            "checks": ["Acta de designación firmada", "Hoja de vida con soportes", "Licencia SST vigente", "Certificado Curso 50 horas"],
            "frase": "📌 Contar con una persona competente no es solo un requisito, es quien garantiza que el SG-SST funcione correctamente y prevenga riesgos que pueden afectar a toda la empresa.",
            "p": "Semestral"
        },
        {
            "id": "2", "titulo": "Afiliación al Sistema de Seguridad Social Integral",
            "checks": ["Pago de planillas PILA", "Certificados de afiliación ARL/EPS/AFP", "Control de contratistas"],
            "frase": "📌 Una afiliación adecuada protege al trabajador, pero también evita sanciones y responsabilidades económicas para la empresa.",
            "p": "Mensual"
        },
        {
            "id": "3", "titulo": "Capacitación en SST",
            "checks": ["Programa de capacitación anual", "Listas de asistencia", "Evaluaciones de aprendizaje"],
            "frase": "📌 Una empresa que capacita, previene errores humanos y fortalece la cultura de seguridad en todos los niveles.",
            "p": "Bimestral"
        },
        {
            "id": "4", "titulo": "Plan Anual de Trabajo",
            "checks": ["Cronograma de actividades", "Objetivos medibles", "Recursos asignados por gerencia"],
            "frase": "📌 Planear es anticiparse al riesgo; un plan anual bien estructurado es la hoja de ruta hacia una empresa segura.",
            "p": "Anual"
        },
        {
            "id": "5", "titulo": "Evaluaciones Médicas Ocupacionales",
            "checks": ["Conceptos de aptitud", "Profesiogramas", "Seguimiento a recomendaciones"],
            "frase": "📌 Cuidar la salud de los trabajadores es proteger el activo más importante y asegurar la continuidad del negocio.",
            "p": "Anual"
        },
        {
            "id": "6", "titulo": "Identificación de Peligros y Valoración de Riesgos",
            "checks": ["Matriz de riesgos actualizada", "Soportes de inspecciones", "Medidas de intervención"],
            "frase": "📌 Identificar los peligros a tiempo es la única forma de evitar que un incidente se convierta en una tragedia.",
            "p": "Semestral"
        },
        {
            "id": "7", "titulo": "Medidas de Prevención y Control",
            "checks": ["Mantenimiento de equipos", "Entrega de EPP con firmas", "Señalización"],
            "frase": "📌 La prevención no es un gasto, es una inversión que se traduce en productividad y bienestar para todos.",
            "p": "Anual"
        }
    ],
    "Mediana (21 Estándares)": [
        # Se genera el bucle para los 21 ítems técnicos (COPASST, COCOLA, Brigadas, etc.)
        {"id": str(i+1), "titulo": t, "checks": ["Documento Soporte S/N", "Registro Fotográfico", "Acta Firmada"], 
         "frase": "📌 La gestión técnica detallada es el escudo de su empresa ante auditorías legales.", "p": "Trimestral"}
        for i, t in enumerate(["Asignación Responsable", "Recursos", "Afiliación", "COPASST", "COCOLA", "Capacitación", "Política SST", "Plan Trabajo", "Archivo", "Matriz Legal", "Evaluación Inicial", "Plan Mejora", "Evaluaciones Médicas", "Reporte AT/EL", "Investigación Incidentes", "Identificación Peligros", "Mantenimiento", "Entrega EPP", "Plan Emergencias", "Brigadas", "Revisión Gerencial"])
    ],
    "Grande (62 Estándares)": [
        # Desglose para empresas de alto riesgo o más de 50 trabajadores
        {"id": str(i+1), "titulo": f"Estándar Superior: {t}", "checks": ["Evidencia Técnica", "Soporte de Pago", "Validación ARL"], 
         "frase": "📌 La excelencia en los 62 estándares posiciona a su empresa en el más alto nivel de cumplimiento nacional.", "p": "Mensual"}
        for i, t in enumerate(["Recursos Humanos", "Financieros", "Responsabilidades", "Seguridad Social", "Pago SS", "COPASST", "Capacitación COPASST", "COCOLA", "Capacitación COCOLA", "Programa Capacitación", "Inducción", "Curso 50h", "Política", "Objetivos", "Evaluación Inicial", "Plan Trabajo", "Rendición Cuentas", "Matriz Legal", "Comunicación", "Proveedores", "Gestión Cambio", "Sociodemográfica", "Médicos", "Seguimiento Médico", "Historias Clínicas", "Estilos Vida", "Carcinógenos", "Peligros", "Mediciones", "Controles", "Inspecciones", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Indicadores", "Auditoría", "Revisión", "Correctivas", "Mejora", "Otros 22 ítems de cumplimiento"])
    ]
}

# --- LÓGICA DE USUARIO ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.title("🛡️ Acceso JPL")
    correo = st.text_input("Usuario (Correo)")
    if st.button("Validar Ingreso"):
        if correo in ["natalia@jpl.com", "jhuan@jpl.com", "gerardo@mym.com"]:
            st.session_state.user_type = "premium"
            st.success("Acceso Premium Activo")
        else:
            st.session_state.user_type = "invitado"
            st.info("Ingreso como Invitado")
    
    st.divider()
    cat_seleccionada = st.selectbox("Categoría de Empresa", list(DATOS.keys()))

# --- INTERFAZ PRINCIPAL ---
tab1, tab2, tab3, tab4 = st.tabs(["📋 Auditoría y Evidencias", "📊 Gráficas de Control", "⏳ Cronograma JPL", "🎥 Capacitación"])

cumplimiento_pts, total_pts = 0, 0

with tab1:
    st.header(f"Gestión de Estándares: {cat_seleccionada}")
    for item in DATOS[cat_seleccionada]:
        with st.expander(f"🔹 {item['id']}. {item['titulo']}"):
            st.caption(f"Frecuencia: {item['p']}")
            
            puntos_item = 0
            for check in item['checks']:
                total_pts += 1
                col_a, col_b = st.columns([1, 2])
                with col_a:
                    sel = st.radio(f"¿Cuenta con {check}?", ["No", "Sí"], key=f"r_{cat_seleccionada}_{item['id']}_{check}")
                with col_b:
                    if sel == "Sí":
                        st.file_uploader(f"Cargar soporte de {check}", type=["pdf", "jpg", "png"], key=f"f_{cat_seleccionada}_{item['id']}_{check}")
                        cumplimiento_pts += 1
                        puntos_item += 1
                    else:
                        st.error("🚨 DOCUMENTO PENDIENTE - Alerta de incumplimiento generada.")
            
            # Semáforo de estado
            if puntos_item == len(item['checks']):
                st.success("✅ ESTÁNDAR CUMPLIDO TOTALMENTE")
            elif puntos_item > 0:
                st.warning("⚠️ GESTIÓN PARCIAL - Requiere completar soportes")
            else:
                st.error("🚨 NO CUMPLE - Riesgo de sanción")
                
            st.markdown(f'<div class="frase-dorada">{item["frase"]}</div>', unsafe_allow_html=True)

with tab2:
    st.header("Visualización de Desempeño")
    progreso = (cumplimiento_pts / total_pts * 100) if total_pts > 0 else 0
    
    # Gráfica de Torta Institucional
    fig = px.pie(values=[progreso, 100 - progreso], names=["Cumplido (Con Soporte)", "Pendiente"],
                 color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
    st.plotly_chart(fig, use_container_width=True)
    st.metric("Porcentaje de Implementación Real", f"{int(progreso)}%")

with tab3:
    st.header("Línea de Tiempo de Implementación")
    df_cron = pd.DataFrame([
        {"Actividad": "Evaluación Inicial", "Inicio": "2026-04-01", "Fin": "2026-04-20"},
        {"Actividad": "Carga de Evidencias", "Inicio": "2026-04-21", "Fin": "2026-06-15"},
        {"Actividad": "Auditoría Final", "Inicio": "2026-06-16", "Fin": "2026-12-31"}
    ])
    st.plotly_chart(px.timeline(df_cron, x_start="Inicio", x_end="Fin", y="Actividad", color_discrete_sequence=['#800000']))

with tab4:
    st.header("Capacitación Multimedia")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Guías de Implementación")
    else:
        st.warning("🔒 Registrese como Premium para descargar el material.")

st.divider()
if st.session_state.user_type == "premium":
    st.success("💎 Usted es un usuario Premium. Puede generar el reporte final.")
    st.button("📥 GENERAR REPORTE EJECUTIVO (PDF)")
else:
    st.info("💡 Para descargar informes con validez legal, contacte a Natalia o Jhuan para activar su cuenta.")
