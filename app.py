import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="JPL Gestion SST", layout="wide", page_icon="🛡️")

# --- ESTILOS CSS (Solución definitiva a los botones invisibles) ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #8B0000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: white !important;
        color: #8B0000 !important;
        font-weight: bold !important;
        border: 2px solid #000000 !important;
    }
    .main { background-color: #f5f5f5; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (LOGO Y NAVEGACIÓN) ---
with st.sidebar:
    st.image("LOGO JPL FINAL.jpl.jpg", use_column_width=True)
    st.title("Panel de Control")
    opcion = st.radio("Seleccione el Segmento:", 
        ["Inicio", "1-10 Trab. (Riesgo I,II,III)", "11-50 Trab. (Riesgo I,II,III)", "Más de 50 o Riesgo IV/V"])

# --- LÓGICA DE INICIO ---
if opcion == "Inicio":
    st.title("Bienvenido al Sistema de Gestión L.I.N.A.")
    st.subheader("Soluciones MyM & JPL Prevencionistas")
    st.write("Seleccione una categoría en el menú lateral para iniciar la evaluación de estándares mínimos.")

# --- MÓDULO 1: 10 O MENOS TRABAJADORES ---
elif opcion == "1-10 Trab. (Riesgo I,II,III)":
    st.header("Evaluación: 10 o menos trabajadores (Riesgo I, II, III)")
    
    # Ejemplo de estructura basada en tu archivo Word
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        st.markdown("**1. Asignación de persona que diseña el SG-SST**")
        st.caption("Periodicidad: Semestral")
    with col2:
        estado = st.selectbox("Estado", ["Cumple", "No Cumple", "No Aplica"], key="e1")
    with col3:
        st.date_input("Próxima Revisión", key="d1")
    
    st.text_area("Observaciones técnicas:", placeholder="Escriba aquí los hallazgos...", key="obs1")

# (Continuaremos agregando los demás módulos según los documentos Word)
