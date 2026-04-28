import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="JPL Prevencionistas - Soluciones MyM", page_icon="🛡️", layout="wide")

# --- ESTILOS CORPORATIVOS (Vinotinto, Gris, Dorado) ---
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    .stTabs [data-baseweb="tab-list"] { background-color: #800000; }
    .stTabs [data-baseweb="tab"] { color: white; }
    
    .frase-dorada {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #FFD700;
        color: #FFD700;
        font-weight: bold;
        font-style: italic;
        margin-bottom: 10px;
    }
    .stExpander { background-color: #F0F2F6 !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- DATOS REALES ---
DATOS = {
    "Pequeña (1-10)": [
        {
            "id": "1",
            "titulo": "Asignación de persona que diseña el SG-SST",
            "lista": [
                {"nombre": "Acta de designación de responsable", "soporte": "PDF/Imagen del Acta firmada"},
                {"nombre": "Hoja de vida del diseñador", "soporte": "PDF de la Hoja de Vida"},
                {"nombre": "Licencia en SST vigente", "soporte": "Copia de la Licencia"},
                {"nombre": "Certificado Curso 50 horas", "soporte": "Certificado del curso"}
            ],
            "frase": "📌 Contar con una persona competente garantiza que el sistema prevenga riesgos que pueden afectar a toda la empresa.",
            "p": "Semestral"
        },
        {
            "id": "2",
            "titulo": "Afiliación al Sistema de Seguridad Social Integral",
            "lista": [
                {"nombre": "Planillas de pago mes a mes", "soporte": "Planilla PILA"},
                {"nombre": "Control de afiliación contratistas", "soporte": "Certificados de afiliación"}
            ],
            "frase": "📌 Una afiliación adecuada protege al trabajador y evita responsabilidades económicas para la empresa.",
            "p": "Mensual"
        }
    ]
}

# --- LÓGICA DE SESIÓN ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=160)
    st.title("🛡️ Gestión de Evidencias")
    correo = st.text_input("Correo de Cliente")
    if st.button("Validar Ingreso"):
        if correo in ["natalia@jpl.com", "jhuan@jpl.com", "gerardo@mym.com"]:
            st.session_state.user_type = "premium"
            st.success("Acceso Premium")
        else:
            st.session_state.user_type = "invitado"
            st.info("Modo Invitado")
    
    st.divider()
    cat = st.selectbox("Categoría de Empresa", list(DATOS.keys()))

# --- INTERFAZ ---
tab1, tab2, tab3 = st.tabs(["📋 Auditoría con Soportes", "📊 Desempeño Real", "🎥 Multimedia"])

cumplimiento_total, total_items = 0, 0

with tab1:
    st.header(f"Panel de Evidencias: {cat}")
    for item in DATOS[cat]:
        with st.expander(f"🔹 {item['id']}. {item['titulo']}"):
            st.markdown(f'<div class="frase-dorada">{item["frase"]}</div>', unsafe_allow_html=True)
            
            puntos_estandar = 0
            for sub in item['lista']:
                total_items += 1
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    # Selección S o N
                    opcion = st.radio(f"¿Cumple con: {sub['nombre']}?", ["No", "Sí"], key=f"r_{cat}_{item['id']}_{sub['nombre']}")
                
                with col2:
                    if opcion == "Sí":
                        # Si cumple, pide el soporte
                        st.file_uploader(f"Cargar {sub['soporte']}", type=["pdf", "png", "jpg"], key=f"f_{cat}_{item['id']}_{sub['nombre']}")
                        puntos_estandar += 1
                        cumplimiento_total += 1
                    else:
                        st.error(f"🚨 Alerta: Falta {sub['nombre']}. Se requiere plan de acción.")
                st.divider()

            # Semáforo final del estándar
            if puntos_estandar == len(item['lista']):
                st.success(f"✅ ESTÁNDAR {item['id']} COMPLETO CON SOPORTES")
            elif puntos_estandar > 0:
                st.warning(f"⚠️ ESTÁNDAR {item['id']} EN PROCESO (Faltan evidencias)")
            else:
                st.error(f"❌ ESTÁNDAR {item['id']} SIN GESTIÓN")

with tab2:
    st.header("Estadísticas Basadas en Evidencias")
    progreso = (cumplimiento_total / total_items * 100) if total_items > 0 else 0
    fig = px.pie(values=[progreso, 100-progreso], names=["Soportado", "Pendiente"], 
                 color_discrete_sequence=['#800000', '#D1D1D1'], hole=.5)
    st.plotly_chart(fig)
    st.metric("Cumplimiento Documental", f"{int(progreso)}%")

with tab3:
    st.header("Biblioteca de Capacitación")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if st.session_state.user_type == "premium":
        st.button("📥 Descargar Guía de Implementación")

st.divider()
if st.session_state.user_type == "premium":
    st.button("📥 Generar Reporte Final con Enlaces a Evidencias")
