import streamlit as st
import os

# --- 1. CONFIGURACIÓN E IDENTIDAD VISUAL ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } 
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    .stExpander { background-color: white !important; border-radius: 8px; border: 1px solid #1A1A1A !important; margin-bottom: 10px; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 12px; font-style: italic; color: #333; }
    .premium-alert-card { background-color: #1A1A1A; color: #FFD700; padding: 20px; border-radius: 10px; border: 2px solid #FFD700; margin-bottom: 25px; text-align: center; }
    .stat-box { background-color: #eee; padding: 10px; border-radius: 5px; border: 1px solid #ccc; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DATOS MAESTRA (7, 21 Y 60 ÍTEMS - PROTECCIÓN TOTAL) ---
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
        {"id": f"2.{i}", "item": f"Estándar Mediana Empresa {i}", "per": "Trimestral", "q": "📌 Gestión técnica para Pymes."} 
        for i in range(1, 22)
    ],
    "🏗️ +50 / Riesgo IV-V (Gran Empresa)": [
        {"id": f"3.{i}", "item": f"Estándar Técnico Superior {i}", "per": "Variable", "q": "📌 Máximo rigor para alta complejidad."} 
        for i in range(1, 61)
    ]
}

# --- 3. BARRA LATERAL (ORDEN DE NAVEGACIÓN Y LOGO) ---
with st.sidebar:
    if os.path.exists("logo_jplfinal.jpg"):
        st.image("logo_jplfinal.jpg", use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>APLICACIÓN JPL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    opciones = [
        "🏠 Inicio", 
        "📊 1-10 Trabajadores (Pequeña Empresa)", 
        "🏢 11-50 Trabajadores (Mediana Empresa)", 
        "🏗️ +50 / Riesgo IV-V (Gran Empresa)", 
        "💎 Contenido Premium"
    ]
    menu = st.radio("Navegación:", opciones)
    
    st.markdown("---")
    st.caption("Soluciones MyM | L.I.N.A. Engine")

# --- 4. LÓGICA DE CONTENIDO ---
if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.info("Plataforma de auditoría compartida. Seleccione su nivel para iniciar el plan de seguimiento.")

elif menu == "💎 Contenido Premium":
    st.header("Biblioteca de Recursos Premium")
    st.info("Contenido exclusivo para planes corporativos: Videos, Infografías y Formatos.")

else:
    st.header(f"Gestión: {menu}")
    
    # --- DINÁMICA PREMIUM EXCLUSIVA PARA GRAN EMPRESA (+50) ---
    if "Gran Empresa" in menu:
        st.markdown("""
            <div class='premium-alert-card'>
                <h2 style='color: #FFD700;'>🌟 MÓDULO PREMIUM: SEGUIMIENTO ILIMITADO</h2>
                <p>Notificaciones Activas: Contabilidad | Medio Ambiente | Calidad</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Alertas de futuro en la app (Notificaciones en tiempo real)
        col1, col2, col3 = st.columns(3)
        with col1: 
            st.error("🔔 **CONTABILIDAD**\n\nAlerta: Revisión de aportes y nómina.")
        with col2: 
            st.success("🌱 **MEDIO AMBIENTE**\n\nReporte residuos: Al día.")
        with col3: 
            st.info("📜 **CALIDAD**\n\nAuditoría interna programada.")
        st.markdown("---")

    # Listado de ítems según el nivel
    items = DATA_SST.get(menu, [])
    cumple = 0
    total = len(items)

    for it in items:
        with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
            st.markdown(f"<div class='quote-box'>{it['q']}</div>", unsafe_allow_html=True)
            c1, c2 = st.columns([2, 1])
            with c1:
                st.write(f"**Periodicidad:** {it['per']}")
                st.text_area("Evidencias / Hallazgos", key=f"t_{it['id']}_{menu}")
            with c2:
                res = st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple"], key=f"s_{it['id']}_{menu}")
                if res == "Cumple": cumple += 1
                st.date_input("Revisión", key=f"d_{it['id']}_{menu}")

    # --- ESTADÍSTICA DE CUMPLIMIENTO (VISIÓN DEL CLIENTE Y JPL) ---
    if total > 0:
        pct = (cumple / total) * 100
        st.sidebar.markdown("---")
        st.sidebar.subheader("📊 Cumplimiento")
        st.sidebar.metric("Porcentaje Actual", f"{round(pct, 1)}%")
        
        # Lógica de aviso de cumplimiento bajo/óptimo
        if pct < 50:
            st.sidebar.error("⚠️ Alerta: Bajo cumplimiento del sistema.")
        elif pct < 85:
            st.sidebar.warning("📉 Seguimiento: Cumplimiento Medio.")
        else:
            st.sidebar.success("✅ Estado: Cumplimiento Óptimo.")
        
        st.sidebar.write("*(Datos compartidos vía correo entre JPL y Contratante)*")
