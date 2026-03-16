"""
Agentes del Sistema Multiagente ISO 27001
para Gestión del Sistema de Gestión de Seguridad de la Información (SGSI)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum
import json


class TipoAgente(Enum):
    AUDITOR = "auditor"
    RIESGO = "riesgo"
    CUMPLIMIENTO = "cumplimiento"
    INCIDENTES = "incidentes"
    MEJORA = "mejora"
    CAPACITACION = "capacitacion"
    PROVEEDORES = "proveedores"
    POLITICAS = "politicas"


class EstadoTarea(Enum):
    PENDIENTE = "pendiente"
    EN_PROCESO = "en_proceso"
    COMPLETADA = "completada"
    BLOQUEADA = "bloqueada"
    CANCELADA = "cancelada"


class Prioridad(Enum):
    CRITICA = "critica"
    ALTA = "alta"
    MEDIA = "media"
    BAJA = "baja"


@dataclass
class Tarea:
    id: str
    titulo: str
    descripcion: str
    agente_responsable: TipoAgente
    estado: EstadoTarea = EstadoTarea.PENDIENTE
    prioridad: Prioridad = Prioridad.MEDIA
    fecha_creacion: datetime = field(default_factory=datetime.now)
    fecha_limite: Optional[datetime] = None
    dependencias: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    datos: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "agente_responsable": self.agente_responsable.value,
            "estado": self.estado.value,
            "prioridad": self.prioridad.value,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "fecha_limite": self.fecha_limite.isoformat()
            if self.fecha_limite
            else None,
            "dependencias": self.dependencias,
            "tags": self.tags,
            "datos": self.datos,
        }


class AgenteBase(ABC):
    def __init__(self, tipo: TipoAgente, nombre: str, descripcion: str):
        self.tipo = tipo
        self.nombre = nombre
        self.descripcion = descripcion
        self.tareas: List[Tarea] = []
        self.historial: List[Dict] = []

    @abstractmethod
    def ejecutar(self, contexto: Dict) -> Dict:
        pass

    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)
        self.registrar_accion(f"Tarea creada: {tarea.id}")

    def registrar_accion(self, accion: str, datos: Dict = None):
        self.historial.append(
            {
                "timestamp": datetime.now().isoformat(),
                "accion": accion,
                "datos": datos or {},
            }
        )

    def get_estado(self) -> Dict:
        return {
            "tipo": self.tipo.value,
            "nombre": self.nombre,
            "tareas_pendientes": len(
                [t for t in self.tareas if t.estado == EstadoTarea.PENDIENTE]
            ),
            "tareas_en_proceso": len(
                [t for t in self.tareas if t.estado == EstadoTarea.EN_PROCESO]
            ),
            "tareas_completadas": len(
                [t for t in self.tareas if t.estado == EstadoTarea.COMPLETADA]
            ),
            "ultima_accion": self.historial[-1] if self.historial else None,
        }


class AgenteAuditor(AgenteBase):
    def __init__(self):
        super().__init__(
            tipo=TipoAgente.AUDITOR,
            nombre="Agente Auditor ISO 27001",
            descripcion="Planifica y ejecuta auditorías internas de cumplimiento ISO 27001",
        )

    def ejecutar(self, contexto: Dict) -> Dict:
        accion = contexto.get("accion", "planificar")

        if accion == "planificar":
            return self.planificar_auditoria(contexto)
        elif accion == "ejecutar":
            return self.ejecutar_auditoria(contexto)
        elif accion == "reportar":
            return self.generar_informe(contexto)
        else:
            return {"error": "Acción no reconocida"}

    def planificar_auditoria(self, contexto: Dict) -> Dict:
        alcance = contexto.get("alcance", "general")
        fecha = contexto.get("fecha", datetime.now().isoformat())

        tarea = Tarea(
            id=f"AUD-{len(self.tareas) + 1:03d}",
            titulo=f"Auditoría ISO 27001 - {alcance}",
            descripcion=f"Planificar auditoría interna con alcance: {alcance}",
            agente_responsable=self.tipo,
            prioridad=Prioridad.ALTA,
            tags=["auditoria", "iso27001", alcance],
        )

        self.agregar_tarea(tarea)

        return {
            "tarea_id": tarea.id,
            "mensaje": f"Auditoría planificada para {fecha}",
            "actividades": [
                "Definir alcance y objetivos",
                "Identificar controles a auditar",
                "Preparar checklist de auditoría",
                "Coordinar con equipos",
                "Programar entrevistas",
            ],
        }

    def ejecutar_auditoria(self, contexto: Dict) -> Dict:
        tarea_id = contexto.get("tarea_id")

        tarea = next((t for t in self.tareas if t.id == tarea_id), None)
        if tarea:
            tarea.estado = EstadoTarea.EN_PROCESO

        return {
            "tarea_id": tarea_id,
            "resultado": "Auditoría en ejecución",
            "progreso": 0,
            "proximos_pasos": [
                "Revisión de documentación",
                "Entrevistas con personal",
                "Evaluación de controles",
                "Recolección de evidencia",
            ],
        }

    def generar_informe(self, contexto: Dict) -> Dict:
        tarea_id = contexto.get("tarea_id")

        return {
            "tarea_id": tarea_id,
            "informe": {
                "hallazgos": [],
                "no_conformidades": [],
                "oportunidades_mejora": [],
                "recomendaciones": [],
                "conclusion": "Auditoría completada",
            },
        }


class AgenteRiesgo(AgenteBase):
    def __init__(self):
        super().__init__(
            tipo=TipoAgente.RIESGO,
            nombre="Agente de Gestión de Riesgos",
            descripcion="Identifica, evalúa y gestiona riesgos de seguridad de la información",
        )
        self.matriz_riesgos = []

    def ejecutar(self, contexto: Dict) -> Dict:
        accion = contexto.get("accion", "identificar")

        if accion == "identificar":
            return self.identificar_riesgos(contexto)
        elif accion == "evaluar":
            return self.evaluar_riesgo(contexto)
        elif accion == "tratar":
            return self.tratar_riesgo(contexto)
        else:
            return {"error": "Acción no reconocida"}

    def identificar_riesgos(self, contexto: Dict) -> Dict:
        categoria = contexto.get("categoria", "general")
        actividad = contexto.get("actividad", "")

        riesgos = []

        if actividad == "factoring":
            riesgos = [
                {
                    "id": "R01",
                    "nombre": "Acceso no autorizado a datos de cartera",
                    "categoria": "confidencialidad",
                },
                {
                    "id": "R02",
                    "nombre": "Manipulación de facturas cedidas",
                    "categoria": "integridad",
                },
                {
                    "id": "R03",
                    "nombre": "Intercepción de datos financieros",
                    "categoria": "confidencialidad",
                },
            ]
        elif actividad == "confirming":
            riesgos = [
                {
                    "id": "C01",
                    "nombre": "Pago a cuenta incorrecta",
                    "categoria": "disponibilidad",
                },
                {
                    "id": "C02",
                    "nombre": "Manipulación de órdenes de pago",
                    "categoria": "integridad",
                },
                {
                    "id": "C03",
                    "nombre": "Compromiso de credenciales bancarias",
                    "categoria": "autenticidad",
                },
            ]
        elif actividad == "pagos_linea":
            riesgos = [
                {
                    "id": "P01",
                    "nombre": "Robo de datos de tarjetas",
                    "categoria": "confidencialidad",
                },
                {
                    "id": "P02",
                    "nombre": "Fraude en transacciones",
                    "categoria": "integridad",
                },
                {
                    "id": "P03",
                    "nombre": "Interrupción de servicio de pagos",
                    "categoria": "disponibilidad",
                },
                {"id": "P04", "nombre": "Ataque MITM", "categoria": "confidencialidad"},
            ]

        self.registrar_accion(
            f"Riesgos identificados para {actividad}", {"count": len(riesgos)}
        )

        return {
            "actividad": actividad,
            "riesgos_identificados": riesgos,
            "total": len(riesgos),
        }

    def evaluar_riesgo(self, contexto: Dict) -> Dict:
        riesgo_id = contexto.get("riesgo_id")
        probabilidad = contexto.get("probabilidad", 3)
        impacto = contexto.get("impacto", 3)

        nivel_riesgo = probabilidad * impacto

        clasificacion = "Bajo"
        if nivel_riesgo >= 16:
            clasificacion = "Crítico"
        elif nivel_riesgo >= 9:
            clasificacion = "Alto"
        elif nivel_riesgo >= 4:
            clasificacion = "Medio"

        return {
            "riesgo_id": riesgo_id,
            "probabilidad": probabilidad,
            "impacto": impacto,
            "nivel_riesgo": nivel_riesgo,
            "clasificacion": clasificacion,
            "tratamiento_recomendado": self._recomendar_tratamiento(clasificacion),
        }

    def _recomendar_tratamiento(self, clasificacion: str) -> str:
        recomendaciones = {
            "Crítico": "Mitigar inmediatamente - Plan de acción en 24 horas",
            "Alto": "Mitigar en corto plazo - Plan de acción en 1 semana",
            "Medio": "Aceptar con controles - Revisión trimestral",
            "Bajo": "Aceptar - Monitoreo periódico",
        }
        return recomendaciones.get(clasificacion, "")

    def tratar_riesgo(self, contexto: Dict) -> Dict:
        riesgo_id = contexto.get("riesgo_id")
        tratamiento = contexto.get("tratamiento", "mitigar")

        tarea = Tarea(
            id=f"RSG-{len(self.tareas) + 1:03d}",
            titulo=f"Tratar riesgo {riesgo_id}",
            descripcion=f"Aplicar tratamiento: {tratamiento}",
            agente_responsable=self.tipo,
            prioridad=Prioridad.ALTA,
            tags=["riesgo", riesgo_id, str(tratamiento)],
        )

        self.agregar_tarea(tarea)

        return {
            "riesgo_id": riesgo_id,
            "tratamiento": tratamiento,
            "tarea_id": tarea.id,
            "proximo_paso": "Ejecutar plan de tratamiento",
        }


class AgenteCumplimiento(AgenteBase):
    def __init__(self):
        super().__init__(
            tipo=TipoAgente.CUMPLIMIENTO,
            nombre="Agente de Cumplimiento Normativo",
            descripcion="Verifica cumplimiento de ISO 27001, PCI-DSS y otras normativas",
        )

    def ejecutar(self, contexto: Dict) -> Dict:
        accion = contexto.get("accion", "verificar")

        if accion == "verificar":
            return self.verificar_cumplimiento(contexto)
        elif accion == "gap":
            return self.analisis_gap(contexto)
        elif accion == "evidencia":
            return self.gestionar_evidencia(contexto)
        else:
            return {"error": "Acción no reconocida"}

    def verificar_cumplimiento(self, contexto: Dict) -> Dict:
        norma = contexto.get("norma", "ISO27001")
        alcance = contexto.get("alcance", "general")

        controles = {
            "A.5.1": {"estado": "implementado", "evidencia": "Completa"},
            "A.5.2": {"estado": "implementado", "evidencia": "Completa"},
            "A.9.1": {"estado": "implementado", "evidencia": "Parcial"},
            "A.9.2": {"estado": "en_proceso", "evidencia": "Pendiente"},
            "A.10.1": {"estado": "implementado", "evidencia": "Completa"},
            "A.12.1": {"estado": "implementado", "evidencia": "Completa"},
            "A.16.1": {"estado": "implementado", "evidencia": "Completa"},
            "A.17.1": {"estado": "en_proceso", "evidencia": "Parcial"},
        }

        total = len(controles)
        implementados = len(
            [c for c in controles.values() if c["estado"] == "implementado"]
        )
        en_proceso = len([c for c in controles.values() if c["estado"] == "en_proceso"])

        return {
            "norma": norma,
            "alcance": alcance,
            "controles": controles,
            "resumen": {
                "total": total,
                "implementados": implementados,
                "en_proceso": en_proceso,
                "porcentaje_cumplimiento": round((implementados / total) * 100, 2),
            },
        }

    def analisis_gap(self, contexto: Dict) -> Dict:
        norma = contexto.get("norma", "ISO27001")

        gaps = [
            {
                "control": "A.9.3",
                "nombre": "Gestión de derechos de acceso",
                "estado_actual": "Parcial",
                "estado_deseado": "Completo",
                "esfuerzo": "Medio",
                "prioridad": "Alta",
            },
            {
                "control": "A.12.5",
                "nombre": "Control de malware",
                "estado_actual": "Completo",
                "estado_deseado": "Completo",
                "esfuerzo": "N/A",
                "prioridad": "N/A",
            },
        ]

        return {
            "norma": norma,
            "gaps_encontrados": len(gaps),
            "gaps": gaps,
            "roadmap": "Plan de remediación requerido",
        }

    def gestionar_evidencia(self, contexto: Dict) -> Dict:
        control = contexto.get("control", "")
        accion = contexto.get("accion", "listar")

        evidencias = {
            "A.5.1": ["Politica_SGSI_v2.pdf", "Acta_Direccion_2024.pdf"],
            "A.9.1": ["Matriz_Controles_Acceso.xlsx", "Revision_Accesos_Q4.pdf"],
            "A.10.1": ["Politica_Cifrado.pdf", "Certificados_TLS.pdf"],
        }

        return {
            "control": control,
            "evidencias": evidencias.get(control, []),
            "total": len(evidencias.get(control, [])),
        }


class AgenteIncidentes(AgenteBase):
    def __init__(self):
        super().__init__(
            tipo=TipoAgente.INCIDENTES,
            nombre="Agente de Gestión de Incidentes",
            descripcion="Detecta, clasifica y coordina respuesta a incidentes de seguridad",
        )
        self.incidentes = []

    def ejecutar(self, contexto: Dict) -> Dict:
        accion = contexto.get("accion", "detectar")

        if accion == "detectar":
            return self.detectar_incidente(contexto)
        elif accion == "clasificar":
            return self.clasificar_incidente(contexto)
        elif accion == "responder":
            return self.responder_incidente(contexto)
        else:
            return {"error": "Acción no reconocida"}

    def detectar_incidente(self, contexto: Dict) -> Dict:
        fuente = contexto.get("fuente", "SIEM")
        descripcion = contexto.get("descripcion", "")

        incidente_id = f"INC-{len(self.incidentes) + 1:05d}"

        incidente = {
            "id": incidente_id,
            "descripcion": descripcion,
            "fuente": fuente,
            "fecha_deteccion": datetime.now().isoformat(),
            "estado": "abierto",
            "severidad": "por-determinar",
        }

        self.incidentes.append(incidente)

        return {
            "incidente_id": incidente_id,
            "mensaje": "Incidente registrado y en análisis",
            "proximo_paso": "Clasificar incidente",
        }

    def clasificar_incidente(self, contexto: Dict) -> Dict:
        incidente_id = contexto.get("incidente_id")
        severidad = contexto.get("severidad", "media")

        clasificacion = {
            "critica": {
                "tiempo_respuesta": "15 min",
                "escalamiento": "CISO + CEO",
                "equipo": "CSIRT Completo",
            },
            "alta": {
                "tiempo_respuesta": "1 hora",
                "escalamiento": "CISO",
                "equipo": "SOC + Línea de negocio",
            },
            "media": {
                "tiempo_respuesta": "4 horas",
                "escalamiento": "Team Leader",
                "equipo": "Seguridad IT",
            },
            "baja": {
                "tiempo_respuesta": "24 horas",
                "escalamiento": "Analista",
                "equipo": "Soporte",
            },
        }

        return {
            "incidente_id": incidente_id,
            "severidad": severidad,
            "clasificacion": clasificacion.get(severidad, clasificacion["baja"]),
            "slack": f"https://empresa.slack.com/incidentes/{incidente_id}",
        }

    def responder_incidente(self, contexto: Dict) -> Dict:
        incidente_id = contexto.get("incidente_id")
        accion = contexto.get("accion", "contener")

        acciones = {
            "contener": [
                "Aislar sistema afectado",
                "Bloquear acceso comprometido",
                "Preservar evidencia",
            ],
            "erradicar": [
                "Eliminar malware",
                "Cerrar vulnerabilidades",
                "Resetear credenciales",
            ],
            "recuperar": [
                "Restaurar servicios",
                "Verificar integridad",
                "Monitoreo intensificado",
            ],
            "lecciones": [
                "Documentar incidente",
                "Identificar mejoras",
                "Actualizar procedimientos",
            ],
        }

        return {
            "incidente_id": incidente_id,
            "fase": accion,
            "acciones_recomendadas": acciones.get(accion, []),
            "checklist": acciones.get(accion, []),
        }


class AgenteMejora(AgenteBase):
    def __init__(self):
        super().__init__(
            tipo=TipoAgente.MEJORA,
            nombre="Agente de Mejora Continua",
            descripcion="Identifica oportunidades de mejora en el SGSI",
        )

    def ejecutar(self, contexto: Dict) -> Dict:
        accion = contexto.get("accion", "analizar")

        if accion == "analizar":
            return self.analizar_mejoras(contexto)
        elif accion == "proponer":
            return self.proponer_mejora(contexto)
        elif accion == "implementar":
            return self.planificar_implementacion(contexto)
        else:
            return {"error": "Acción no reconocida"}

    def analizar_mejoras(self, contexto: Dict) -> Dict:
        metricas = contexto.get("metricas", {})

        mejoras = []

        for metrica_id, valor in metricas.items():
            if valor < 80:
                mejoras.append(
                    {
                        "metrica": metrica_id,
                        "valor_actual": valor,
                        "valor_objetivo": 95,
                        "prioridad": "Alta",
                        "categoria": "Eficiencia",
                    }
                )

        return {
            "mejoras_identificadas": len(mejoras),
            "mejoras": mejoras,
            "roadmap": "Generar plan de acción",
        }

    def proponer_mejora(self, contexto: Dict) -> Dict:
        area = contexto.get("area", "")
        descripcion = contexto.get("descripcion", "")

        tarea = Tarea(
            id="MJR-{len(self.tareas)+1:03d}",
            titulo=f"Mejora: {area}",
            descripcion=descripcion,
            agente_responsable=self.tipo,
            prioridad=Prioridad.MEDIA,
            tags=["mejora", area],
        )

        self.agregar_tarea(tarea)

        return {
            "tarea_id": tarea.id,
            "mejora_propuesta": {
                "area": area,
                "descripcion": descripcion,
                "beneficios_esperados": "Mejora en cumplimiento y eficiencia",
                "recursos_necesarios": "Por determinar",
            },
        }

    def planificar_implementacion(self, contexto: Dict) -> Dict:
        mejora_id = contexto.get("mejora_id")

        fases = [
            {
                "fase": 1,
                "nombre": "Análisis",
                "duracion": "2 semanas",
                "entregable": "Informe de viabilidad",
            },
            {
                "fase": 2,
                "nombre": "Diseño",
                "duracion": "3 semanas",
                "entregable": "Especificación técnica",
            },
            {
                "fase": 3,
                "nombre": "Implementación",
                "duracion": "6 semanas",
                "entregable": "Solución desplegada",
            },
            {
                "fase": 4,
                "nombre": "Validación",
                "duracion": "2 semanas",
                "entregable": "Informe de pruebas",
            },
            {
                "fase": 5,
                "nombre": "Cierre",
                "duracion": "1 semana",
                "entregable": "Lecciones aprendidas",
            },
        ]

        return {
            "mejora_id": mejora_id,
            "fases": fases,
            "duracion_total": "14 semanas",
            "proximo_paso": "Iniciar fase 1: Análisis",
        }


class AgenteCapacitacion(AgenteBase):
    def __init__(self):
        super().__init__(
            tipo=TipoAgente.CAPACITACION,
            nombre="Agente de Capacitación en Seguridad",
            descripcion="Gestiona programas de formación en seguridad de la información",
        )

    def ejecutar(self, contexto: Dict) -> Dict:
        accion = contexto.get("accion", "evaluar")

        if accion == "evaluar":
            return self.evaluar_necesidades(contexto)
        elif accion == "planificar":
            return self.planificar_capacitacion(contexto)
        elif accion == "ejecutar":
            return self.ejecutar_capacitacion(contexto)
        else:
            return {"error": "Acción no reconocida"}

    def evaluar_necesidades(self, contexto: Dict) -> Dict:
        roles = contexto.get("roles", [])

        programas = {
            "general": ["Concienciación en seguridad", "Phishing simulation"],
            "desarrolladores": ["Secure coding", "OWASP Top 10"],
            "operaciones": ["Gestión de incidentes", "Hardening de sistemas"],
            "directivos": ["Ciberseguridad para ejecutivos", "Gestión de crisis"],
            "factoring": ["Protección de datos financieros", "Prevención de fraude"],
            "pagos": ["PCI-DSS", "Tokenización"],
        }

        return {
            "roles_evaluados": roles,
            "programas_recomendados": [programas.get(r, []) for r in roles],
            "prioridades": ["Concienciación trimestral", "Capacitación técnica anual"],
        }

    def planificar_capacitacion(self, contexto: Dict) -> Dict:
        programa = contexto.get("programa", "")
        frecuencia = contexto.get("frecuencia", "anual")

        return {
            "programa": programa,
            "frecuencia": frecuencia,
            "sesiones": [
                {"modulo": 1, "titulo": "Fundamentos", "duracion": "2 horas"},
                {"modulo": 2, "titulo": "Casos prácticos", "duracion": "2 horas"},
                {"modulo": 3, "titulo": "Evaluación", "duracion": "1 hora"},
            ],
            "participantes_estimados": "100% del personal",
        }

    def ejecutar_capacitacion(self, contexto: Dict) -> Dict:
        programa = contexto.get("programa", "")

        return {
            "programa": programa,
            "estado": "En ejecución",
            "progreso": 0,
            "proximos_pasos": [
                "Enviar invitaciones",
                "Configurar LMS",
                "Iniciar primera sesión",
            ],
        }


class AgenteProveedores(AgenteBase):
    def __init__(self):
        super().__init__(
            tipo=TipoAgente.PROVEEDORES,
            nombre="Agente de Gestión de Proveedores",
            descripcion="Evalúa y gestiona riesgos de seguridad de terceros",
        )

    def ejecutar(self, contexto: Dict) -> Dict:
        accion = contexto.get("accion", "evaluar")

        if accion == "evaluar":
            return self.evaluar_proveedor(contexto)
        elif accion == "contratar":
            return self.proceso_contratacion(contexto)
        elif accion == "monitorear":
            return self.monitorear_proveedor(contexto)
        else:
            return {"error": "Acción no reconocida"}

    def evaluar_proveedor(self, contexto: Dict) -> Dict:
        proveedor = contexto.get("proveedor", "")
        criticidad = contexto.get("criticidad", "media")

        criterios = [
            {"criterio": "Seguridad de datos", "peso": 0.3, "puntuacion": 85},
            {"criterio": "Certificaciones", "peso": 0.25, "puntuacion": 90},
            {"criterio": "Incidentes previos", "peso": 0.2, "puntuacion": 80},
            {"criterio": "Capacidad de respuesta", "peso": 0.15, "puntuacion": 75},
            {"criterio": "Presencia local", "peso": 0.1, "puntuacion": 70},
        ]

        puntuacion_total = sum(c["peso"] * c["puntuacion"] for c in criterios)

        return {
            "proveedor": proveedor,
            "criticidad": criticidad,
            "puntuacion_total": round(puntuacion_total, 2),
            "clasificacion": "Aprobado" if puntuacion_total >= 70 else "Rechazado",
            "criterios": criterios,
            "acciones": ["Renovar evaluación en 12 meses"]
            if puntuacion_total >= 70
            else ["Revisar contrato", "Establecer plan de remediación"],
        }

    def proceso_contratacion(self, contexto: Dict) -> Dict:
        proveedor = contexto.get("proveedor", "")

        return {
            "proveedor": proveedor,
            "fase": "Evaluación inicial completada",
            "pasos": [
                {
                    "paso": 1,
                    "nombre": "Solicitud de información",
                    "estado": "completado",
                },
                {
                    "paso": 2,
                    "nombre": "Evaluación de seguridad",
                    "estado": "completado",
                },
                {"paso": 3, "nombre": "Revisión contractual", "estado": "en_proceso"},
                {"paso": 4, "nombre": "Aprobación", "estado": "pendiente"},
            ],
        }

    def monitorear_proveedor(self, contexto: Dict) -> Dict:
        proveedor = contexto.get("proveedor", "")

        return {
            "proveedor": proveedor,
            "monitoreo": {
                "incidentes": 0,
                "auditorias": 1,
                "evaluaciones": "al_dia",
                "proximas_acciones": ["Revisión trimestral programada"],
            },
        }


class AgentePoliticas(AgenteBase):
    def __init__(self):
        super().__init__(
            tipo=TipoAgente.POLITICAS,
            nombre="Agente de Gestión de Políticas",
            descripcion="Administra y actualiza políticas de seguridad de la información",
        )

    def ejecutar(self, contexto: Dict) -> Dict:
        accion = contexto.get("accion", "gestionar")

        if accion == "gestionar":
            return self.gestionar_politica(contexto)
        elif accion == "actualizar":
            return self.actualizar_politica(contexto)
        elif accion == "diffundir":
            return self.diffundir_politica(contexto)
        else:
            return {"error": "Acción no reconocida"}

    def gestionar_politica(self, contexto: Dict) -> Dict:
        politica = contexto.get("politica", "")

        politicas = {
            "sgsi": {
                "version": "3.0",
                "fecha": "2024-01-15",
                "proximarevision": "2025-01-15",
                "estado": "activa",
            },
            "contrasenas": {
                "version": "2.1",
                "fecha": "2024-03-01",
                "proximarevision": "2025-03-01",
                "estado": "activa",
            },
            "uso_acceptable": {
                "version": "1.5",
                "fecha": "2024-02-20",
                "proximarevision": "2025-02-20",
                "estado": "activa",
            },
            "datos_personales": {
                "version": "2.0",
                "fecha": "2024-06-01",
                "proximarevision": "2025-06-01",
                "estado": "activa",
            },
            "pagos": {
                "version": "1.0",
                "fecha": "2024-08-15",
                "proximarevision": "2025-08-15",
                "estado": "activa",
            },
        }

        return {"politica": politica, "detalles": politicas.get(politica, {})}

    def actualizar_politica(self, contexto: Dict) -> Dict:
        politica = contexto.get("politica", "")
        motivo = contexto.get("motivo", "")

        tarea = Tarea(
            id=f"POL-{len(self.tareas) + 1:03d}",
            titulo=f"Actualizar política: {politica}",
            descripcion=f"Motivo: {motivo}",
            agente_responsable=self.tipo,
            prioridad=Prioridad.MEDIA,
            tags=["politica", politica],
        )

        self.agregar_tarea(tarea)

        return {
            "politica": politica,
            "tarea_id": tarea.id,
            "proceso": [
                "Revisar versión actual",
                "Incorporar cambios requeridos",
                "Revisión legal",
                "Aprobación de dirección",
                "Publicación y comunicación",
            ],
        }

    def difundir_politica(self, contexto: Dict) -> Dict:
        politica = contexto.get("politica", "")
        audiencia = contexto.get("audiencia", "general")

        return {
            "politica": politica,
            "audiencia": audiencia,
            "canales": ["Intranet", "Email", "Capacitación"],
            "confirmacion_requerida": True,
            "plazo": "30 días",
        }


class CoordinatorAgent:
    def __init__(self):
        self.agentes = {
            TipoAgente.AUDITOR: AgenteAuditor(),
            TipoAgente.RIESGO: AgenteRiesgo(),
            TipoAgente.CUMPLIMIENTO: AgenteCumplimiento(),
            TipoAgente.INCIDENTES: AgenteIncidentes(),
            TipoAgente.MEJORA: AgenteMejora(),
            TipoAgente.CAPACITACION: AgenteCapacitacion(),
            TipoAgente.PROVEEDORES: AgenteProveedores(),
            TipoAgente.POLITICAS: AgentePoliticas(),
        }

    def obtener_agente(self, tipo: TipoAgente) -> Optional[AgenteBase]:
        return self.agentes.get(tipo)

    def ejecutar_agente(self, tipo_agente: TipoAgente, contexto: Dict) -> Dict:
        agente = self.obtener_agente(tipo_agente)
        if agente:
            return agente.ejecutar(contexto)
        return {"error": "Agente no encontrado"}

    def get_estado_sistema(self) -> Dict:
        return {
            "agentes": {
                tipo.value: agente.get_estado() for tipo, agente in self.agentes.items()
            },
            "total_agentes": len(self.agentes),
            "total_tareas": sum(len(a.tareas) for a in self.agentes.values()),
        }

    def get_dashboard(self) -> Dict:
        return {
            "estado_sistema": self.get_estado_sistema(),
            "metricas_clave": {
                "cumplimiento_general": 85,
                "riesgos_criticos": 2,
                "incidentes_abiertos": 3,
                "mejoras_en_curso": 5,
                "auditorias_pendientes": 1,
            },
        }
