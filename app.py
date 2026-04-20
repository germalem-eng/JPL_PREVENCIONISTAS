import streamlit as st
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="JPL - Gestión SST", layout="wide", page_icon="🛡️")

# --- 2. COLORES INSTITUCIONALES (Vinotinto, Gris, Negro) ---
st.markdown("""
    <style>
    /* Fondo principal: Gris muy claro para profesionalismo */
    .stApp {
        background-color: #ECECEC;
    }
    
    /* Barra lateral: Vinotinto JPL con borde Negro */
    [data-testid="stSidebar"] {
        background-color: #8B0000 !important;
        border-right: 4px solid #1A1A1A;
    }
    
    /* Textos en barra lateral: Blanco */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Títulos Principales: Negro Puro */
    h1, h2, h3 {
        color: #000000 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Expanders (Acordeones): Blanco con borde Gris Oxford */
    .stExpander {
        background-color: white !important;
        border: 1px solid #4A4A4A !important;
        border-radius: 5px !important;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
    }

    /* Botones: Negro con Hover en Gris */
    .stButton>button {
        background-color: #1A1A1A !important;
        color: white !important;
        border: none !important;
        border-radius: 4px;
        padding: 0.6rem 1rem;
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #4A4A4A !important;
        border: 1px solid #8B0000 !important;
    }

    /* Labels de formularios: Negro */
    label {
        color: #1A1A1A !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL Y LOGOTIPO ---
with st.sidebar:
    # USAMOS EL NOMBRE EXACTO QUE ME DISTE: logo_jplfinal.jpg
    nombre_archivo_logo = "logo_jplfinal.jpg"
    
    if os.path.exists(nombre_archivo_logo):
        st.image(nombre_archivo_logo, use_container_width=True)
    else:
        st.error(f"❌ No se encuentra: {nombre_archivo_logo}")
        st.info("Sube el archivo a la raíz de GitHub con ese nombre exacto.")
    
    st.markdown("<hr style='border: 0.5px solid #4A4A4A;'>", unsafe_allow_html=True)
    st.title("L.I.N.A. v2.0")
    
    menu = st.radio(
        "Nivel de Auditoría:",
        ["🏠 Inicio", 
         "📊 1-10 Trabajadores", 
         "🏢 11-50 Trabajadores", 
         "🏗️ +50 Trab. o Riesgo IV/V"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("Desarrollado por Soluciones MyM")
    st.caption("Soporte Técnico - 2026")

# --- 4. CONTENIDO PRINCIPAL ---

if menu == "🏠 Inicio":
    st.title("Sistema de Gestión de Estándares Mínimos")
    
    # Cuadro de bienvenida con bordes Grises y Vinotinto
    st.markdown(f"""
    <div style="background-color: white; padding: 30px; border-top: 5px solid #8B0000; border-bottom: 5px solid #4A4A4A; border-radius: 5px;">
        <h2 style="color: #1A1A1A; margin-top:0;">Bienvenido, Gerardo</h2>
        <p style="color: #333; font-size: 18px;">Usted está operando la plataforma oficial de <b>JPL Prevencionistas</b>.</p>
        <p style="color: #666;">Seleccione el módulo de auditoría según el tamaño y riesgo de la empresa para iniciar el cargue de evidencias de la Resolución 0312.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.header(f"Sección: {menu}")
    
    # Lógica de carga de datos (Simplificada para prueba)
    items = [
        {"id": "1", "item": "Asignación de responsable", "per": "Semestral"},
        {"id": "2", "item": "Afiliación a Seguridad Social", "per": "Mensual"}
    ]

    for i in items:
        with st.expander(f"📌 {i['id']} - {i['item']}"):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**Periodicidad:** {i['per']}")
                st.text_area("Hallazgos", key=f"h_{menu}_{i['id']}")
            with col2:
                st.selectbox("Resultado", ["Seleccione...", "Cumple", "No Cumple"], key=f"r_{menu}_{i['id']}")
                st.date_input("Revisión", key=f"f_{menu}_{i['id']}")

    if st.button("Finalizar Reporte"):
        st.success("Reporte generado con éxito. Los colores Gris, Negro y Vinotinto se han aplicado.")
        st.balloons()
