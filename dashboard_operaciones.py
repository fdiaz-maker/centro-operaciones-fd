
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Centro de Operaciones", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Centro de Operaciones")
app_mode = st.sidebar.selectbox("Selecciona un Panel", ["Planta Industrial", "Emprendimientos", "Radar de Inversiones"])

if app_mode == "Planta Industrial":
    st.header("🏭 Control de Producción")
    col1, col2, col3 = st.columns(3)
    col1.metric("OEE Actual (Turno)", "88.5%", "2.1%")
    col2.metric("Eficiencia Línea 166ml", "92%", "-0.5%")
    col3.metric("Tiempo de Detención", "12 min", "-15 min", delta_color="inverse")
    
    with st.expander("Abrir Asistente de Falla"):
        if st.button("Solicitar Análisis a IA"):
            st.info("**Reporte Preliminar:** Falla en sellado detectada. Verificar temperatura de mordazas.")

elif app_mode == "Emprendimientos":
    st.header("🚀 Gestión de Proyectos")
    tab1, tab2 = st.tabs(["🍺 La Capital (Cerveza)", "🐈 Felinus (Gatos)"])
    with tab1:
        st.subheader("Monitoreo Cold Crash")
        st.success("Estado: Cold Crash estable a 2.0°C. Clarificación en curso.")
    with tab2:
        st.subheader("Calculadora de Costeo")
        carne = st.number_input("Precio Carne/kg ($)", value=4500)
        st.metric("Costo Proyectado", f"${carne*0.7}")

elif app_mode == "Radar de Inversiones":
    st.header("📈 Radar Portafolio")
    st.write("Análisis de rentabilidad por dividendos activo.")
