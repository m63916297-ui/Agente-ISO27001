"""
Sistema Multiagente ISO 27001 - Frontend Streamlit
==================================================
Interfaz web para la gestión de certificación ISO 27001
"""

import streamlit as st
import pandas as pd
import json
from datetime import datetime

from metricas import GestorMetricas, TemplatesMetricas, TipoMetrica, CategoriaControl
from criterios import GestorCriterios, TipoOperacion
from agentes import CoordinatorAgent, TipoAgente
from rules import (
    REGLAS_SISTEMA,
    REGLAS_OPERATIVAS,
    obtener_reglas_por_categoria,
    obtener_reglas_por_actividad,
)
from skills import SkillsAgentes, get_skills_agente
from mejora_procesos import MotorMejoraSGSI, TipoProceso, EstadoProceso


st.set_page_config(
    page_title="ISO 27001 - Sistema Multiagente",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)


CSS = """
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stApp {
        background-color: #ffffff;
    }
    .titulo-principal {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e3a5f;
        text-align: center;
        padding: 20px;
        border-bottom: 3px solid #1e3a5f;
    }
    .subtitulo {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c5282;
        padding: 10px 0;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #3182ce;
    }
    .card-success {
        border-left: 4px solid #38a169;
    }
    .card-warning {
        border-left: 4px solid #dd6b20;
    }
    .card-danger {
        border-left: 4px solid #e53e3e;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 20px;
        color: white;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
    }
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .agent-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        border-radius: 10px;
        padding: 15px;
        color: white;
        margin: 5px 0;
    }
    .rule-item {
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        background-color: #edf2f7;
    }
    .skill-badge {
        display: inline-block;
        background-color: #4299e1;
        color: white;
        padding: 3px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 2px;
    }
    div.stButton > button {
        background-color: #3182ce;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    div.stButton > button:hover {
        background-color: #2c5282;
    }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


gestor_metricas = GestorMetricas()
gestor_criterios = GestorCriterios()
coordinador = CoordinatorAgent()
motor_mejora = MotorMejoraSGSI()


def sidebar_menu():
    with st.sidebar:
        st.title("🔒 ISO 27001")
        st.caption("Sistema Multiagente para Certificación")

        menu = st.radio(
            "Navegación",
            [
                "🏠 Inicio",
                "📊 Dashboard",
                "📏 Métricas",
                "📋 Criterios",
                "🤖 Agentes",
                "📜 Rules",
                "💡 Skills",
                "🔄 Mejora Procesos",
                "📚 Certificación",
            ],
        )

        st.markdown("---")
        st.caption("Versión 1.0.0")
        st.caption("2026")

    return menu


def inicio():
    st.markdown(
        '<p class="titulo-principal">Sistema Multiagente ISO 27001</p>',
        unsafe_allow_html=True,
    )

    st.markdown("""
    ## 🏢 Empresa de Factoring, Confirming y Pagos en Línea
    
    Este sistema proporciona asistencia integral para la obtención y mantenimiento 
    de la certificación **ISO 27001:2022** en empresas de servicios financieros.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="metric-card">
            <div class="metric-value">8</div>
            <div class="metric-label">Agentes Activos</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <div class="metric-value">30</div>
            <div class="metric-label">Reglas Definidas</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <div class="metric-value">93</div>
            <div class="metric-label">Controles ISO 27001</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("### 🚀 Características del Sistema")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Módulos Principales:**
        - 📊 Métricas de cumplimiento
        - 📋 Criterios específicos por actividad
        - 🤖 Agentes especializados
        - 📜 Reglas de seguridad
        - 💡 Skills y competencias
        """)

    with col2:
        st.markdown("""
        **Actividades Soportadas:**
        - 💰 Factoring
        - 🏦 Confirming  
        - 💳 Pagos en Línea
        """)

    st.markdown("### 📋 Normativas Adicionales Soportadas")

    normativas = {
        "ISO 27001:2022": "Sistema de Gestión de Seguridad de la Información",
        "PCI-DSS 4.0": "Seguridad de datos de tarjetas de pago",
        "PSD2": "Servicios de pago en la UE",
        "GDPR/LGPD": "Protección de datos personales",
        "SOX": "Controles financieros",
        "Basilea III": "Gestión de riesgos bancarios",
    }

    for norma, desc in normativas.items():
        st.markdown(f"- **{norma}**: {desc}")


def dashboard():
    st.title("📊 Dashboard de Cumplimiento ISO 27001")

    dashboard_data = coordinador.get_dashboard()

    st.markdown("### Indicadores Clave")

    col1, col2, col3, col4 = st.columns(4)

    metricas_clave = dashboard_data.get("metricas_clave", {})

    with col1:
        st.metric(
            "Cumplimiento General",
            f"{metricas_clave.get('cumplimiento_general', 0)}%",
            delta="+5%",
        )
    with col2:
        st.metric(
            "Riesgos Críticos",
            metricas_clave.get("riesgos_criticos", 0),
            delta="-2",
            delta_color="inverse",
        )
    with col3:
        st.metric(
            "Incidentes Abiertos",
            metricas_clave.get("incidentes_abiertos", 0),
            delta="-1",
            delta_color="inverse",
        )
    with col4:
        st.metric("Mejoras en Curso", metricas_clave.get("mejoras_en_curso", 0))

    st.markdown("### Estado de Agentes")

    estado_sistema = coordinador.get_estado_sistema()

    for agente_tipo, estado in estado_sistema["agentes"].items():
        with st.expander(f"🤖 {estado.get('nombre', agente_tipo)}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Tareas Pendientes:** {estado.get('tareas_pendientes', 0)}")
                st.write(f"**Tareas en Proceso:** {estado.get('tareas_en_proceso', 0)}")
            with col2:
                st.write(
                    f"**Tareas Completadas:** {estado.get('tareas_completadas', 0)}"
                )
                if estado.get("ultima_accion"):
                    st.caption(
                        f"Última acción: {estado['ultima_accion'].get('accion', 'N/A')}"
                    )

    st.markdown("### Procesos del SGSI")

    estado_sgsi = motor_mejora.get_estado_sgsi()
    procesos = estado_sgsi.get("indicadores_clave", {})

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Procesos Operacionales", procesos.get("procesos_operacionales", 0))
    with col2:
        st.metric("Mejoras en Curso", procesos.get("mejoras_en_curso", 0))
    with col3:
        st.metric(
            "Actualizaciones Pendientes", procesos.get("actualizaciones_pendientes", 0)
        )


def metricas():
    st.title("📏 Métricas ISO 27001")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Todas las Métricas", "Por Categoría", "Evaluación", "Registros"]
    )

    with tab1:
        st.markdown("### Todas las Métricas Configuradas")

        templates = gestor_metricas.templates

        for metrica in templates:
            with st.expander(f"**{metrica.id}** - {metrica.nombre}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Descripción:** {metrica.descripcion}")
                    st.write(f"**Categoría:** {metrica.categoria.value}")
                    st.write(f"**Tipo:** {metrica.tipo.value}")
                with col2:
                    st.write(
                        f"**Objetivo:** {metrica.umbral.objetivo} {metrica.umbral.unidad}"
                    )
                    st.write(
                        f"**Mínimo:** {metrica.umbral.minimo} {metrica.umbral.unidad}"
                    )
                    st.write(f"**Responsable:** {metrica.responsable}")

                if metrica.aplicabilidad:
                    st.write(f"**Aplicabilidad:** {', '.join(metrica.aplicabilidad)}")

    with tab2:
        st.markdown("### Métricas por Categoría")

        categoria_seleccionada = st.selectbox(
            "Seleccionar Categoría", [c.value for c in CategoriaControl]
        )

        metricas_categoria = [
            m
            for m in gestor_metricas.templates
            if m.categoria.value == categoria_seleccionada
        ]

        st.write(f"Se encontraron {len(metricas_categoria)} métricas en esta categoría")

        for m in metricas_categoria:
            st.markdown(
                f"""
            <div class="card">
                <strong>{m.id}</strong> - {m.nombre}<br>
                <small>Objetivo: {m.umbral.objetivo} {m.umbral.unidad}</small>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with tab3:
        st.markdown("### Evaluar Métrica")

        metrica_id = st.selectbox(
            "Seleccionar Métrica", [m.id for m in gestor_metricas.templates]
        )

        if metrica_id:
            metrica = gestor_metricas.get_metrica(metrica_id)
            if metrica:
                st.write(f"**Nombre:** {metrica.nombre}")
                st.write(f"**Fórmula:** {metrica.formula}")
                st.write(
                    f"**Umbral objetivo:** {metrica.umbral.objetivo} {metrica.umbral.unidad}"
                )

                valor = st.number_input(
                    "Ingrese valor a evaluar", min_value=0.0, step=0.1
                )

                if st.button("Evaluar"):
                    resultado = gestor_metricas.evaluar_metrica(metrica_id, valor)

                    if resultado.get("estado") == "cumplido":
                        st.success(f"✅ CUMPLIDO - {resultado['estado']}")
                    elif resultado.get("estado") == "parcial":
                        st.warning(f"⚠️ PARCIAL - {resultado['estado']}")
                    else:
                        st.error(f"❌ NO CUMPLIDO - {resultado['estado']}")

    with tab4:
        st.markdown("### Registros de Métricas")
        st.info("Esta sección muestra el historial de evaluaciones de métricas.")


def criterios():
    st.title("📋 Criterios por Actividad")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Factoring", "Confirming", "Pagos en Línea", "Resumen"]
    )

    with tab1:
        st.markdown("### Criterios para Factoring")

        criterios_factoring = gestor_criterios.get_criterios_por_tipo(
            TipoOperacion.FACTORING
        )

        for c in criterios_factoring:
            with st.expander(f"**{c.id}** - {c.nombre}"):
                st.write(f"**Descripción:** {c.descripcion}")
                st.write(f"**Categoría de Riesgo:** {c.categoria_riesgo.value}")
                st.write(f"**Peso:** {c.peso}")
                st.write(f"**Controles ISO:** {', '.join(c.controles_relacionados)}")

                st.write("**Preguntas de Evaluación:**")
                for p in c.preguntas_evaluacion:
                    st.write(f"- {p}")

                st.write("**Evidencia Requerida:**")
                for e in c.evidencia_requerida:
                    st.write(f"- {e}")

    with tab2:
        st.markdown("### Criterios para Confirming")

        criterios_confirming = gestor_criterios.get_criterios_por_tipo(
            TipoOperacion.CONFIRMING
        )

        for c in criterios_confirming:
            with st.expander(f"**{c.id}** - {c.nombre}"):
                st.write(f"**Descripción:** {c.descripcion}")
                st.write(f"**Categoría de Riesgo:** {c.categoria_riesgo.value}")
                st.write(f"**Peso:** {c.peso}")
                st.write(f"**Controles ISO:** {', '.join(c.controles_relacionados)}")

    with tab3:
        st.markdown("### Criterios para Pagos en Línea")

        criterios_pagos = gestor_criterios.get_criterios_por_tipo(
            TipoOperacion.PAGOS_LINEA
        )

        for c in criterios_pagos:
            with st.expander(f"**{c.id}** - {c.nombre}"):
                st.write(f"**Descripción:** {c.descripcion}")
                st.write(f"**Categoría de Riesgo:** {c.categoria_riesgo.value}")
                st.write(f"**Peso:** {c.peso}")
                st.write(f"**Controles ISO:** {', '.join(c.controles_relacionados)}")
                st.write(
                    f"**Requisitos Normativos:** {', '.join(c.requisitos_normativos)}"
                )

    with tab4:
        st.markdown("### Resumen de Criterios")

        resumen = gestor_criterios.get_resumen_por_tipo()

        df = pd.DataFrame(
            [
                {"Actividad": k, "Total Criterios": v["total"]}
                for k, v in resumen.items()
            ]
        )

        st.table(df)


def agentes():
    st.title("🤖 Agentes del SGSI")

    st.markdown("""
    El sistema cuenta con 8 agentes especializados que automatizan 
    diferentes aspectos del Sistema de Gestión de Seguridad de la Información.
    """)

    tab1, tab2, tab3 = st.tabs(["Lista de Agentes", "Estado", "Interacción"])

    with tab1:
        agentes_info = [
            (
                "Auditor",
                "Planifica y ejecuta auditorías internas",
                ["AUD-001", "AUD-002", "AUD-003", "AUD-004"],
            ),
            (
                "Riesgo",
                "Identifica y evalúa riesgos de seguridad",
                ["RSG-001", "RSG-002", "RSG-003", "RSG-004"],
            ),
            (
                "Cumplimiento",
                "Verifica cumplimiento normativo",
                ["CMP-001", "CMP-002", "CMP-003", "CMP-004"],
            ),
            (
                "Incidentes",
                "Gestiona respuesta a incidentes",
                ["INC-001", "INC-002", "INC-003", "INC-004"],
            ),
            (
                "Mejora",
                "Propone mejoras continuas",
                ["MJR-001", "MJR-002", "MJR-003", "MJR-004"],
            ),
            (
                "Capacitación",
                "Gestiona formación en seguridad",
                ["CAP-001", "CAP-002", "CAP-003", "CAP-004"],
            ),
            (
                "Proveedores",
                "Evalúa riesgos de terceros",
                ["PRV-001", "PRV-002", "PRV-003", "PRV-004"],
            ),
            (
                "Políticas",
                "Administra políticas de seguridad",
                ["POL-001", "POL-002", "POL-003", "POL-004"],
            ),
        ]

        for nombre, desc, skills in agentes_info:
            with st.expander(f"**{nombre}**"):
                st.write(f"**Función:** {desc}")
                st.write("**Skills:**")
                for s in skills:
                    st.markdown(
                        f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True
                    )

    with tab2:
        st.markdown("### Estado de los Agentes")

        estado = coordinador.get_estado_sistema()

        for tipo, data in estado["agentes"].items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{data.get('nombre', tipo)}**")
            with col2:
                total = (
                    data.get("tareas_pendientes", 0)
                    + data.get("tareas_en_proceso", 0)
                    + data.get("tareas_completadas", 0)
                )
                st.progress(
                    (data.get("tareas_completadas", 0) / total * 100)
                    if total > 0
                    else 0
                )

    with tab3:
        st.markdown("### Interactuar con Agentes")

        agente_seleccionado = st.selectbox(
            "Seleccionar Agente",
            [
                "Auditor",
                "Riesgo",
                "Cumplimiento",
                "Incidentes",
                "Capacitacion",
                "Proveedores",
                "Politicas",
            ],
        )

        accion = st.selectbox("Seleccionar Acción", ["Ver estado", "Ejecutar tarea"])

        if st.button("Ejecutar"):
            tipo_map = {
                "Auditor": TipoAgente.AUDITOR,
                "Riesgo": TipoAgente.RIESGO,
                "Cumplimiento": TipoAgente.CUMPLIMIENTO,
                "Incidentes": TipoAgente.INCIDENTES,
                "Capacitacion": TipoAgente.CAPACITACION,
                "Proveedores": TipoAgente.PROVEEDORES,
                "Politicas": TipoAgente.POLITICAS,
            }

            resultado = coordinador.ejecutar_agente(
                tipo_map[agente_seleccionado], {"accion": "verificar"}
            )
            st.json(resultado)


def rules():
    st.title("📜 Reglas del Sistema")

    st.markdown("""
    El sistema define 30 reglas de seguridad específicas para empresas 
    de factoring, confirming y pagos en línea.
    """)

    tab1, tab2, tab3 = st.tabs(["Todas las Reglas", "Por Categoría", "Por Actividad"])

    with tab1:
        reglas = REGLAS_SISTEMA["reglas"]

        for regla in reglas:
            with st.expander(f"**{regla['id']}** - {regla['nombre']}"):
                st.write(f"**Categoría:** {regla['categoria']}")
                st.write(f"**Descripción:** {regla['descripcion']}")
                st.write(f"**Aplicabilidad:** {regla.get('aplicabilidad', 'todas')}")

    with tab2:
        categorias = list(set(r["categoria"] for r in REGLAS_SISTEMA["reglas"]))

        categoria_seleccionada = st.selectbox("Seleccionar Categoría", categorias)

        reglas_categoria = obtener_reglas_por_categoria(categoria_seleccionada)

        for r in reglas_categoria:
            st.markdown(
                f"""
            <div class="rule-item">
                <strong>{r["id"]}</strong> - {r["nombre"]}<br>
                <small>{r["descripcion"]}</small>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with tab3:
        actividad = st.selectbox(
            "Seleccionar Actividad", ["factoring", "confirming", "pagos_linea"]
        )

        reglas_actividad = obtener_reglas_por_actividad(actividad)

        st.write(
            f"Se encontraron {len(reglas_actividad)} reglas aplicables a {actividad}"
        )

        for r in reglas_actividad:
            with st.expander(f"**{r['id']}** - {r['nombre']}"):
                st.write(r["descripcion"])
                st.write(f"**Categoría:** {r['categoria']}")


def skills_view():
    st.title("💡 Skills y Competencias")

    st.markdown("""
    Cada agente cuenta con habilidades específicas (skills) que definen 
    sus capacidades para ejecutar tareas relacionadas con ISO 27001.
    """)

    all_skills = SkillsAgentes.get_all_skills()

    tab1, tab2 = st.tabs(["Por Agente", "Resumen"])

    with tab1:
        for agente_key, agente_data in all_skills.items():
            with st.expander(f"**{agente_data['nombre_agente']}**"):
                st.write(f"**Rol:** {agente_data['rol']}")

                st.write("**Competencias Clave:**")
                for comp in agente_data["competencias_clave"]:
                    st.write(f"- {comp}")

                st.write("**Skills:**")
                for skill in agente_data["skills"]:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**{skill['nombre']}**")
                        st.caption(skill["descripcion"])
                    with col2:
                        st.write(f"Nivel: {skill['nivel']}/5")
                        if skill["certificaciones"]:
                            st.caption(f"Certs: {', '.join(skill['certificaciones'])}")

                st.write("**Limitantes:**")
                for limit in agente_data["limitantes"]:
                    st.write(f"- {limit}")

    with tab2:
        data = []
        for agente_key, agente_data in all_skills.items():
            data.append(
                {
                    "Agente": agente_data["nombre_agente"],
                    "Skills": len(agente_data["skills"]),
                    "Competencias": len(agente_data["competencias_clave"]),
                    "Limitantes": len(agente_data["limitantes"]),
                }
            )

        df = pd.DataFrame(data)
        st.table(df)


def mejora_procesos():
    st.title("🔄 Mejora de Procesos")

    tab1, tab2, tab3 = st.tabs(["Procesos", "Mejoras", "Estado SGSI"])

    with tab1:
        st.markdown("### Procesos del SGSI")

        procesos = motor_mejora.gestor_procesos.get_dashboard_procesos()

        st.write(f"**Total de Procesos:** {procesos['total_procesos']}")

        st.write("#### Por Estado")
        for estado, count in procesos["por_estado"].items():
            st.write(f"- {estado}: {count}")

        st.write("#### Por Tipo")
        for tipo, count in procesos["por_tipo"].items():
            st.write(f"- {tipo}: {count}")

    with tab2:
        st.markdown("### Gestión de Mejoras")

        col1, col2 = st.columns(2)

        with col1:
            titulo = st.text_input("Título de la Mejora")

        with col2:
            proceso = st.selectbox(
                "Proceso Origen", [p.id for p in motor_mejora.gestor_procesos.procesos]
            )

        if st.button("Identificar Mejora"):
            resultado = motor_mejora.gestor_mejoras.identificar_mejora(
                {
                    "titulo": titulo,
                    "descripcion": "Nueva mejora identificada",
                    "proceso_origen": proceso,
                    "tipo": "preventiva",
                    "impacto": "alto",
                    "urgencia": "media",
                }
            )
            st.success(f"Mejora identificada: {resultado['mejora_id']}")

        st.markdown("### Resumen de Mejoras")

        resumen = motor_mejora.gestor_mejoras.get_resumen_mejoras()

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("Total", resumen["total"])
        with col2:
            st.metric("Identificadas", resumen["por_estado"]["identificadas"])
        with col3:
            st.metric("Aprobadas", resumen["por_estado"]["aprobadas"])
        with col4:
            st.metric("En Planificación", resumen["por_estado"]["en_planificacion"])
        with col5:
            st.metric("Implementadas", resumen["por_estado"]["implementadas"])

    with tab3:
        st.markdown("### Estado General del SGSI")

        estado = motor_mejora.get_estado_sgsi()

        indicadores = estado["indicadores_clave"]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Procesos Operacionales", indicadores["procesos_operacionales"])
        with col2:
            st.metric("Mejoras en Curso", indicadores["mejoras_en_curso"])
        with col3:
            st.metric(
                "Actualizaciones Pendientes", indicadores["actualizaciones_pendientes"]
            )

        if st.button("Generar Plan Anual"):
            plan = motor_mejora.generar_plan_mejora_anual()
            st.json(plan)


def certificacion():
    st.title("📚 Guía de Certificación ISO 27001")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Fases", "Controles", "Documentación", "Normativas", "Roadmap"]
    )

    with tab1:
        st.markdown("""
        ## 📋 Fases de Implementación
        
        ### Fase 1: Inicio (Semanas 1-4)
        - Definir alcance del SGSI
        - Obtener compromiso de la dirección
        - Constituir equipo SGSI
        
        ### Fase 2: Análisis (Semanas 5-12)
        - Evaluación de riesgos
        - Análisis gap
        - Diseño de controles
        
        ### Fase 3: Implementación (Semanas 13-26)
        - Controles técnicos
        - Controles organizacionales
        - Controles de personas
        
        ### Fase 4: Operación (Semanas 27-52)
        - Gestión de incidentes
        - Mantenimiento
        - Auditorías
        """)

    with tab2:
        st.markdown("""
        ## 🔐 Controles del Anexo A (ISO 27001:2022)
        
        | Categoría | Controles |
        |-----------|-----------|
        | A.5 Organizacionales | 5 |
        | A.6 Personas | 2 |
        | A.7 Físicos | 2 |
        | A.8 Tecnológicos | 34 |
        | A.9 Acceso | 9 |
        | A.10 Criptografía | 2 |
        | A.11 Operaciones | 14 |
        | A.12 Comunicaciones | 10 |
        | A.13 Adquisición | 7 |
        | A.14 Proveedores | 5 |
        | A.15 Incidentes | 9 |
        | A.16 Continuidad | 4 |
        | A.17 Cumplimiento | 2 |
        
        **Total: 93 controles**
        """)

    with tab3:
        st.markdown("""
        ## 📄 Documentación Requerida
        
        ### Documentos Obligatorios (Cláusulas 4-10)
        1. ✅ Política de Seguridad de la Información
        2. ✅ Alcance del SGSI
        3. ✅ Evaluación de Riesgos
        4. ✅ Declaración de Aplicabilidad (SoA)
        5. ✅ Plan de Tratamiento de Riesgos
        6. ✅ Definición de Roles de Seguridad
        7. ✅ Inventario de Activos
        8. ✅ Procedimientos de Gestión de Incidentes
        9. ✅ Plan de Continuidad del Negocio
        10. ✅ Registros de Auditoría
        """)

    with tab4:
        st.markdown("""
        ## 📜 Normativas Adicionales
        
        ### Para Pagos en Línea (PCI-DSS 4.0)
        - Requisito 1: Configuración de firewall
        - Requisito 3: Proteger datos de tarjeta
        - Requisito 4: Cifrar transmisión
        - Requisito 8: Identificación única
        - Requisito 10: Rastreo de accesos
        
        ### Protección de Datos
        - GDPR/LGPD: Consentimiento, Derechos ARCO
        - Notificación de brechas: 72 horas
        
        ### Controles Financieros
        - SOX: Trazabilidad, Segregación de funciones
        - Basilea III: Gestión de riesgos operativos
        """)

    with tab5:
        st.markdown("""
        ## 🗓️ Roadmap de Implementación
        
        | Mes | Fase | Progreso |
        |-----|------|----------|
        | 1-3 | Inicio y Análisis | 30% |
        | 4-6 | Diseño y Planificación | 50% |
        | 7-12 | Implementación | 90% |
        | 13 | Auditoría y Certificación | 100% |
        
        ### Milestones Clave
        - **Mes 3**: Evaluación de riesgos completada
        - **Mes 6**: Análisis gap completado
        - **Mes 12**: Implementación de controles
        - **Mes 13**: Auditoría interna
        - **Mes 14**: Certificación
        """)


def main():
    menu = sidebar_menu()

    if menu == "🏠 Inicio":
        inicio()
    elif menu == "📊 Dashboard":
        dashboard()
    elif menu == "📏 Métricas":
        metricas()
    elif menu == "📋 Criterios":
        criterios()
    elif menu == "🤖 Agentes":
        agentes()
    elif menu == "📜 Rules":
        rules()
    elif menu == "💡 Skills":
        skills_view()
    elif menu == "🔄 Mejora Procesos":
        mejora_procesos()
    elif menu == "📚 Certificación":
        certificacion()


if __name__ == "__main__":
    main()
