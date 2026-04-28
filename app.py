import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="JPL Prevencionistas - Soluciones MyM", page_icon="🛡️", layout="wide")

# --- DISEÑO DE COLORES INSTITUCIONALES (VINOTINTO, GRIS, BLANCO) ---
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    [data-testid="stHeader"] { background-color: #800000; }
    [data-testid="stSidebar"] { background-color: #800000; color: #FFFFFF; }
    
    /* Recuadros de Auditoría en Gris */
    .stExpander {
        background-color: #F0F2F6 !important;
        border: 1px solid #D1D1D1 !important;
        border-radius: 8px !important;
    }

    /* Frase Motivacional en Dorado */
    .frase-dorada {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #FFD700;
        margin-top: 10px;
        color: #FFD700;
        font-weight: bold;
        font-style: italic;
    }
    
    .texto-vinotinto { color: #800000; font-weight: bold; }
    h1, h2, h3 { color: #800000; }
    
    /* Estilo para los botones */
    .stButton>button {
        background-color: #800000;
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS ÍNTEGRA (Sin resúmenes) ---
DATOS = {
    "Pequeña (1-10)": [
        {"id": "1", "titulo": "Asignación de persona que diseña el Sistema de Gestión de SST", "lista": ["Acta de designación de responsable", "Hoja de vida de la persona que diseña y ejecuta el sistema", "Licencia en Seguridad y Salud en el Trabajo", "Curso de SG-SST de 50 horas"], "frase": "📌 Contar con una persona competente no es solo un requisito, es quien garantiza que el SG-SST funcione correctamente y prevenga riesgos que pueden afectar a toda la empresa.", "p": "Semestral"},
        {"id": "2", "titulo": "Afiliación al Sistema de Seguridad Social Integral", "lista": ["Pagar la seguridad social y custodiar las planillas de pago mes a mes", "Revisar que no se tenga presuntas moras y estar al tanto de los beneficios de ARL, EPS y AFP", "Controlar la afiliación de los contratistas y proveedores y custodiar la planilla de cada mes"], "frase": "📌 Una afiliación adecuada protege al trabajador, pero también evita sanciones y responsabilidades económicas para la empresa.", "p": "Cuatrimestral"},
        {"id": "3", "titulo": "Programa de capacitación", "lista": ["Crear el Programa y el cronograma de capacitación", "Realizar las formaciones y entrenamientos en prevención de acuerdo a los riesgos prioritarios", "Salvaguardar las evidencias como listados de asistencia y evaluaciones", "Garantizar la participación de la alta dirección e incluir a proveedores y contratistas"], "frase": "📌 Una empresa que capacita, previene errores humanos y fortalece la cultura de seguridad en todos los niveles.", "p": "Bimestral"},
        {"id": "4", "titulo": "Plan Anual de Trabajo", "lista": ["Definir objetivos y metas de acuerdo a los riesgos", "Crear cronograma de actividades con responsables", "Asignar y firmar los recursos financieros y técnicos"], "frase": "📌 Planear es anticiparse al riesgo; un plan anual bien estructurado es la hoja de ruta hacia una empresa segura.", "p": "Anual"},
        {"id": "5", "titulo": "Evaluaciones Médicas Ocupacionales", "lista": ["Realizar exámenes de ingreso, periódicos y de egreso", "Custodiar las historias clínicas bajo reserva legal", "Realizar seguimiento a las recomendaciones médicas"], "frase": "📌 Cuidar la salud de los trabajadores es proteger el activo más importante y asegurar la continuidad del negocio.", "p": "Anual"},
        {"id": "6", "titulo": "Identificación de Peligros y Valoración de Riesgos", "lista": ["Elaborar la matriz de riesgos (GTC 45)", "Garantizar la participación de los trabajadores en la identificación", "Definir medidas de intervención para cada riesgo hallado"], "frase": "📌 Identificar los peligros a tiempo es la única forma de evitar que un incidente se convierta en una tragedia.", "p": "Semestral"},
        {"id": "7", "titulo": "Medidas de Prevención y Control", "lista": ["Ejecutar las actividades de control definidas", "Realizar mantenimiento preventivo a instalaciones y equipos", "Registrar la entrega y reposición de Elementos de Protección Personal (EPP)"], "frase": "📌 La prevención no es un gasto, es una inversión que se traduce en productividad y bienestar para todos.", "p": "Anual"}
    ],
    "Mediana (11-50)": [], # Aquí se cargan los 21 de la misma forma
    "Grande (>50)": [] # Aquí los 62
}

# --- LÓGICA DE USUARIO ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.title("🛡️ Panel de Control")
    correo = st.text_input("Correo o Clave Dinámica")
    if st.button("Validar Acceso"):
        if correo in ["natalia@jpl.com", "jhuan@jpl.com", "gerardo@mym.com"]:
            st.session_state.user_type = "premium"
            st.success("Acceso Premium")
        else:
            st.session_state.user_type = "invitado"
            st.info("Modo Invitado")
    
    st.divider()
    cat = st.selectbox("Categoría de Empresa", list(DATOS.keys()))

# --- INTERFAZ PRINCIPAL ---
tab1, tab2, tab3, tab4 = st.tabs(["📋 Auditoría Real", "📊 Desempeño", "⏳ Cronograma", "🎥 Multimedia"])

cumplimiento_count, total_checks = 0, 0

with tab1:
    st.header(f"Gestión de Estándares: {cat}")
    for item in DATOS[cat]:
        with st.expander(f"🔹 {item['id']}. {item['titulo']}"):
            st.caption(f"Periodicidad sugerida: {item['p']}")
            puntos_item = 0
            for check_text in item['lista']:
                total_checks += 1
                if st.checkbox(check_text, key=f"c_{cat}_{item['id']}_{check_text}"):
                    cumplimiento_count += 1
                    puntos_item += 1
            
            # Semáforo de cumplimiento por ítem
            if puntos_item == len(item['lista']):
                st.success("✅ CUMPLE")
            elif puntos_item > 0:
                st.warning("⚠️ PENDIENTE")
            else:
                st.error("🚨 NO CUMPLE")
                
            st.markdown(f'<div class="frase-dorada">{item["frase"]}</div>', unsafe_allow_html=True)

with tab2:
    st.header("Análisis de Implementación")
    progreso = (cumplimiento_count / total_checks * 100) if total_checks > 0 else 0
    fig = px.pie(values=[progreso, 100-progreso], names=["Cumplido", "Pendiente"], 
                 color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
    st.plotly_chart(fig)
    st.metric("Nivel de Cumplimiento", f"{int(progreso)}%")

with tab3:
    st.header("Línea de Tiempo")
    df_t = pd.DataFrame([
        {"Fase": "Evaluación Inicial", "Inicio": "2026-04-01", "Fin": "2026-04-30"},
        {"Fase": "Plan de Trabajo", "Inicio": "2026-05-01", "Fin": "2026-06-30"}
    ])
    st.plotly_chart(px.timeline(df_t, x_start="Inicio", x_end="Fin", y="Fase", color_discrete_sequence=['#800000']))

with tab4:
    st.header("Biblioteca de Videos")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Video")
    else:
        st.warning("🔒 Descarga exclusiva para Premium.")

st.divider()
if st.session_state.user_type == "premium":
    st.button("📥 Generar Reporte PDF Final")
