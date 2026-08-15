import streamlit as st
import pandas as pd
from datetime import datetime, date

st.set_page_config(
    page_title="Sistema Arquetípico y Gematría Avanzado",
    page_icon="✨",
    layout="wide"
)

st.title("✨ Sistema Integral de Ingeniería Cognitiva y Análisis Arquetípico")
st.markdown("Plataforma avanzada de perfilado profundo basada en Cábala, Gematría, Numerología Teosófica y Correspondencias del Alfabeto Hebreo.")

with st.form("perfil_form_extendido"):
    st.subheader("Parámetros de Análisis de Alta Precisión")
    
    col_a, col_b = st.columns(2)
    with col_a:
        nombre_completo = st.text_input("Nombre Completo del Consultante", value="HERNAN PABLO MABIGLIA")
    with col_b:
        nombre_madre = st.text_input("Nombre de la Madre (Matriz Raíz / Opcional)", value="IVANA BENITEZ")
        
    col1, col2, col3 = st.columns(3)
    with col1:
        fecha_nacimiento = st.date_input(
            "Fecha de Nacimiento", 
            value=datetime(1979, 7, 26),
            min_value=date(1920, 1, 1),
            max_value=date.today()
        )
    with col2:
        hora_nacimiento = st.time_input("Hora de Nacimiento", value=datetime.strptime("17:30", "%H:%M").time())
    with col3:
        ciclo_actual = st.number_input("Año de Ciclo a Evaluar", min_value=2000, max_value=2050, value=2026)
    
    submitted = st.form_submit_button("Generar Informe Arquetípico y Proyección Operativa")

if submitted:
    if not nombre_completo:
        st.warning("Por favor, ingresa el nombre completo para calcular las frecuencias arquetípicas.")
    else:
        st.success("¡Análisis profundo y proyección operativa procesados con éxito!")
        
        fecha_str = fecha_nacimiento.strftime("%d%m%Y")
        suma_digitos = sum(int(char) for char in fecha_str)
        
        arcano_base = suma_digitos
        while arcano_base > 22 and arcano_base not in [33, 44]:
            arcano_base = sum(int(char) for char in str(arcano_base))
            
        gematria_nombre = sum(ord(c.upper()) - 64 for c in nombre_completo if c.isalpha())
        sendero_nombre = (gematria_nombre % 22) + 1
        
        ciclo_str = str(ciclo_actual)
        energia_ciclo = sum(int(c) for c in ciclo_str)
        while energia_ciclo > 9:
            energia_ciclo = sum(int(c) for c in str(energia_ciclo))

        st.markdown("---")
        st.header(f"Reporte Integral Extendido para: {nombre_completo}")
        
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric(label="Arcano Raíz / Base", value=str(arcano_base), delta="Matriz Vital")
        with m2:
            st.metric(label="Sendero Gematrico", value=str(sendero_nombre), delta="Alfabeto Hebreo")
        with m3:
            st.metric(label="Año de Sintonía", value=str(ciclo_actual), delta=f"Vibración {energia_ciclo}")
        with m4:
            st.metric(label="Hora Operativa", value=str(hora_nacimiento.strftime("%H:%M")), delta="Sello Temporal")
            
        st.markdown("---")
        st.subheader("📚 Síntesis Detallada de Cábala, Gematría y Arquetipos")
        
        st.write(f"""
        A partir de la fecha natal registrada (**{fecha_nacimiento.strftime('%d/%m/%Y')}** a las **{hora_nacimiento.strftime('%H:%M')}**), los patrones fonéticos del nombre (**{nombre_completo}**) y el vector temporal del año **{ciclo_actual}**, el sistema computa los flujos de energía sutil, los arquetipos raíz de los 22 Senderos del Árbol de la Vida y las frecuencias del alfabeto hebreo.
        """)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧬 Matriz Arquetípica", "⚡ Dinámica de Senderos", "🌀 Claves de Gematría", "📈 Proyección Anual", "🎯 Consejo Operativo (Mes/Semana/Día)"])
        
        with tab1:
            st.markdown("### Análisis de la Matriz Natal")
            st.info(f"El Arcano Base **{arcano_base}** denota la estructura psicológica profunda, reflejando el propósito de integración entre la voluntad consciente y el orden operativo del entorno.")
            st.write("- **Eje de Manifestación:** Alta capacidad de estructuración lógica y visión directiva.")
            st.write("- **Desafío Evolutivo:** Trascender los condicionamientos operativos hacia la autonomía directiva total.")
            
        with tab2:
            st.markdown(f"### Correspondencias con el Sendero {sendero_nombre}")
            st.success(f"Vinculación directa con las fuerzas ocultas del alfabeto hebreo y los canales de la consciencia superior.")
            st.write("- **Frecuencia Fonética:** Los valores numéricos del nombre operan como un campo de resonancia directiva.")
            st.write("- **Directriz Estratégica:** Alineación entre el diseño técnico y la ejecución comercial sin fricciones.")

        with tab3:
            st.markdown("### Gematría y Cómputo Fonético")
            st.write(f"Suma acumulada de coeficientes literales procesada: **{gematria_nombre}** unidades vibracionales.")
            st.write("- **Equilibrio Activo:** Sintonía entre la estructura analítica y la toma de decisiones basada en resultados tangibles.")
            
        with tab4:
            st.markdown(f"### Proyección para el Ciclo {ciclo_actual}")
            st.warning(f"Año regido por la vibración teosófica **{energia_ciclo}**: Periodo de máxima consolidación de proyectos independientes, reestructuración operativa y optimización de recursos.")

        with tab5:
            st.markdown("### 🎯 Consejo de Manejo y Proyección Táctica (Hasta Fin de Año)")
            st.write("Estrategia integral orientada a la eficiencia directiva, el control de variables operativas y la rentabilidad comercial sostenida:")
            
            st.markdown("#### 📅 Proyección Mes a Mes (Ciclo Activo)")
            st.markdown("- **Meses de Consolidación (Agosto - Septiembre):** Enfoque absoluto en la puesta en marcha de sistemas autónomos. Cero margen para desvíos operativos; optimización de recursos y blindaje de procesos técnicos.")
            st.markdown("- **Meses de Expansión (Octubre - Noviembre):** Apertura comercial agresiva, monetización de estructuras desarrolladas y escalabilidad de proyectos independientes.")
            st.markdown("- **Mes de Cierre y Cómputo (Diciembre):** Evaluación de rendimiento, balance de capitales y planificación estructural para el próximo periodo.")
            
            st.markdown("#### 📆 Guía Semanal Estándar")
            st.markdown("- **Semana 1 (Planificación y Arquitectura):** Diseño, revisión de código y estructuración de bases operativas sin intervención redundante.")
            st.markdown("- **Semana 2 (Ejecución y Despliegue):** Puesta en producción de módulos cerrados, pruebas en entornos reales y validación de flujos.")
            st.markdown("- **Semana 3 (Monetización y Comercialización):** Activación de canales de venta, optimización de ofertas y tracción de mercado.")
            st.markdown("- **Semana 4 (Auditoría y Cierre):** Revisión de métricas, corrección de fricciones y consolidación de resultados.")

            st.markdown("#### ☀️ Manejo del Día a Día (Directiva Diaria)")
            st.markdown("- **Franja Matutina (Claridad y Estrategia):** Dedicada a la toma de decisiones críticas, resolución técnica de alta complejidad y liderazgo de proyectos.")
            st.markdown("- **Franja Vespertina (Ejecución y Control):** Orientada al seguimiento operativo, control de avances y optimización de tiempos con autonomía total.")

        st.markdown("---")
        st.subheader("📋 Tabla Consolidada de Variables del Perfil")
        
        perfil_data = {
            "Variable Evaluada": ["Matriz Base (Arcano)", "Sendero Gematrico", "Frecuencia Fonética del Nombre", "Sintonía del Ciclo Actual", "Hora de Activación Natal", "Llave Operativa del Sistema"],
            "Resultado Computado": [f"Sendero {arcano_base}", f"Canal {sendero_nombre}", f"Valor {gematria_nombre}", f"Vibración {energia_ciclo} ({ciclo_actual})", str(hora_nacimiento.strftime("%H:%M")), "Ingeniería Cognitiva y Autónoma 360"]
        }
        st.table(pd.DataFrame(perfil_data))
