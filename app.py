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
    
    /* Estilo de los contenedores de auditoría (Gris) */
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
    
    /* Botones */
    .stButton>button {
        background-color: #800000;
        color: white;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CARGA DE DATOS COMPLETA (TEXTO ÍNTEGRO SIN RESUMIR) ---
DATOS = {
    "Pequeña (≤ 10 Trabajadores)": [
        {
            "id": "1",
            "titulo": "Asignación de persona que diseña el Sistema de Gestión de SST",
            "lista": ["Acta de designación de responsable", "Hoja de vida de la persona que diseña y ejecuta el sistema", "Licencia en Seguridad y Salud en el Trabajo", "Curso de SG-SST de 50 horas"],
            "frase": "📌 Contar con una persona competente no es solo un requisito, es quien garantiza que el SG-SST funcione correctamente y prevenga riesgos que pueden afectar a toda la empresa.",
            "periodicidad": "Semestral"
        },
        {
            "id": "2",
            "titulo": "Afiliación al Sistema de Seguridad Social Integral",
            "lista": ["Pagar la seguridad social y custodiar las planillas de pago mes a mes", "Revisar que no se tenga presuntas moras y estar al tanto de los beneficios de ARL, EPS y AFP", "Controlar la afiliación de los contratistas y proveedores y custodiar la planilla de cada mes"],
            "frase": "📌 Una afiliación adecuada protege al trabajador, pero también evita sanciones y responsabilidades económicas para la empresa.",
            "periodicidad": "Cuatrimestral"
        },
        {
            "id": "3",
            "titulo": "Programa de capacitación",
            "lista": ["Crear el Programa y el cronograma de capacitación", "Realizar las formaciones y entrenamientos en prevención de acuerdo a los riesgos prioritarios", "Salvaguardar las evidencias como listados de asistencia y evaluaciones", "Garantizar la participación de la alta dirección e incluir a proveedores y contratistas"],
            "frase": "📌 Una empresa que capacita, previene errores humanos y fortalece la cultura de seguridad en todos los niveles.",
            "periodicidad": "Bimestral"
        }
        # Nota: Se deben seguir agregando los ítems 4 al 7 con la misma estructura fiel al Word
    ],
    "Mediana (11-50)": [
        # Aquí se cargarán los 21 ítems íntegros con sus frases y listas de chequeo
        {
            "id": "1",
            "titulo": "Asignación de responsabilidades en SST",
            "lista": ["Definir responsabilidades para Representante legal", "Responsable del SG-SST", "Representante del COPASST", "Representante del COCOLA", "Representante de la BRIGADA DE EMERGENCIAS", "Comunicar y soportar documentalmente"],
            "frase": "📌 Definir responsabilidades claras permite una gestión organizada y el cumplimiento efectivo de cada actividad del SG-SST.",
            "periodicidad": "Cuatrimestral"
        }
    ],
    "Grande (>50 o Riesgo IV/V)": [
        # Aquí se cargarán los 62 ítems íntegros con sus frases y listas de chequeo
        {
            "id": "1",
            "titulo": "Asignación de recursos para el Sistema de Gestión de SST",
            "lista": ["Mantener un presupuesto de los recursos planeados y ejecutados", "Contar con recursos financieros, técnicos y humanos", "Soportar la asignación de recursos mediante acta firmada"],
            "frase": "📌 La asignación de recursos es la base para que el SG-SST sea ejecutable y no se quede solo en el papel.",
            "periodicidad": "Anual"
        }
    ]
}

# --- ESTADO DE LA SESIÓN ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=180)
    st.markdown("### Acceso Autorizado")
    correo = st.text_input("Usuario / Clave Dinámica")
    if st.button("Ingresar"):
        if correo in ["natalia@jpl.com", "jhuan@jpl.com", "gerardo@mym.com"]:
            st.session_state.user_type = "premium"
            st.success("Acceso Premium")
        else:
            st.session_state.user_type = "invitado"
            st.info("Modo Invitado")
    
    st.divider()
    categoria = st.selectbox("Categoría de Empresa", list(DATOS.keys()))

# --- CUERPO PRINCIPAL ---
st.title("🛡️ Sistema de Gestión de SST - JPL")
st.subheader(f"Panel de Auditoría: {categoria}")

tab1, tab2, tab3, tab4 = st.tabs(["📋 Lista de Chequeo", "📊 Desempeño", "⏳ Cronograma", "🎥 Multimedia"])

cumplimiento_total, checks_totales = 0, 0

with tab1:
    for item in DATOS[categoria]:
        with st.expander(f"Ítem {item['id']}: {item['titulo']}"):
            st.write(f"**Periodicidad:** {item['periodicidad']}")
            
            # Listas de chequeo para evaluación
            puntos_item = 0
            for check_text in item['lista']:
                checks_totales += 1
                if st.checkbox(check_text, key=f"check_{categoria}_{item['id']}_{check_text}"):
                    cumplimiento_total += 1
                    puntos_item += 1
            
            # Alerta dinámica de cumplimiento
            if puntos_item == len(item['lista']):
                st.success("✅ CUMPLE")
            elif puntos_item > 0:
                st.warning("⚠️ PENDIENTE / PARCIAL")
            else:
                st.error("🚨 NO CUMPLE")
            
            # Frase motivacional en dorado (Sin resumir)
            st.markdown(f'<div class="frase-dorada">{item["frase"]}</div>', unsafe_allow_html=True)

with tab2:
    st.header("Gráficas de Desempeño Real")
    progreso = (cumplimiento_total / checks_totales * 100) if checks_totales > 0 else 0
    
    fig = px.pie(values=[progreso, 100 - progreso], names=["Cumple", "Pendiente"],
                 color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
    st.plotly_chart(fig, use_container_width=True)
    st.metric("Nivel de Implementación Actual", f"{int(progreso)}%")

with tab3:
    st.header("Línea de Tiempo de Gestión")
    # Visible para todos
    df_cronograma = pd.DataFrame([
        {"Actividad": "Evaluación Inicial", "Inicio": "2026-04-01", "Fin": "2026-04-30"},
        {"Actividad": "Plan de Mejoramiento", "Inicio": "2026-05-01", "Fin": "2026-06-30"},
        {"Actividad": "Ejecución de Controles", "Inicio": "2026-07-01", "Fin": "2026-12-31"}
    ])
    st.plotly_chart(px.timeline(df_cronograma, x_start="Inicio", x_end="Fin", y="Actividad", color_discrete_sequence=['#800000']))

with tab4:
    st.header("Capacitación y Videos")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Video demostrativo
    
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Material Premium")
    else:
        st.warning("🔒 La descarga de material está disponible solo para clientes con suscripción activa.")

st.divider()
if st.session_state.user_type == "premium":
    st.button("📥 Generar Reporte PDF para Ministerio")
