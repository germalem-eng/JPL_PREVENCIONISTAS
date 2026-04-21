import streamlit as st
import os

# --- 1. CONFIGURACIÓN Y ESTÉTICA ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } 
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    .stExpander { background-color: white !important; border-radius: 8px; border: 1px solid #1A1A1A !important; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 10px; font-style: italic; }
    .premium-tag { background-color: #000; color: #FFD700; padding: 5px; border-radius: 5px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BARRA LATERAL (ORDEN CORRECTO) ---
with st.sidebar:
    logo = "logo_jplfinal.jpg"
    if os.path.exists(logo): st.image(logo, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>APLICACIÓN JPL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Inicio al principio
    opciones = ["🏠 Inicio", "📊 1-10 Trabajadores", "🏢 11-50 Trabajadores", "🏗️ +50 / Riesgo IV-V", "💎 Contenido Premium"]
    menu = st.radio("Navegación:", opciones)
    
    st.markdown("---")
    st.caption("Soluciones MyM | Ecosistema L.I.N.A.")

# --- 3. LÓGICA POR NIVELES ---

if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.info("Seleccione el nivel de su empresa para iniciar.")

elif menu == "🏗️ +50 / Riesgo IV-V":
    st.markdown("<div class='premium-tag'>🌟 ACCESO PREMIUM ACTIVADO</div>", unsafe_allow_html=True)
    st.header("Evaluación: Gran Empresa (SST Ilimitado)")
    
    # Alertas Premium exclusivas para este nivel
    col1, col2, col3 = st.columns(3)
    with col1: st.error("🔔 CONTABILIDAD\n\nRevisión de aportes.")
    with col2: st.success("🌱 AMBIENTAL\n\nResiduos al día.")
    with col3: st.info("📜 CALIDAD\n\nAuditoría en 5 días.")
    
    st.markdown("---")
    # Carga de los 60 ítems
    for i in range(1, 61):
        with st.expander(f"📍 ÍTEM 3.{i} - Estándar Técnico de Alta Complejidad"):
            st.write("📌 *Frase de seguimiento JPL: El rigor en este punto es vital para la gran empresa.*")
            st.selectbox("Resultado", ["Pendiente", "Cumple", "No Cumple"], key=f"gran_{i}")
            st.text_area("Evidencia / Observación", key=f"obs_{i}")

elif menu == "🏢 11-50 Trabajadores":
    st.header("Evaluación: Media Empresa (Pymes)")
    # Solo los 21 ítems, sin alertas premium
    for i in range(1, 22):
        with st.expander(f"📍 ÍTEM 2.{i} - Estándar para Media Empresa"):
            st.write("📌 *Seguimiento estándar para el cumplimiento de la norma.*")
            st.selectbox("Resultado", ["Pendiente", "Cumple", "No Cumple"], key=f"med_{i}")

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca de Recursos Premium")
    st.info("Disponible para empresas de Nivel +50 y Consultores JPL.")
    # Aquí irían los videos e infografías que mencionamos antes
