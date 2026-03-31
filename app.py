import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="App JPL - Gestión Técnica SST", layout="wide")

# --- 2. BASE DE DATOS Y LÓGICA DE TIEMPO (CORRECCIÓN 'ME') ---
# Corregimos el freq='M' por 'ME' para evitar la advertencia en tu terminal
fechas = pd.date_range(start="2026-01-01", periods=5, freq='ME').strftime('%Y-%m').tolist()
# Datos simulados para la línea de tiempo de cumplimiento
historial_ejemplo = [35, 48, 55, 70, 88]

# --- 3. ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }
    
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Botones Gris Plata Redondeados */
    div.stButton > button { 
        background-color: #C0C0C0 !important; 
        color: #333 !important; 
        border-radius: 15px;
        border: 1px solid #A9A9A9;
        transition: 0.3s;
    }
    div.stButton > button:hover { border-color: #800000; color: #800000 !important; }

    .stApp { background-color: #F8F9FA; }
    
    /* Diseño de la Alerta como Línea de Tiempo */
    .timeline-box {
        border-left: 6px solid #800000;
        padding: 15px 25px;
        margin: 15px 0;
        background: #ffffff;
        border-radius: 0 15px 15px 0;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.05);
    }

    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background: #F2F2F2; text-align: center; padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; }
</style>
""", unsafe_allow_html=True)

# --- 4. ESTADO DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'respuestas' not in st.session_state: st.session_state.respuestas = {}
if 'autenticado' not in st.session_state: st.session_state.autenticado = False

# --- 5. BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    st.markdown("### PANEL ADMINISTRATIVO")
    if not st.session_state.autenticado:
        u = st.text_input("Usuario")
        p = st.text_input("Contraseña", type="password")
        if st.button("ACCEDER"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Gerardo: Sesión Activa")
        if st.button("CERRAR SESIÓN"): st.session_state.autenticado = False; st.rerun()
    
    st.divider()
    if st.button("🏠 VISTA PRINCIPAL"): st.session_state.pantalla = 'inicio'; st.rerun()

# --- 6. PANTALLAS ---

if st.session_state.pantalla == 'inicio':
    st.title("🛡️ Diagnóstico Técnico y Alerta Temprana")
    st.markdown("#### Gestión de Estándares Mínimos - Resolución 0312")
    
    # BOTONES DE EMPRESA (Protagonistas arriba)
    st.write("Seleccione el tamaño de la organización para iniciar evaluación:")
    c1, c2, c3 = st.columns(3)
    if c1.button("🏢 MICRO EMPRESA\n(7 Estándares)"): st.session_state.nivel = "7"; st.session_state.pantalla = 'diagnostico'; st.rerun()
    if c2.button("🏬 PYME\n(21 Estándares)"): st.session_state.nivel = "21"; st.session_state.pantalla = 'diagnostico'; st.rerun()
    if c3.button("🏭 GRAN EMPRESA\n(62 Estándares)"): st.session_state.nivel = "62"; st.session_state.pantalla = 'diagnostico'; st.rerun()

    st.divider()

    # SERVICIOS DE SEGURIDAD (Abajo, moderados)
    st.markdown("### 📋 Soporte y Consultoría JPL")
    p1, p2, p3, p4 = st.columns(4)
    servicios = [
        ("Asesoría Micro", "$30.000"), 
        ("Soporte Pyme", "$60.000"), 
        ("Gestión Grande", "$100.000"), 
        ("Premium", "Consultar")
    ]
    for i, (nombre, valor) in enumerate(servicios):
        with [p1, p2, p3, p4][i]:
            st.markdown(f"**{nombre}**\n\n{valor}\n\n[WhatsApp de Soporte](https://wa.me/573000000000)")

elif st.session_state.pantalla == 'diagnostico':
    nivel = st.session_state.nivel
    st.header(f"Instrumento Diagnóstico: Nivel {nivel}")
    
    # 📉 LÍNEA DE TIEMPO VISUAL
    st.subheader("⏳ Línea de Tiempo: Evolución de Cumplimiento")
    chart_data = pd.DataFrame({"Mes": fechas, "Cumplimiento %": historial_ejemplo})
    st.line_chart(chart_data, x="Mes", y="Cumplimiento %")

    # SISTEMA DE AUTO-REFRESCO DE ALERTAS
    # Definimos los ítems según el nivel
    items_auditoria = {
        "7": ["Persona que diseña SG-SST", "Recursos", "Seguridad Social", "Plan Trabajo", "Evaluaciones Médicas", "Peligros", "Prevención y Control"],
        "21": ["Responsable", "Recursos", "COPASST", "Capacitación", "Evaluación Inicial", "Peligros", "Reporte AT/EL"], # Resumen para demo
        "62": ["Ciclo PHVA Completo - Auditoría Integral"]
    }
    
    lista_actual = items_auditoria.get(nivel, ["Ítem General"])
    cumplidos = sum(1 for it in lista_actual if st.session_state.respuestas.get(f"{nivel}_{it}") == "CUMPLE")
    total_it = len(lista_actual)
    porcentaje = round((cumplidos / total_it) * 100, 2)

    # ALERTA TEMPRANA DINÁMICA (Sin clics adicionales, cambia al marcar)
    color_alerta = "red" if porcentaje < 60 else "orange" if porcentaje < 85 else "green"
    texto_alerta = "RIESGO CRÍTICO" if porcentaje < 60 else "MODERADAMENTE ACEPTABLE" if porcentaje < 85 else "ACEPTABLE"
    
    st.markdown(f"""<div class='timeline-box' style='border-left-color:{color_alerta};'>
        <h3 style='color:{color_alerta};'>{texto_alerta} ({porcentaje}%)</h3>
        <p><b>Diagnóstico:</b> De acuerdo con la Resolución 0312, este puntaje sitúa a la empresa en fase de {'intervención inmediata' if porcentaje < 60 else 'mejora continua'}.</p>
    </div>""", unsafe_allow_html=True)

    # FORMULARIO DE EVALUACIÓN
    st.write("---")
    st.write("### Verificación de Estándares:")
    for it in lista_actual:
        st.radio(f"**Estándar:** {it}", ["Pendiente", "CUMPLE", "NO CUMPLE"], key=f"{nivel}_{it}", horizontal=True, disabled=not st.session_state.autenticado)

    if st.button("⬅️ VOLVER AL PANEL"): st.session_state.pantalla = 'inicio'; st.rerun()

# --- 7. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
