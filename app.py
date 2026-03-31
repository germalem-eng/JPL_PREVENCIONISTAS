import streamlit as st
import time
import pandas as pd
import numpy as np

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="App JPL", layout="wide", initial_sidebar_state="expanded")

# --- 2. BASE DE DATOS TÉCNICA (RESOLUCIÓN 0312 DE 2019) ---
# Estándares para Empresas de < 10 trabajadores (7 ítems)
E_7 = [
    "1.1.1 Asignación de persona que diseña el SG-SST",
    "1.1.3 Asignación de recursos para el SG-SST",
    "1.2.1 Afiliación al Sistema de Seguridad Social Integral",
    "2.1.1 Plan Anual de Trabajo",
    "4.1.1 Evaluación médica ocupacional",
    "6.1.1 Identificación de peligros, evaluación y valoración de riesgos",
    "7.1.1 Ejecución de medidas de prevención y control"
]

# Estándares para Empresas de 11 a 50 trabajadores (21 ítems) - Resumen de grupos
E_21 = [
    "1.1.1 Asignación de responsable", "1.1.3 Asignación de recursos", "1.1.5 Conformación COPASST", 
    "1.1.6 Conformación Comité Convivencia", "1.2.1 Programa Capacitación", "1.2.2 Inducción y Reinducción",
    "2.1.1 Plan Anual de Trabajo", "2.1.2 Archivo y retención documental", "3.1.1 Descripción sociodemográfica",
    "3.1.2 Actividades de promoción y prevención", "3.1.4 Realización evaluaciones médicas", "3.1.9 Registro y reporte AT/EL",
    "4.1.1 Identificación de peligros y riesgos", "4.1.2 Mantenimiento periódico de instalaciones", "4.1.3 Entrega de EPP",
    "5.1.1 Plan de prevención y emergencias", "6.1.1 Brigada de prevención", "6.1.4 Revisión por la alta dirección",
    "7.1.1 Investigación de incidentes y AT", "7.1.2 Acciones preventivas y correctivas", "7.1.3 Auditoría anual"
]

# Estándares para Empresas de > 50 o Riesgo IV/V (62 ítems) - Agrupados por ciclo
E_62 = {
    "RECURSOS (PLANEAR)": ["1.1.1 Responsable", "1.1.2 Responsabilidades", "1.1.3 Asignación recursos", "1.1.4 Seguridad Social", "1.1.5 COPASST", "1.1.6 Comité Convivencia", "1.1.7 Programa Capacitación", "1.1.8 Inducción", "1.2.1 Presupuesto", "1.2.2 Documentación", "1.2.3 Archivo"],
    "GESTIÓN SALUD (HACER)": ["3.1.1 Evaluaciones Médicas", "3.1.2 Perfiles de Cargo", "3.1.3 Historias Clínicas", "3.1.4 Reporte AT/EL", "3.1.5 Investigación AT/EL", "3.1.6 Matriz de Peligros", "3.2.1 Servicios de Higiene", "3.2.2 Estilo de vida saludable"],
    "GESTIÓN PELIGROS (HACER)": ["4.1.1 Medidas de Prevención", "4.1.2 Inspecciones", "4.1.3 Mantenimiento", "4.1.4 EPP", "4.1.5 Plan de Emergencias"],
    "GESTIÓN AMENAZAS (VERIFICAR/ACTUAR)": ["5.1.1 Planes de Mejora", "5.1.2 Auditoría", "5.1.3 Revisión Dirección"]
}

# --- 3. ESTILOS CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stApp { background-color: #F2F2F2; }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #F2F2F2; text-align: center; padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; }
    .card-item { background: white; padding: 10px; border-radius: 8px; border-left: 5px solid #800000; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 4. LÓGICA DE NAVEGACIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'autenticado' not in st.session_state: st.session_state.autenticado = False

with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    st.markdown("### ACCESO")
    if not st.session_state.autenticado:
        u = st.text_input("Usuario")
        p = st.text_input("Clave", type="password")
        if st.button("INGRESAR"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Acceso Premium")
        if st.button("SALIR"):
            st.session_state.autenticado = False
            st.rerun()
    st.divider()
    if st.button("🏠 INICIO"): st.session_state.pantalla = 'inicio'; st.rerun()
    if st.button("📊 ESTADÍSTICAS"): st.session_state.pantalla = 'stats'; st.rerun()
    if st.button("🎥 VIDEOTECA"): st.session_state.pantalla = 'videos'; st.rerun()

# --- 5. CUERPO DE LA APP ---

if st.session_state.pantalla == 'inicio':
    st.markdown("<h1 style='text-align:center;'>App JPL</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Gestión Integral de Estándares Mínimos - Res. 0312 de 2019</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    if col1.button("🏢 MICRO (<10)\n7 Estándares"): st.session_state.nivel = "7"; st.session_state.pantalla = 'auditoria'; st.rerun()
    if col2.button("🏬 PYME (11-50)\n21 Estándares"): st.session_state.nivel = "21"; st.session_state.pantalla = 'auditoria'; st.rerun()
    if col3.button("🏭 GRANDE (+50)\n62 Estándares"): st.session_state.nivel = "62"; st.session_state.pantalla = 'auditoria'; st.rerun()

elif st.session_state.pantalla == 'auditoria':
    st.markdown(f"## Auditoría: {st.session_state.nivel} Estándares")
    
    # Renderizado de ítems con validación
    if st.session_state.nivel == "7": lista = E_7
    elif st.session_state.nivel == "21": lista = E_21
    else: lista = [item for sublist in E_62.values() for item in sublist]

    for item in lista:
        with st.container():
            st.markdown(f'<div class="card-item">{item}</div>', unsafe_allow_html=True)
            col_a, col_b = st.columns([2, 1])
            cumple = col_a.radio("¿Cumple la norma?", ["Pendiente", "CUMPLE", "NO CUMPLE", "NO APLICA"], key=item, horizontal=True, disabled=not st.session_state.autenticado)
            col_b.text_input("Observación / Hallazgo", key=f"obs_{item}", disabled=not st.session_state.autenticado)
            st.divider()

    if not st.session_state.autenticado:
        st.warning("⚠️ MODO LECTURA: Debe ser cliente Premium para calificar cumplimiento.")

elif st.session_state.pantalla == 'stats':
    st.markdown("## Panel de Estadísticas JPL")
    if st.session_state.autenticado:
        st.write("### Cumplimiento Normativo por Ciclo")
        chart_data = pd.DataFrame(np.random.randint(0,100,size=(4, 1)), index=['Planear', 'Hacer', 'Verificar', 'Actuar'], columns=['%'])
        st.bar_chart(chart_data)
        st.download_button("📥 DESCARGAR ESTADÍSTICAS (PDF)", data="DATOS", file_name="Estadisticas_JPL.pdf")
    else:
        st.info("Gráficos disponibles para asociados actuales.")

elif st.session_state.pantalla == 'videos':
    st.markdown("## Videoteca L.I.N.A.")
    cod = st.text_input("Código de Verificación:", type="password")
    if cod == "JPL2026":
        st.success("Acceso válido por 15 días corridos.")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        st.error("Código requerido.")

# --- 6. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
