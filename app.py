import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="APP JPL - Soluciones MyM", page_icon="🛡️", layout="wide")

# Estilos CSS
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

# --- DATOS (7, 21 Y 62) ---
DATOS = {
    "Pequeña (1-10)": [
        {"id": "1", "titulo": "Asignación Diseñador", "subs": ["Acta", "HV", "Licencia", "Curso 50h"], "f": "Garantiza competencia técnica.", "p": "Semestral"},
        {"id": "2", "titulo": "Afiliación SS", "subs": ["Planillas", "Pagos"], "f": "Protección legal y económica.", "p": "Cuatrimestral"}
    ],
    "Mediana (11-50)": [
        {"id": str(i+1), "titulo": f"Estándar Mediano {i+1}", "subs": ["Soporte"], "f": "Gestión preventiva.", "p": "Trimestral"} for i in range(21)
    ],
    "Grande (>50)": [
        {"id": str(i+1), "titulo": f"Estándar Superior {i+1}", "subs": ["Evidencia"], "f": "Excelencia operativa.", "p": "Mensual"} for i in range(62)
    ]
}

# --- LÓGICA DE USUARIO ---
if "user_type" not in st.session_state:
    st.session_state.user_type = "invitado"

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/JPL_PREVENCIONISTAS/main/logo_jplfinal.jpg", width=150)
    st.title("🛡️ Panel de Control")
    correo = st.text_input("Correo")
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
tab1, tab2, tab3 = st.tabs(["📊 Auditoría SST", "📈 Desempeño", "⏳ Línea de Tiempo"])

with tab1:
    st.header(f"Gestión: {cat}")
    cumplimiento_count = 0
    total_checks = 0
    
    for item in DATOS[cat]:
        with st.expander(f"📌 {item['id']}. {item['titulo']}"):
            st.caption(f"Vigencia: {item['p']}")
            for s in item['subs']:
                check = st.checkbox(s, key=f"c_{cat}_{item['id']}_{s}")
                total_checks += 1
                if check: cumplimiento_count += 1
            
            st.markdown(f'<div class="frase-jpl"><span class="texto-dorado">📌 {item["f"]}</span></div>', unsafe_allow_html=True)

with tab2:
    st.header("Gráficas de Desempeño Real")
    # Cálculo para la gráfica
    progreso_val = (cumplimiento_count / total_checks * 100) if total_checks > 0 else 0
    
    df_grafica = pd.DataFrame({
        "Estado": ["Cumplido", "Pendiente"],
        "Valor": [progreso_val, 100 - progreso_val]
    })
    
    fig = px.pie(df_grafica, values='Valor', names='Estado', 
                 title=f"Nivel de Cumplimiento: {cat}",
                 color_discrete_sequence=['#FFD700', '#444444'])
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Línea de Tiempo de Implementación")
    eventos = [
        {"Tarea": "Fase 1: Diagnóstico", "Inicio": "2026-04-01", "Fin": "2026-04-15"},
        {"Tarea": "Fase 2: Documentación", "Inicio": "2026-04-16", "Fin": "2026-05-15"},
        {"Tarea": "Fase 3: Auditoría", "Inicio": "2026-05-16", "Fin": "2026-06-30"}
    ]
    df_timeline = pd.DataFrame(eventos)
    fig_timeline = px.timeline(df_timeline, x_start="Inicio", x_end="Fin", y="Tarea", color="Tarea")
    fig_timeline.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_timeline, use_container_width=True)

# --- ZONA PREMIUM ---
st.divider()
if st.session_state.user_type == "premium":
    st.success("💎 Funciones Premium Desbloqueadas: Descarga de Reportes y Videos activa.")
    st.button("📥 Generar Reporte Ejecutivo PDF")
else:
    st.warning("🔒 Registrado como Invitado. Gráficas y Alertas habilitadas, Descargas bloqueadas.")
