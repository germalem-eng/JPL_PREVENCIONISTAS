import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="App JPL - Gestión Técnica SST", layout="wide", initial_sidebar_state="expanded")

# --- 2. BASE DE DATOS TÉCNICA (RESOLUCIÓN 0312 DE 2019) ---
# Estándares completos por nivel
E_7 = [
    "1.1.1 Asignación de persona que diseña el SG-SST",
    "1.1.3 Asignación de recursos para el SG-SST",
    "1.2.1 Afiliación al Sistema de Seguridad Social Integral",
    "2.1.1 Plan Anual de Trabajo",
    "4.1.1 Evaluación médica ocupacional",
    "6.1.1 Identificación de peligros, evaluación y valoración de riesgos",
    "7.1.1 Ejecución de medidas de prevención y control"
]

E_21 = [
    "1.1.1 Asignación de responsable", "1.1.3 Asignación de recursos", "1.1.5 Conformación COPASST", 
    "1.1.6 Conformación Comité Convivencia", "1.2.1 Programa Capacitación", "1.2.2 Inducción y Reinducción",
    "2.1.1 Plan Anual de Trabajo", "2.1.2 Archivo y retención documental", "3.1.1 Descripción sociodemográfica",
    "3.1.2 Actividades de promoción y prevención", "3.1.4 Realización evaluaciones médicas", "3.1.9 Registro y reporte AT/EL",
    "4.1.1 Identificación de peligros y riesgos", "4.1.2 Mantenimiento periódico de instalaciones", "4.1.3 Entrega de EPP",
    "5.1.1 Plan de prevención y emergencias", "6.1.1 Brigada de prevención", "6.1.4 Revisión por la alta dirección",
    "7.1.1 Investigación de incidentes y AT", "7.1.2 Acciones preventivas y correctivas", "7.1.3 Auditoría anual"
]

E_62 = {
    "RECURSOS (PLANEAR)": ["1.1.1 Responsable", "1.1.2 Responsabilidades", "1.1.3 Asignación recursos", "1.1.4 Seguridad Social", "1.1.5 COPASST", "1.1.6 Comité Convivencia", "1.1.7 Programa Capacitación", "1.1.8 Inducción", "1.2.1 Presupuesto", "1.2.2 Documentación", "1.2.3 Archivo"],
    "GESTIÓN SALUD (HACER)": ["3.1.1 Evaluaciones Médicas", "3.1.2 Perfiles de Cargo", "3.1.3 Historias Clínicas", "3.1.4 Reporte AT/EL", "3.1.5 Investigación AT/EL", "3.1.6 Matriz de Peligros", "3.2.1 Servicios de Higiene", "3.2.2 Estilo de vida saludable"],
    "GESTIÓN PELIGROS (HACER)": ["4.1.1 Medidas de Prevención", "4.1.2 Inspecciones", "4.1.3 Mantenimiento", "4.1.4 EPP", "4.1.5 Plan de Emergencias"],
    "GESTIÓN AMENAZAS (VERIFICAR/ACTUAR)": ["5.1.1 Planes de Mejora", "5.1.2 Auditoría", "5.1.3 Revisión Dirección"]
}

# --- 3. LÓGICA DE TIEMPO Y ESTADÍSTICAS ---
# Corrección ME (Month End) para evitar el Warning en tu HP Compaq
fechas = pd.date_range(start="2026-01-01", periods=5, freq='ME').strftime('%Y-%m').tolist()
historial_cumplimiento = [35, 42, 58, 71, 85]

# --- 4. ESTILOS CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }
    
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Botones Gris Plata */
    div.stButton > button { 
        background-color: #C0C0C0 !important; 
        color: #333 !important; 
        border-radius: 12px;
        border: 1px solid #A9A9A9;
    }

    .stApp { background-color: #F8F9FA; }
    
    .timeline-box {
        border-left: 6px solid #800000;
        padding: 15px 25px;
        margin: 15px 0;
        background: #ffffff;
        border-radius: 0 15px 15px 0;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.05);
    }

    .card-item { background: white; padding: 10px; border-radius: 8px; border-left: 5px solid #800000; margin-bottom: 5px; }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background: #F2F2F2; text-align: center; padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; }
</style>
""", unsafe_allow_html=True)

# --- 5. ESTADO DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'respuestas' not in st.session_state: st.session_state.respuestas = {}
if 'autenticado' not in st.session_state: st.session_state.autenticado = False

# --- 6. BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    if not st.session_state.autenticado:
        u = st.text_input("Usuario")
        p = st.text_input("Clave", type="password")
        if st.button("ACCEDER"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Acceso: Gerardo")
        if st.button("CERRAR SESIÓN"): st.session_state.autenticado = False; st.rerun()
    
    st.divider()
    if st.button("🏠 INICIO"): st.session_state.pantalla = 'inicio'; st.rerun()
    if st.button("📊 ESTADÍSTICAS"): st.session_state.pantalla = 'stats'; st.rerun()
    if st.button("🎥 VIDEOTECA"): st.session_state.pantalla = 'videos'; st.rerun()

# --- 7. PANTALLAS ---

if st.session_state.pantalla == 'inicio':
    st.title("🛡️ App JPL - Diagnóstico Técnico 0312")
    st.markdown("### Herramienta de Alertas Tempranas en Seguridad y Salud")
    
    st.write("Seleccione el tamaño de la empresa para iniciar la auditoría:")
    c1, c2, c3 = st.columns(3)
    if c1.button("🏢 MICRO (<10)\n7 Estándares"): st.session_state.nivel = "7"; st.session_state.pantalla = 'auditoria'; st.rerun()
    if c2.button("🏬 PYME (11-50)\n21 Estándares"): st.session_state.nivel = "21"; st.session_state.pantalla = 'auditoria'; st.rerun()
    if c3.button("🏭 GRANDE (+50)\n62 Estándares"): st.session_state.nivel = "62"; st.session_state.pantalla = 'auditoria'; st.rerun()

    st.divider()

    # PLANES MODERADOS (Al final como soporte de servicio)
    st.markdown("#### 📋 Soporte y Consultoría JPL")
    p1, p2, p3, p4 = st.columns(4)
    planes = [("Asesoría Micro", "$30.000"), ("Soporte Pyme", "$60.000"), ("Gestión Grande", "$100.000"), ("Corporativo", "Convenio")]
    for i, (n, v) in enumerate(planes):
        with [p1, p2, p3, p4][i]:
            st.info(f"**{n}**\n\n{v}")

elif st.session_state.pantalla == 'auditoria':
    nivel = st.session_state.nivel
    st.header(f"Auditoría de Cumplimiento: Nivel {nivel}")
    
    # 📈 LÍNEA DE TIEMPO (Auto-refresco visual)
    chart_data = pd.DataFrame({"Mes": fechas, "Cumplimiento %": historial_cumplimiento})
    st.line_chart(chart_data, x="Mes", y="Cumplimiento %")

    # LÓGICA DE CALIFICACIÓN Y ALERTA DINÁMICA
    if nivel == "7": lista = E_7
    elif nivel == "21": lista = E_21
    else: lista = [item for sublist in E_62.values() for item in sublist]

    cumplidos = sum(1 for it in lista if st.session_state.respuestas.get(f"{nivel}_{it}") == "CUMPLE")
    porcentaje = round((cumplidos / len(lista)) * 100, 2)

    # ALERTA TEMPRANA
    color = "red" if porcentaje < 60 else "orange" if porcentaje < 85 else "green"
    texto = "RIESGO CRÍTICO" if porcentaje < 60 else "MODERADO" if porcentaje < 85 else "ACEPTABLE"
    
    st.markdown(f"""<div class='timeline-box' style='border-left-color:{color};'>
        <h3 style='color:{color};'>{texto} ({porcentaje}%)</h3>
        <p><b>Fase de Diagnóstico:</b> La empresa se encuentra en estado {texto.lower()}.</p>
    </div>""", unsafe_allow_html=True)

    # FORMULARIO TÉCNICO
    for item in lista:
        with st.container():
            st.markdown(f'<div class="card-item">{item}</div>', unsafe_allow_html=True)
            col_a, col_b = st.columns([2, 1])
            res = col_a.radio("Verificación:", ["Pendiente", "CUMPLE", "NO CUMPLE"], key=f"{nivel}_{item}", horizontal=True, disabled=not st.session_state.autenticado)
            st.session_state.respuestas[f"{nivel}_{item}"] = res
            col_b.text_input("Hallazgo / Evidencia", key=f"ev_{nivel}_{item}", disabled=not st.session_state.autenticado)

elif st.session_state.pantalla == 'stats':
    st.header("📊 Estadísticas de Gestión JPL")
    if st.session_state.autenticado:
        st.write("### Reporte Global por Ciclos PHVA")
        st.bar_chart(pd.DataFrame(np.random.randint(50,100,size=(4, 1)), index=['Planear', 'Hacer', 'Verificar', 'Actuar']))
        st.download_button("📥 Descargar Reporte Completo (PDF)", data="DATOS", file_name="Reporte_JPL.pdf")
    else:
        st.warning("Debe iniciar sesión para ver estadísticas detalladas.")

elif st.session_state.pantalla == 'videos':
    st.header("🎥 Videoteca de Capacitación")
    cod = st.text_input("Código de Acceso:", type="password")
    if cod == "JPL2026":
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        st.error("Código requerido para visualizar contenido técnico.")

# --- 8. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
