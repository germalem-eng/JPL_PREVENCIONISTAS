import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="App JPL - Gestión Técnica SST", layout="wide")

# --- 2. BASE DE DATOS Y LÓGICA DE TIEMPO ---
# Simulación de cumplimiento histórico para la línea de tiempo
fechas = pd.date_range(start="2026-01-01", periods=5, freq='M').strftime('%Y-%m').tolist()
historial_ejemplo = [30, 45, 58, 72, 85]

# --- 3. ESTILOS CSS ---
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
        border-radius: 20px;
        border: 1px solid #A9A9A9;
    }

    .stApp { background-color: #F8F9FA; }
    
    /* Alertas con Diseño de Línea de Tiempo */
    .timeline-box {
        border-left: 4px solid #800000;
        padding-left: 20px;
        margin: 20px 0;
        background: #ffffff;
        border-radius: 0 10px 10px 0;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }

    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background: #F2F2F2; text-align: center; padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; }
</style>
""", unsafe_allow_html=True)

# --- 4. ESTADO DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'respuestas' not in st.session_state: st.session_state.respuestas = {}
if 'autenticado' not in st.session_state: st.session_state.autenticado = False

# --- 5. SIDEBAR ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    if not st.session_state.autenticado:
        u = st.text_input("Admin")
        p = st.text_input("Pass", type="password")
        if st.button("ACCEDER"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Modo Edición: Activo")
        if st.button("SALIR"): st.session_state.autenticado = False; st.rerun()
    
    st.divider()
    if st.button("🏠 VISTA PRINCIPAL"): st.session_state.pantalla = 'inicio'; st.rerun()

# --- 6. PANTALLAS ---

if st.session_state.pantalla == 'inicio':
    st.title("🛡️ Panel de Diagnóstico y Alerta Temprana")
    st.info("Seleccione el tamaño de su organización para evaluar el cumplimiento de la Resolución 0312.")

    # BOTONES DE EMPRESA (Protagonistas arriba)
    c1, c2, c3 = st.columns(3)
    if c1.button("🏢 MICRO (7 ítems)"): st.session_state.nivel = "7"; st.session_state.pantalla = 'diagnostico'; st.rerun()
    if c2.button("🏬 PYME (21 ítems)"): st.session_state.nivel = "21"; st.session_state.pantalla = 'diagnostico'; st.rerun()
    if c3.button("🏭 GRANDE (62 ítems)"): st.session_state.nivel = "62"; st.session_state.pantalla = 'diagnostico'; st.rerun()

    st.divider()

    # PLANES MODERADOS (Abajo como información de servicio)
    st.markdown("### 📋 Servicios de Soporte Técnico")
    p1, p2, p3, p4 = st.columns(4)
    planes = [("Micro", "$30.000"), ("Pyme", "$60.000"), ("Grande", "$100.000"), ("Corporativo", "Convenio")]
    for i, (n, v) in enumerate(planes):
        with [p1, p2, p3, p4][i]:
            st.markdown(f"**Plan {n}**\n\n{v}\n\n[Consultar vía WhatsApp](https://wa.me/573000000000)")

elif st.session_state.pantalla == 'diagnostico':
    nivel = st.session_state.nivel
    st.header(f"Diagnóstico en Tiempo Real: Nivel {nivel}")
    
    # 📉 LÍNEA DE TIEMPO DE CUMPLIMIENTO (Estadística de Alerta)
    st.subheader("⏳ Evolución del Cumplimiento (Línea de Tiempo)")
    chart_data = pd.DataFrame({"Mes": fechas, "Cumplimiento %": historial_ejemplo})
    st.line_chart(chart_data, x="Mes", y="Cumplimiento %")

    # SISTEMA DE AUTO-REFRESCO DE ALERTAS
    # Contamos respuestas actuales
    items = ["Ítem 1", "Ítem 2", "Ítem 3", "Ítem 4", "Ítem 5"] # Simplificado para demo
    cumplidos = sum(1 for it in items if st.session_state.respuestas.get(f"{nivel}_{it}") == "CUMPLE")
    porcentaje = round((cumplidos / len(items)) * 100, 2)

    # Bloque de Alerta Dinámica
    if porcentaje < 60:
        st.markdown(f"""<div class='timeline-box' style='border-left-color:red;'>
            <h3 style='color:red;'>🔴 FASE ACTUAL: RIESGO CRÍTICO ({porcentaje}%)</h3>
            <p><b>Acción inmediata:</b> Ejecutar Plan de Emergencia y reporte ARL.</p>
        </div>""", unsafe_allow_html=True)
    elif 60 <= porcentaje < 85:
        st.markdown(f"""<div class='timeline-box' style='border-left-color:orange;'>
            <h3 style='color:orange;'>🟡 FASE ACTUAL: MODERADO ({porcentaje}%)</h3>
            <p><b>Acción:</b> Revisar hallazgos en la Matriz de Peligros.</p>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""<div class='timeline-box' style='border-left-color:green;'>
            <h3 style='color:green;'>🟢 FASE ACTUAL: ACEPTABLE ({porcentaje}%)</h3>
            <p><b>Acción:</b> Mejora continua y auditoría preventiva.</p>
        </div>""", unsafe_allow_html=True)

    # FORMULARIO (Se refresca solo al marcar)
    st.write("### Marque los ítems verificados:")
    for it in items:
        # Al usar on_change o simplemente interactuar, Streamlit refresca los cálculos de arriba
        st.radio(it, ["No verificado", "CUMPLE", "NO CUMPLE"], key=f"{nivel}_{it}", horizontal=True, disabled=not st.session_state.autenticado)

    if st.button("⬅️ VOLVER"): st.session_state.pantalla = 'inicio'; st.rerun()

# --- 7. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
