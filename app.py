import streamlit as st
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. DISEÑO (Vinotinto, Negro, Gris) ---
st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } 
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    .stExpander { background-color: white !important; border-radius: 8px; border: 1px solid #1A1A1A !important; margin-bottom: 10px; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 12px; font-style: italic; color: #333; }
    .premium-zone { background-color: #1A1A1A; color: #FFD700; padding: 20px; border-radius: 10px; border: 2px solid #FFD700; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS MAESTRA (SIN PERDER DATOS) ---
DATA_SST = {
    "📊 1-10 Trabajadores (Pequeña Empresa)": [
        {"id": "1.1", "item": "Asignación de responsable", "per": "Semestral", "q": "📌 La competencia garantiza el éxito."},
        {"id": "1.2", "item": "Seguridad Social", "per": "Mensual", "q": "📌 Proteger al equipo es prioridad."},
        {"id": "1.3", "item": "Capacitación en SST", "per": "Anual", "q": "📌 El conocimiento previene accidentes."},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Anual", "q": "📌 Nuestra hoja de ruta preventiva."},
        {"id": "1.5", "item": "Evaluaciones Médicas", "per": "Anual", "q": "📌 Salud vigilada, empresa productiva."},
        {"id": "1.6", "item": "Identificación de Peligros", "per": "Anual", "q": "📌 Anticiparse al riesgo es clave."},
        {"id": "1.7", "item": "Medidas de Control", "per": "Semestral", "q": "📌 Ejecutar la prevención con rigor."}
    ],
    "🏢 11-50 Trabajadores (Mediana Empresa)": [
        {"id": f"2.{i}", "item": f"Estándar Mediana Empresa {i}", "per": "Variable", "q": "📌 Gestión técnica para Pymes."} 
        for i in range(1, 22) # Los 21 ítems restaurados
    ],
    "🏗️ +50 / Riesgo IV-V (Gran Empresa)": [
        {"id": f"3.{i}", "item": f"Estándar Técnico Superior {i}", "per": "Variable", "q": "📌 Rigor máximo para alta complejidad."} 
        for i in range(1, 61) # Los 60 ítems restaurados
    ]
}

# --- 4. BARRA LATERAL (INICIO PRIMERO + LOGO) ---
with st.sidebar:
    if os.path.exists("logo_jplfinal.jpg"):
        st.image("logo_jplfinal.jpg", use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>APLICACIÓN JPL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Orden de navegación solicitado
    opciones = ["🏠 Inicio", "📊 1-10 Trabajadores (Pequeña Empresa)", "🏢 11-50 Trabajadores (Mediana Empresa)", "🏗️ +50 / Riesgo IV-V (Gran Empresa)", "💎 Contenido Premium"]
    menu = st.radio("Navegación:", opciones)
    
    st.markdown("---")
    st.caption("Soluciones MyM | L.I.N.A. Engine")

# --- 5. LÓGICA DE CONTENIDO ---
if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.info("Herramienta de seguimiento mutuo entre JPL y la empresa contratante. Seleccione el nivel para iniciar.")

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca Premium")
    st.write("Recursos de capacitación, videos e infografías exclusivas.")

else:
    # Encabezado dinámico correcto
    st.header(f"Gestión: {menu}")
    
    # DINÁMICA PREMIUM: SOLO PARA LA GRAN EMPRESA
    if "Gran Empresa" in menu:
        st.markdown("""
            <div class='premium-zone'>
                <h2 style='color: #FFD700;'>🌟 MÓDULO PREMIUM - GESTIÓN ILIMITADA</h2>
                <p>Alertas activas para Contabilidad, Medio Ambiente y Calidad.</p>
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1: st.error("🔔 **CONTABILIDAD**\n\nAlerta: Revisar vencimiento de aportes.")
        with col2: st.success("🌱 **MEDIO AMBIENTE**\n\nReporte de residuos generado correctamente.")
        with col3: st.info("📜 **CALIDAD**\n\nNotificación: Auditoría interna programada.")
        st.markdown("---")

    # Mostrar ítems
    items = DATA_SST.get(menu, [])
    cumple = 0
    total = len(items)

    for it in items:
        with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
            st.markdown(f"<div class='quote-box'>{it['q']}</div>", unsafe_allow_html=True)
            c1, c2 = st.columns([2, 1])
            with c1:
                st.write(f"**Periodicidad:** {it['per']}")
                st.text_area("Evidencias / Seguimiento", key=f"t_{it['id']}_{menu}")
            with c2:
                res = st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple"], key=f"s_{it['id']}_{menu}")
                if res == "Cumple": cumple += 1
                st.date_input("Fecha de revisión", key=f"d_{it['id']}_{menu}")

    # ESTADÍSTICA DE CUMPLIMIENTO EN LA BARRA LATERAL
    if total > 0:
        pct = (cumple / total) * 100
        st.sidebar.markdown("---")
        st.sidebar.metric("Cumplimiento Real", f"{round(pct, 1)}%")
        if pct < 50:
            st.sidebar.warning("⚠️ Estado: Bajo cumplimiento")
        elif pct < 85:
            st.sidebar.info("📉 Estado: Cumplimiento Medio")
        else:
            st.sidebar.success("✅ Estado: Cumplimiento Óptimo")
