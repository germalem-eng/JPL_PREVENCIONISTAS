import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="App JPL - Diagnóstico 0312", layout="wide")

# --- 2. BASE DE DATOS TÉCNICA (CON PESOS PORCENTUALES) ---
# Simulamos los pesos de la norma para el diagnóstico
ESTANDARES = {
    "7": ["Responsable", "Recursos", "Seguridad Social", "Plan Trabajo", "Médicos", "Peligros", "Medidas Control"],
    "21": ["Responsable", "Recursos", "COPASST", "Comité Convivencia", "Capacitación", "Inducción", "Plan Trabajo", "Archivo", "Sociodemográfico", "P&P", "Médicos", "Reporte AT/EL", "Peligros", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Revisión Dirección", "Investigación AT", "Acciones Mejora", "Auditoría"],
    "62": ["Ciclo PHVA Completo - 62 Estándares"]
}

# --- 3. ESTILOS CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Botones Gris Plata */
    div.stButton > button { background-color: #C0C0C0 !important; color: #333 !important; font-weight: bold; }
    .stApp { background-color: #F2F2F2; }
    
    /* Estilos de Alerta */
    .alerta-critica { padding: 20px; background-color: #ff4b4b; color: white; border-radius: 10px; border-left: 10px solid #800000; margin: 10px 0; }
    .alerta-aceptable { padding: 20px; background-color: #28a745; color: white; border-radius: 10px; margin: 10px 0; }
    .card-diagnostico { background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 10px; border-left: 5px solid #C0C0C0; }
    
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background: #F2F2F2; text-align: center; padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; }
</style>
""", unsafe_allow_html=True)

# --- 4. LÓGICA DE DIAGNÓSTICO ---
if 'respuestas' not in st.session_state: st.session_state.respuestas = {}
if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'

def calcular_diagnostico(nivel):
    lista = ESTANDARES[nivel]
    total = len(lista)
    cumplidos = sum(1 for item in lista if st.session_state.respuestas.get(f"{nivel}_{item}") == "CUMPLE")
    porcentaje = (cumplidos / total) * 100 if total > 0 else 0
    return round(porcentaje, 2)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    st.header("ACCESO")
    if not st.session_state.autenticado:
        u = st.text_input("Usuario")
        p = st.text_input("Clave", type="password")
        if st.button("INGRESAR"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Admin: Gerardo")
        if st.button("SALIR"): st.session_state.autenticado = False; st.rerun()
    
    st.divider()
    if st.button("🏠 PANEL DE INICIO"): st.session_state.pantalla = 'inicio'; st.rerun()
    if st.button("🎥 VIDEOTECA"): st.session_state.pantalla = 'videos'; st.rerun()

# --- 6. CUERPO DE LA APP (DIAGNÓSTICO Y ALERTAS) ---

if st.session_state.pantalla == 'inicio':
    st.title("App JPL - Herramienta Diagnóstica Res. 0312")
    
    # SECCIÓN DE PRECIOS PREMIUM
    st.markdown("### 💎 Planes de Afiliación")
    c1, c2, c3, c4 = st.columns(4)
    planes = [("Micro", "$30.000"), ("Pyme", "$60.000"), ("Grande", "$100.000"), ("Premium", "$300.000")]
    for i, (n, p) in enumerate(planes):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"<div style='text-align:center; background:white; padding:15px; border-radius:10px; border:1px solid #C0C0C0;'><h4>{n}</h4><h3 style='color:#800000;'>{p}</h3><a href='https://wa.me/573000000000' style='text-decoration:none;'><button style='width:100%; background:#25D366; color:white; border:none; border-radius:5px; padding:5px;'>WhatsApp</button></a></div>", unsafe_allow_html=True)

    st.divider()
    st.subheader("🚀 Iniciar Diagnóstico de Alerta Temprana")
    col1, col2, col3 = st.columns(3)
    if col1.button("🏢 Diagnóstico Micro (7)"): st.session_state.nivel = "7"; st.session_state.pantalla = 'diagnostico'; st.rerun()
    if col2.button("🏬 Diagnóstico Pyme (21)"): st.session_state.nivel = "21"; st.session_state.pantalla = 'diagnostico'; st.rerun()
    if col3.button("🏭 Diagnóstico Grande (62)"): st.session_state.nivel = "62"; st.session_state.pantalla = 'diagnostico'; st.rerun()

elif st.session_state.pantalla == 'diagnostico':
    nivel = st.session_state.nivel
    st.header(f"Instrumento de Evaluación: Nivel {nivel}")
    
    # CÁLCULO DE ALERTA EN TIEMPO REAL
    puntaje = calcular_diagnostico(nivel)
    
    st.subheader(f"Resultado Actual: {puntaje}%")
    
    # LÓGICA DE ALERTA TEMPRANA (Res. 0312)
    if puntaje < 60:
        st.markdown(f"""<div class='alerta-critica'>
            <h3>🚨 ALERTA TEMPRANA: CRÍTICO</h3>
            <p>El cumplimiento es inferior al 60%. La empresa debe realizar un Plan de Mejora inmediato y enviar reporte a la ARL.</p>
        </div>""", unsafe_allow_html=True)
    elif 60 <= puntaje < 85:
        st.warning("⚠️ ESTADO: MODERADAMENTE ACEPTABLE. Se requiere plan de mejora disponible para el Ministerio.")
    else:
        st.markdown(f"""<div class='alerta-aceptable'>
            <h3>✅ ESTADO: ACEPTABLE</h3>
            <p>Cumplimiento superior al 85%. Mantener acciones preventivas.</p>
        </div>""", unsafe_allow_html=True)

    # LISTADO DIAGNÓSTICO
    st.divider()
    for item in ESTANDARES[nivel]:
        with st.container():
            st.markdown(f"<div class='card-diagnostico'><b>{item}</b></div>", unsafe_allow_html=True)
            res = st.radio("Validación:", ["No Evaluado", "CUMPLE", "NO CUMPLE", "NO APLICA"], key=f"{nivel}_{item}", horizontal=True, disabled=not st.session_state.autenticado)
            st.session_state.respuestas[f"{nivel}_{item}"] = res

    if st.button("Actualizar Diagnóstico"): st.rerun()

# --- 7. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
