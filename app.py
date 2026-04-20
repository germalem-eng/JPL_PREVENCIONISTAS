import streamlit as st
import os

# --- 1. CONFIGURACIÓN E IDENTIDAD ---
st.set_page_config(page_title="JPL - Gestión SST", layout="wide", page_icon="🛡️")

# Estilos corregidos para visibilidad total
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #8B0000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button { background-color: white !important; color: #8B0000 !important; border: 2px solid black; font-weight: bold; width: 100%; }
    .stExpander { border: 1px solid #ddd; border-radius: 10px; margin-bottom: 10px; background-color: white; }
    p, span, label { color: #333 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DATOS DE ESTÁNDARE (Según tus archivos Word) ---
DATA_SST = {
    "1-10 Trabajadores": [
        {"id": "1.1", "item": "Asignación de persona que diseña el SG-SST", "per": "Semestral", "tip": "Licencia SST y curso 50h."},
        {"id": "1.2", "item": "Afiliación al Sistema de Seguridad Social Integral", "per": "Cuatrimestral", "tip": "Pagos planilla y contratistas."},
        {"id": "1.3", "item": "Capacitación en SST", "per": "Cuatrimestral", "tip": "Evidencias y listados."},
        {"id": "1.4", "item": "Plan de Trabajo Anual", "per": "Semestral", "tip": "Firma de gerencia."},
        {"id": "1.5", "item": "Evaluaciones Médicas Ocupacionales", "per": "Anual", "tip": "Certificados de aptitud."},
        {"id": "1.6", "item": "Identificación de Peligros y Riesgos", "per": "Semestral", "tip": "Matriz de riesgos actualizada."},
        {"id": "1.7", "item": "Medidas de Prevención y Control", "per": "Semestral", "tip": "Ejecución de actividades."}
    ],
    "11-50 Trabajadores": [
        {"id": "2.1", "item": "Asignación de responsable del SG-SST", "per": "Semestral", "tip": "Hoja de vida y acta de designación."},
        {"id": "2.2", "item": "Recursos para el Sistema de Gestión", "per": "Anual", "tip": "Presupuesto firmado."},
        {"id": "2.3", "item": "Conformación y funcionamiento del COPASST", "per": "Cuatrimestral", "tip": "Actas de reunión mensual."},
        {"id": "2.4", "item": "Conformación del Comité de Convivencia", "per": "Cuatrimestral", "tip": "Gestión de acoso laboral."}
    ]
}

# --- 3. INTERFAZ LATERAL ---
with st.sidebar:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", use_container_width=True)
    else:
        st.warning("⚠️ Sube 'logo.jpg' a GitHub")
    
    st.title("L.I.N.A. v2.0")
    menu = st.radio("Nivel de Empresa:", ["Inicio", "1-10 Trabajadores", "11-50 Trabajadores", "+50 o Riesgo IV/V"])
    st.markdown("---")
    st.info("Desarrollado por Soluciones MyM")

# --- 4. LÓGICA PRINCIPAL ---
if menu == "Inicio":
    st.title("Bienvenido al Ecosistema Digital JPL")
    st.markdown("""
    ### Instrucciones para el Auditor:
    1. Seleccione el tipo de empresa en el menú izquierdo.
    2. Evalúe cada ítem desplegando la pestaña correspondiente.
    3. Registre hallazgos y defina la próxima fecha de revisión según la **periodicidad** legal.
    """)
    st.image("https://img.freepik.com/vector-gratis/ilustracion-concepto-analisis-datos_114360-785.jpg", width=400)

else:
    # Carga dinámica de estándares según el menú
    lista_actual = DATA_SST.get(menu, [])
    st.header(f"Evaluación: {menu}")
    
    if not lista_actual:
        st.error("Módulo en construcción según requerimientos del cliente.")
    else:
        # Generación de formularios
        for est in lista_actual:
            with st.expander(f"📌 {est['id']} - {est['item']}"):
                c1, c2, c3 = st.columns([2, 1, 1])
                with c1:
                    st.write(f"**Periodicidad Sugerida:** {est['per']}")
                    st.caption(f"💡 {est['tip']}")
                with c2:
                    st.selectbox("Resultado", ["Cumple", "No Cumple", "Pendiente"], key=f"res_{est['id']}")
                with c3:
                    st.date_input("Próximo Seguimiento", key=f"date_{est['id']}")
                
                st.text_area("Evidencia y Plan de Acción", key=f"txt_{est['id']}", placeholder="Escriba aquí...")

        # Botón final de reporte
        if st.button("Finalizar y Generar Resumen"):
            st.balloons()
            st.success("Diagnóstico completado. Listo para exportación.")
