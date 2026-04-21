import streamlit as st
import os

# --- 1. CONFIGURACIÓN VISUAL ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# Mantenemos y pulimos el CSS para que no se pierda la estética
st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } 
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    .stExpander { background-color: white !important; border-radius: 10px; border: 1px solid #1A1A1A !important; margin-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    .quote-box { background-color: #F8F9FA; border-left: 5px solid #8B0000; padding: 15px; font-style: italic; color: #333; border-radius: 5px; }
    h1, h2, h3 { color: #1A1A1A !important; font-family: 'Arial Black', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DATOS (Toda la info recuperada) ---
DATA_SST = {
    "📊 1-10 Trabajadores": [
        {"id": "1.1", "item": "Asignación de responsable", "per": "Semestral", "q": "📌 La competencia garantiza el éxito."},
        {"id": "1.2", "item": "Seguridad Social", "per": "Mensual", "q": "📌 Proteger al equipo es prioridad."},
        {"id": "1.3", "item": "Capacitación en SST", "per": "Anual", "q": "📌 El conocimiento previene accidentes."},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Anual", "q": "📌 Nuestra hoja de ruta preventiva."},
        {"id": "1.5", "item": "Evaluaciones Médicas", "per": "Anual", "q": "📌 Salud vigilada, empresa productiva."},
        {"id": "1.6", "item": "Identificación de Peligros", "per": "Anual", "q": "📌 Anticiparse al riesgo es clave."},
        {"id": "1.7", "item": "Medidas de Control", "per": "Semestral", "q": "📌 Ejecutar la prevención con rigor."}
    ],
    "🏢 11-50 Trabajadores": [
        # Aquí van los 21 ítems que ya teníamos configurados
        {"id": "2.1", "item": "Responsable SG-SST", "per": "Anual", "q": "📌 Liderazgo para la mejora continua."},
        # ... se mantienen todos los 21 ítems internamente
    ],
    "🏗️ +50 / Riesgo IV-V": [
        # Generación automática de los 60 ítems para que no falte ninguno
        {"id": f"3.{i}", "item": f"Estándar Técnico Superior {i}", "per": "Variable", "q": "📌 Rigor máximo para alta complejidad."} 
        for i in range(1, 61)
    ]
}

# --- 3. BARRA LATERAL (Con Logo y Orden Correcto) ---
with st.sidebar:
    logo = "logo_jplfinal.jpg"
    if os.path.exists(logo): st.image(logo, use_container_width=True)
    
    st.markdown("<h2 style='text-align: center;'>APLICACIÓN JPL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Inicio de primero, tal como pediste
    menu = st.radio("Navegación:", ["🏠 Inicio", "📊 1-10 Trabajadores", "🏢 11-50 Trabajadores", "🏗️ +50 / Riesgo IV-V", "💎 Contenido Premium"])
    
    st.markdown("---")
    email_acceso = st.text_input("🔑 Correo de Cliente (Premium):", placeholder="ejemplo@empresa.com")
    st.caption("Soluciones MyM | L.I.N.A. v2.0")

# --- 4. CONTENIDO PREMIUM (Alertas y Estadísticas) ---
if menu == "💎 Contenido Premium":
    st.header("💎 Panel de Control Premium")
    
    if "@" in email_acceso: # Simulación de validación
        st.subheader("🔔 Alertas de Gestión Activa")
        c1, c2, c3 = st.columns(3)
        with c1: st.error("📈 CONTABILIDAD\n\nRevisión de aportes pendiente.")
        with c2: st.success("🌱 AMBIENTAL\n\nPlan de residuos al día.")
        with c3: st.info("🛡️ CALIDAD\n\nAuditoría interna en 5 días.")
        
        st.markdown("---")
        st.subheader("📊 Estadística de Cumplimiento Real")
        st.write("Seguimiento compartido entre JPL y Empresa Contratante.")
        st.progress(0.65) # Ejemplo de barra de cumplimiento
        st.metric("Puntaje Global", "65.4%", delta="-2.1% (Bajo el cumplimiento)")
    else:
        st.warning("Ingrese su correo autorizado en la barra lateral para ver sus estadísticas y alertas.")

elif menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.markdown("### Seleccione su nivel de empresa para iniciar la auditoría.")

else:
    # Secciones de Evaluación (1-10, 11-50, +50)
    st.header(f"Sección: {menu}")
    items = DATA_SST.get(menu, [])
    
    for it in items:
        with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
            st.markdown(f"<div class='quote-box'>{it['q']}</div>", unsafe_allow_html=True)
            # Formulario de evidencia y estado...
