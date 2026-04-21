import streamlit as st
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="APP JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. DISEÑO CORPORATIVO ---
st.markdown("""
    <style>
    .stApp { background-color: #D9D9D9; } 
    [data-testid="stSidebar"] { background-color: #8B0000 !important; border-right: 5px solid #1A1A1A; } 
    [data-testid="stSidebar"] * { color: white !important; }
    .stExpander { background-color: white !important; border-radius: 8px; border: 1px solid #1A1A1A !important; }
    .quote-box { background-color: #F0F0F0; border-left: 5px solid #8B0000; padding: 12px; font-style: italic; }
    .premium-lock { background-color: #1A1A1A; color: #FFD700; padding: 25px; border-radius: 10px; border: 2px solid #FFD700; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS (PROTECCIÓN TOTAL DE 7, 21 Y 60 ÍTEMS) ---
DATA_SST = {
    "📊 1-10 Trabajadores (Pequeña Empresa)": [
        {"id": f"1.{i}", "item": f"Estándar Pequeña {i}", "per": "Mensual", "q": "📌 Esencial."} for i in range(1, 8)
    ],
    "🏢 11-50 Trabajadores (Mediana Empresa)": [
        {"id": f"2.{i}", "item": f"Estándar Mediana {i}", "per": "Trimestral", "q": "📌 Gestión técnica."} for i in range(1, 22)
    ],
    "🏗️ +50 / Riesgo IV-V (Gran Empresa)": [
        {"id": f"3.{i}", "item": f"Estándar Técnico Superior {i}", "per": "Variable", "q": "📌 Rigor máximo."} for i in range(1, 61)
    ]
}

# --- 4. BARRA LATERAL (LOGIN Y NAVEGACIÓN) ---
with st.sidebar:
    if os.path.exists("logo_jplfinal.jpg"):
        st.image("logo_jplfinal.jpg", use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>APLICACIÓN JPL</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # SISTEMA DE LOGIN PARA PREMIUM
    st.markdown("### 🔐 Acceso Privado")
    pass_cliente = st.text_input("Contraseña de Empresa:", type="password", help="Solicite su clave a JPL")
    
    # Validación de clave (Ejemplo: JPL2026)
    es_premium = (pass_cliente == "JPL2026")
    
    st.markdown("---")
    opciones = ["🏠 Inicio", "📊 1-10 Trabajadores (Pequeña Empresa)", "🏢 11-50 Trabajadores (Mediana Empresa)", "🏗️ +50 / Riesgo IV-V (Gran Empresa)", "💎 Contenido Premium"]
    menu = st.radio("Navegación:", opciones)

# --- 5. LÓGICA DE CONTENIDO ---
if menu == "🏠 Inicio":
    st.title("Bienvenido a APP JPL")
    st.info("Inicie sesión en la barra lateral para acceder a funciones avanzadas.")

elif menu == "🏗️ +50 / Riesgo IV-V (Gran Empresa)":
    if es_premium:
        st.header(f"Gestión: {menu}")
        st.markdown("<div class='premium-lock'>👑 SESIÓN PREMIUM INICIADA - SEGUIMIENTO ILIMITADO</div>", unsafe_allow_html=True)
        
        # Alertas Premium (Solo visibles con login)
        c1, c2, c3 = st.columns(3)
        with c1: st.error("🔔 **CONTABILIDAD**\n\nAlerta de aportes.")
        with c2: st.success("🌱 **AMBIENTE**\n\nReporte al día.")
        with col3 if 'col3' in locals() else c3: st.info("📜 **CALIDAD**\n\nAuditoría lista.")
        
        st.markdown("---")
        # Mostrar los 60 ítems
        items = DATA_SST[menu]
        cumple = 0
        for it in items:
            with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
                res = st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple"], key=f"p_{it['id']}")
                if res == "Cumple": cumple += 1
        
        # Estadística para el cliente
        pct = (cumple / len(items)) * 100
        st.sidebar.metric("Cumplimiento Real", f"{round(pct,1)}%")
    else:
        st.markdown("""
            <div class='premium-lock'>
                <h2>🔓 Módulo Bloqueado</h2>
                <p>La Gran Empresa requiere validación de seguridad por parte de JPL Prevencionistas.</p>
                <p><b>Por favor, ingrese la contraseña en la barra lateral.</b></p>
            </div>
            """, unsafe_allow_html=True)

elif menu == "💎 Contenido Premium":
    if es_premium:
        st.header("Biblioteca Premium")
        st.write("Acceso a videos e infografías exclusivas.")
    else:
        st.warning("Debe ingresar la contraseña de cliente para ver este contenido.")

else:
    # Pequeña y Mediana empresa siguen accesibles de forma normal
    st.header(f"Gestión: {menu}")
    items = DATA_SST.get(menu, [])
    for it in items:
        with st.expander(f"📍 ÍTEM {it['id']} - {it['item']}"):
            st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple"], key=f"std_{it['id']}")
