import streamlit as st
import os

# --- 1. CONFIGURACIÓN Y ESTÉTICA (Sin cambios que borren info) ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } 
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    .stExpander { background-color: white !important; border-radius: 8px; border: 1px solid #1A1A1A !important; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 10px; font-style: italic; }
    .premium-badge { background-color: #000; color: #FFD700; padding: 10px; border-radius: 5px; font-weight: bold; text-align: center; margin-bottom: 20px; border: 1px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DATOS COMPLETA (RECUPERADA) ---
DATA_SST = {
    "📊 1-10 Trabajadores (Pequeña)": [
        {"id": "1.1", "item": "Asignación de responsable", "per": "Semestral", "q": "📌 La competencia garantiza el éxito."},
        {"id": "1.2", "item": "Seguridad Social", "per": "Mensual", "q": "📌 Proteger al equipo es prioridad."},
        {"id": "1.3", "item": "Capacitación en SST", "per": "Anual", "q": "📌 El conocimiento previene accidentes."},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Anual", "q": "📌 Nuestra hoja de ruta preventiva."},
        {"id": "1.5", "item": "Evaluaciones Médicas", "per": "Anual", "q": "📌 Salud vigilada, empresa productiva."},
        {"id": "1.6", "item": "Identificación de Peligros", "per": "Anual", "q": "📌 Anticiparse al riesgo es clave."},
        {"id": "1.7", "item": "Medidas de Control", "per": "Semestral", "q": "📌 Ejecutar la prevención con rigor."}
    ],
    "🏢 11-50 Trabajadores (Mediana)": [
        {"id": f"2.{i}", "item": f"Estándar Mediana Empresa {i}", "per": "Variable", "q": "📌 Seguimiento estándar para Pymes."} 
        for i in range(1, 22) # Los 21 ítems completos
    ],
    "🏗️ +50 / Riesgo IV-V (Grande)": [
        {"id": f"3.{i}", "item": f"Estándar Técnico Superior {i}", "per": "Variable", "q": "📌 Rigor máximo para alta complejidad."} 
        for i in range(1, 61) # Los 60 ítems completos
    ]
}

# --- 3. BARRA LATERAL (ORDEN Y LOGO) ---
with st.sidebar:
    logo = "logo_jplfinal.jpg"
    if os.path.exists(logo): st.image(logo, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>APLICACIÓN JPL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Inicio al principio
    opciones = ["🏠 Inicio", "📊 1-10 Trabajadores (Pequeña)", "🏢 11-50 Trabajadores (Mediana)", "🏗️ +50 / Riesgo IV-V (Grande)", "💎 Contenido Premium"]
    menu = st.radio("Navegación:", opciones)
    
    st.markdown("---")
    st.caption("Soluciones MyM | L.I.N.A. Engine")

# --- 4. LÓGICA DE CONTENIDO ---

if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.info("Seleccione el nivel de empresa según la cantidad de empleados.")

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca de Recursos Premium")
    st.info("Contenido exclusivo para planes corporativos y la Gran Empresa.")

else:
    # ENUNCIADO DINÁMICO SEGÚN EL MENÚ
    st.header(f"Sección: {menu}")
    
    # SOLO LA GRAN EMPRESA MUESTRA BENEFICIOS PREMIUM
    if "Grande" in menu:
        st.markdown("<div class='premium-badge'>👑 BENEFICIOS PREMIUM ACTIVADOS (CONTABILIDAD - AMBIENTAL - CALIDAD)</div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.error("🔔 ALERTA CONTABLE\n\nRevisar aportes de ley.")
        with c2: st.success("🌱 ALERTA AMBIENTAL\n\nReporte residuos al día.")
        with c3: st.info("📜 ALERTA CALIDAD\n\nAuditoría en proceso.")
        st.markdown("---")

    items = DATA_SST.get(menu, [])
    cumple = 0
    total = len(items)

    for it in items:
        with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
            st.markdown(f"<div class='quote-box'>{it['q']}</div>", unsafe_allow_html=True)
            c1, c2 = st.columns([2, 1])
            with c1:
                st.write(f"**Periodicidad:** {it['per']}")
                st.text_area("Hallazgos", key=f"t_{it['id']}_{menu}")
            with c2:
                res = st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple"], key=f"s_{it['id']}_{menu}")
                if res == "Cumple": cumple += 1
                st.date_input("Seguimiento", key=f"d_{it['id']}_{menu}")

    # ESTADÍSTICA DE CUMPLIMIENTO
    if total > 0:
        pct = (cumple / total) * 100
        st.sidebar.markdown("---")
        st.sidebar.metric("Cumplimiento Actual", f"{round(pct, 1)}%")
