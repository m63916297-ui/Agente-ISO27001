"""
Módulo de Mejora y Actualización de Procesos del SGSI
Sistema Multiagente ISO 27001
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta
from enum import Enum
import json


class TipoProceso(Enum):
    GESTION_ACCESS = "gestion_acceso"
    GESTION_INCIDENTES = "gestion_incidentes"
    GESTION_CAMBIOS = "gestion_cambios"
    GESTION_RIESGOS = "gestion_riesgos"
    GESTION_PROVEEDORES = "gestion_proveedores"
    GESTION_POLITICAS = "gestion_politicas"
    AUDITORIA = "auditoria"
    CAPACITACION = "capacitacion"
    CONTINUIDAD = "continuidad"
    CUMPLIMIENTO = "cumplimiento"


class EstadoProceso(Enum):
    DISENO = "diseno"
    IMPLEMENTACION = "implementacion"
    OPERACION = "operacion"
    MEJORA = "mejora"
    OBSOLETO = "obsoleto"


class TipoMejora(Enum):
    PREVENTIVA = "preventiva"
    CORRECTIVA = "correctiva"
    EVOLUTIVA = "evolutiva"
    REACTIVA = "reactiva"


class PrioridadMejora(Enum):
    CRITICA = 1
    ALTA = 2
    MEDIA = 3
    BAJA = 4


@dataclass
class Proceso:
    id: str
    nombre: str
    descripcion: str
    tipo: TipoProceso
    estado: EstadoProceso
    version: str = "1.0"
    fecha_creacion: datetime = field(default_factory=datetime.now)
    fecha_ultima_actualizacion: datetime = field(default_factory=datetime.now)
    responsable: str = ""
    controles_iso: List[str] = field(default_factory=list)
    kpis: List[Dict] = field(default_factory=list)
    documentacion: List[str] = field(default_factory=list)
    interdependencias: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "tipo": self.tipo.value,
            "estado": self.estado.value,
            "version": self.version,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "fecha_ultima_actualizacion": self.fecha_ultima_actualizacion.isoformat(),
            "responsable": self.responsable,
            "controles_iso": self.controles_iso,
            "kpis": self.kpis,
            "documentacion": self.documentacion,
            "interdependencias": self.interdependencias,
        }


@dataclass
class Mejora:
    id: str
    titulo: str
    descripcion: str
    tipo: TipoMejora
    prioridad: PrioridadMejora
    proceso_origen: str
    estado: str = "identificada"
    fecha_identificacion: datetime = field(default_factory=datetime.now)
    fecha_implementacion: Optional[datetime] = None
    responsable: str = ""
    recursos_necesarios: Dict = field(default_factory=dict)
    beneficios_esperados: List[str] = field(default_factory=list)
    riesgos_asociados: List[str] = field(default_factory=list)
    dependencias: List[str] = field(default_factory=list)
    historiallo: List[Dict] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "tipo": self.tipo.value,
            "prioridad": self.prioridad.name,
            "proceso_origen": self.proceso_origen,
            "estado": self.estado,
            "fecha_identificacion": self.fecha_identificacion.isoformat(),
            "fecha_implementacion": self.fecha_implementacion.isoformat()
            if self.fecha_implementacion
            else None,
            "responsable": self.responsable,
            "recursos_necesarios": self.recursos_necesarios,
            "beneficios_esperados": self.beneficios_esperados,
            "riesgos_asociados": self.riesgos_asociados,
            "dependencias": self.dependencias,
            "historial": self.historiallo,
        }


@dataclass
class Actualizacion:
    id: str
    proceso_id: str
    tipo_cambio: str
    descripcion: str
    justificacion: str
    fecha_solicitud: datetime = field(default_factory=datetime.now)
    fecha_aprobacion: Optional[datetime] = None
    solicitante: str = ""
    aprobador: str = ""
    impacto: str = ""
    estado: str = "pendiente"
    nueva_version: str = ""
    cambios: List[Dict] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "proceso_id": self.proceso_id,
            "tipo_cambio": self.tipo_cambio,
            "descripcion": self.descripcion,
            "justificacion": self.justificacion,
            "fecha_solicitud": self.fecha_solicitud.isoformat(),
            "fecha_aprobacion": self.fecha_aprobacion.isoformat()
            if self.fecha_aprobacion
            else None,
            "solicitante": self.solicitante,
            "aprobador": self.aprobador,
            "impacto": self.impacto,
            "estado": self.estado,
            "nueva_version": self.nueva_version,
            "cambios": self.cambios,
        }


class GestorProcesosSGSI:
    def __init__(self):
        self.procesos: List[Proceso] = []
        self.mejoras: List[Mejora] = []
        self.actualizaciones: List[Actualizacion] = []
        self._inicializar_procesos_default()

    def _inicializar_procesos_default(self):
        self.procesos = [
            Proceso(
                id="PROC-001",
                nombre="Gestión de Control de Acceso",
                descripcion="Proceso para gestionar el acceso de usuarios a los sistemas de información",
                tipo=TipoProceso.GESTION_ACCESS,
                estado=EstadoProceso.OPERACION,
                version="2.1",
                responsable="CISO",
                controles_iso=["A.9.1", "A.9.2", "A.9.3", "A.9.4"],
                kpis=[
                    {
                        "nombre": "Usuarios con acceso vigente",
                        "valor_objetivo": 100,
                        "unidad": "%",
                    },
                    {
                        "nombre": "Tiempo de aprovisionamiento",
                        "valor_objetivo": 24,
                        "unidad": "horas",
                    },
                ],
            ),
            Proceso(
                id="PROC-002",
                nombre="Gestión de Incidentes de Seguridad",
                descripcion="Proceso para detectar, analizar y responder a incidentes de seguridad",
                tipo=TipoProceso.GESTION_INCIDENTES,
                estado=EstadoProceso.OPERACION,
                version="1.5",
                responsable="SOC Manager",
                controles_iso=["A.16.1", "A.16.1.1", "A.16.1.2"],
                kpis=[
                    {
                        "nombre": "Tiempo medio de respuesta",
                        "valor_objetivo": 60,
                        "unidad": "minutos",
                    },
                    {
                        "nombre": "Incidentes resueltos",
                        "valor_objetivo": 95,
                        "unidad": "%",
                    },
                ],
            ),
            Proceso(
                id="PROC-003",
                nombre="Gestión de Cambios",
                descripcion="Proceso para gestionar cambios en la infraestructura y sistemas",
                tipo=TipoProceso.GESTION_CAMBIOS,
                estado=EstadoProceso.OPERACION,
                version="3.0",
                responsable="IT Manager",
                controles_iso=["A.14.2", "A.14.2.1", "A.14.2.2"],
                kpis=[
                    {
                        "nombre": "Cambios aprobados",
                        "valor_objetivo": 90,
                        "unidad": "%",
                    },
                    {
                        "nombre": "Cambios con testing",
                        "valor_objetivo": 100,
                        "unidad": "%",
                    },
                ],
            ),
            Proceso(
                id="PROC-004",
                nombre="Gestión de Riesgos de Seguridad",
                descripcion="Proceso para identificar, evaluar y tratar riesgos de seguridad",
                tipo=TipoProceso.GESTION_RIESGOS,
                estado=EstadoProceso.OPERACION,
                version="2.0",
                responsable="Risk Manager",
                controles_iso=["A.6.1", "A.6.1.1", "A.6.1.2"],
                kpis=[
                    {
                        "nombre": "Riesgos evaluados",
                        "valor_objetivo": 100,
                        "unidad": "%",
                    },
                    {
                        "nombre": "Riesgos críticos residuales",
                        "valor_objetivo": 0,
                        "unidad": "unidades",
                    },
                ],
            ),
            Proceso(
                id="PROC-005",
                nombre="Gestión de Proveedores",
                descripcion="Proceso para evaluar y gestionar riesgos de terceros",
                tipo=TipoProceso.GESTION_PROVEEDORES,
                estado=EstadoProceso.OPERACION,
                version="1.2",
                responsable="Vendor Manager",
                controles_iso=["A.15.1", "A.15.2", "A.15.3"],
                kpis=[
                    {
                        "nombre": "Proveedores evaluados",
                        "valor_objetivo": 100,
                        "unidad": "%",
                    },
                    {
                        "nombre": "Contratos con cláusulas de seguridad",
                        "valor_objetivo": 100,
                        "unidad": "%",
                    },
                ],
            ),
            Proceso(
                id="PROC-006",
                nombre="Gestión de Pagos Electrónicos",
                descripcion="Proceso para gestionar operaciones de pago en línea de forma segura",
                tipo=TipoProceso.GESTION_POLITICAS,
                estado=EstadoProceso.OPERACION,
                version="1.0",
                responsable="Pagos Manager",
                controles_iso=["A.10.1", "A.10.2", "A.13.1"],
                kpis=[
                    {
                        "nombre": "Transacciones seguras",
                        "valor_objetivo": 100,
                        "unidad": "%",
                    },
                    {"nombre": "Tasa de fraude", "valor_objetivo": 0.1, "unidad": "%"},
                ],
            ),
            Proceso(
                id="PROC-007",
                nombre="Operaciones de Factoring",
                descripcion="Proceso para gestionar operaciones de factoring con seguridad",
                tipo=TipoProceso.CUMPLIMIENTO,
                estado=EstadoProceso.OPERACION,
                version="1.0",
                responsable="Factoring Manager",
                controles_iso=["A.9.1", "A.10.1", "A.12.3"],
                kpis=[
                    {
                        "nombre": "Documentos procesados",
                        "valor_objetivo": 100,
                        "unidad": "%",
                    },
                    {
                        "nombre": "Errores en cesiones",
                        "valor_objetivo": 0.5,
                        "unidad": "%",
                    },
                ],
            ),
            Proceso(
                id="PROC-008",
                nombre="Operaciones de Confirming",
                descripcion="Proceso para gestionar pagos a proveedores via confirming",
                tipo=TipoProceso.CUMPLIMIENTO,
                estado=EstadoProceso.OPERACION,
                version="1.0",
                responsable="Confirming Manager",
                controles_iso=["A.13.1", "A.13.2", "A.9.4"],
                kpis=[
                    {
                        "nombre": "Pagos verificados",
                        "valor_objetivo": 100,
                        "unidad": "%",
                    },
                    {
                        "nombre": "Tiempo de procesamiento",
                        "valor_objetivo": 24,
                        "unidad": "horas",
                    },
                ],
            ),
        ]

    def obtener_proceso(self, proceso_id: str) -> Optional[Proceso]:
        for p in self.procesos:
            if p.id == proceso_id:
                return p
        return None

    def get_procesos_por_tipo(self, tipo: TipoProceso) -> List[Proceso]:
        return [p for p in self.procesos if p.tipo == tipo]

    def get_procesos_por_estado(self, estado: EstadoProceso) -> List[Proceso]:
        return [p for p in self.procesos if p.estado == estado]

    def get_dashboard_procesos(self) -> Dict:
        return {
            "total_procesos": len(self.procesos),
            "por_estado": {
                estado.value: len(self.get_procesos_por_estado(estado))
                for estado in EstadoProceso
            },
            "por_tipo": {
                tipo.value: len(self.get_procesos_por_tipo(tipo))
                for tipo in TipoProceso
            },
            "procesos": [p.to_dict() for p in self.procesos],
        }


class GestorMejoras:
    def __init__(self, gestor_procesos: GestorProcesosSGSI):
        self.gestor_procesos = gestor_procesos
        self.mejoras: List[Mejora] = []

    def identificar_mejora(self, contexto: Dict) -> Dict:
        titulo = contexto.get("titulo", "")
        descripcion = contexto.get("descripcion", "")
        tipo = contexto.get("tipo", "preventiva")
        proceso_origen = contexto.get("proceso_origen", "")

        mejora_id = f"MJR-{len(self.mejoras) + 1:04d}"

        clasificacion = self._clasificar_prioridad(contexto)

        mejora = Mejora(
            id=mejora_id,
            titulo=titulo,
            descripcion=descripcion,
            tipo=TipoMejora[tipo.upper()],
            prioridad=clasificacion,
            proceso_origen=proceso_origen,
            estado="identificada",
        )

        self.mejoras.append(mejora)

        return {
            "mejora_id": mejora_id,
            "mensaje": "Mejora identificada exitosamente",
            "clasificacion": clasificacion.name,
            "proximo_paso": "Evaluar y aprobar mejora",
        }

    def _clasificar_prioridad(self, contexto: Dict) -> PrioridadMejora:
        impacto = contexto.get("impacto", "medio")
        urgencia = contexto.get("urgencia", "media")

        score = 0
        if impacto == "critico":
            score += 3
        elif impacto == "alto":
            score += 2
        elif impacto == "medio":
            score += 1

        if urgencia == "alta":
            score += 2
        elif urgencia == "media":
            score += 1

        if score >= 5:
            return PrioridadMejora.CRITICA
        elif score >= 3:
            return PrioridadMejora.ALTA
        elif score >= 1:
            return PrioridadMejora.MEDIA
        return PrioridadMejora.BAJA

    def evaluar_mejora(self, mejora_id: str) -> Dict:
        mejora = next((m for m in self.mejoras if m.id == mejora_id), None)

        if not mejora:
            return {"error": "Mejora no encontrada"}

        evaluacion = {
            "mejora_id": mejora_id,
            "titulo": mejora.titulo,
            "prioridad": mejora.prioridad.name,
            "criterios_evaluacion": [
                {"criterio": "Viabilidad técnica", "puntuacion": 4, "maximo": 5},
                {"criterio": "Impacto en seguridad", "puntuacion": 4, "maximo": 5},
                {"criterio": "Costo-beneficio", "puntuacion": 3, "maximo": 5},
                {
                    "criterio": "Facilidad de implementación",
                    "puntuacion": 3,
                    "maximo": 5,
                },
                {"criterio": "Soporte de la dirección", "puntuacion": 5, "maximo": 5},
            ],
            "recomendacion": "Aprobar" if 15 else "Revisar",
        }

        return evaluacion

    def aprobar_mejora(self, mejora_id: str, aprobador: str) -> Dict:
        mejora = next((m for m in self.mejoras if m.id == mejora_id), None)

        if not mejora:
            return {"error": "Mejora no encontrada"}

        mejora.estado = "aprobada"
        mejora.historiallo.append(
            {
                "fecha": datetime.now().isoformat(),
                "accion": "Aprobada",
                "usuario": aprobador,
            }
        )

        return {
            "mejora_id": mejora_id,
            "estado": "aprobada",
            "aprobador": aprobador,
            "proximo_paso": "Planificar implementación",
        }

    def planificar_implementacion(self, mejora_id: str, contexto: Dict) -> Dict:
        mejora = next((m for m in self.mejoras if m.id == mejora_id), None)

        if not mejora:
            return {"error": "Mejora no encontrada"}

        mejora.estado = "en_planificacion"

        fases = [
            {"fase": 1, "nombre": "Preparación", "duracion_estimada": "2 semanas"},
            {"fase": 2, "nombre": "Diseño", "duracion_estimada": "3 semanas"},
            {
                "fase": 3,
                "nombre": "Desarrollo/Implementación",
                "duracion_estimada": "6 semanas",
            },
            {"fase": 4, "nombre": "Pruebas", "duracion_estimada": "2 semanas"},
            {"fase": 5, "nombre": "Despliegue", "duracion_estimada": "1 semana"},
            {"fase": 6, "nombre": "Seguimiento", "duracion_estimada": "4 semanas"},
        ]

        return {
            "mejora_id": mejora_id,
            "fases": fases,
            "duracion_total": "18 semanas",
            "recursos_necesarios": {
                "personal": ["Analista de seguridad", "Desarrollador"],
                "herramientas": ["Por definir"],
                "presupuesto": "Por estimar",
            },
        }

    def implementar_mejora(self, mejora_id: str) -> Dict:
        mejora = next((m for m in self.mejoras if m.id == mejora_id), None)

        if not mejora:
            return {"error": "Mejora no encontrada"}

        mejora.estado = "implementada"
        mejora.fecha_implementacion = datetime.now()
        mejora.historiallo.append(
            {"fecha": datetime.now().isoformat(), "accion": "Implementada"}
        )

        return {
            "mejora_id": mejora_id,
            "estado": "implementada",
            "fecha_implementacion": mejora.fecha_implementacion.isoformat(),
            "verificacion_requerida": True,
        }

    def verificar_implementacion(self, mejora_id: str, contexto: Dict) -> Dict:
        resultados = contexto.get("resultados", {})

        return {
            "mejora_id": mejora_id,
            "verificacion": {
                "objetivos_logrados": resultados.get("objetivos_logrados", True),
                " KPIs_cumplidos": resultados.get("kpis_cumplidos", True),
                "beneficios_obtenidos": resultados.get("beneficios_obtenidos", []),
            },
            "estado_final": "cerrada",
            "lecciones_aprendidas": [],
        }

    def get_resumen_mejoras(self) -> Dict:
        return {
            "total": len(self.mejoras),
            "por_estado": {
                "identificadas": len(
                    [m for m in self.mejoras if m.estado == "identificada"]
                ),
                "aprobadas": len([m for m in self.mejoras if m.estado == "aprobada"]),
                "en_planificacion": len(
                    [m for m in self.mejoras if m.estado == "en_planificacion"]
                ),
                "implementadas": len(
                    [m for m in self.mejoras if m.estado == "implementada"]
                ),
                "cerradas": len([m for m in self.mejoras if m.estado == "cerrada"]),
            },
            "por_prioridad": {
                "criticas": len(
                    [m for m in self.mejoras if m.prioridad == PrioridadMejora.CRITICA]
                ),
                "altas": len(
                    [m for m in self.mejoras if m.prioridad == PrioridadMejora.ALTA]
                ),
                "medias": len(
                    [m for m in self.mejoras if m.prioridad == PrioridadMejora.MEDIA]
                ),
                "bajas": len(
                    [m for m in self.mejoras if m.prioridad == PrioridadMejora.BAJA]
                ),
            },
        }


class GestorActualizaciones:
    def __init__(self, gestor_procesos: GestorProcesosSGSI):
        self.gestor_procesos = gestor_procesos
        self.actualizaciones: List[Actualizacion] = []

    def solicitar_actualizacion(self, contexto: Dict) -> Dict:
        proceso_id = contexto.get("proceso_id", "")
        tipo_cambio = contexto.get("tipo_cambio", "")
        descripcion = contexto.get("descripcion", "")
        justificacion = contexto.get("justificacion", "")
        solicitante = contexto.get("solicitante", "")

        actualizacion_id = f"ACT-{len(self.actualizaciones) + 1:04d}"

        actualizacion = Actualizacion(
            id=actualizacion_id,
            proceso_id=proceso_id,
            tipo_cambio=tipo_cambio,
            descripcion=descripcion,
            justificacion=justificacion,
            solicitante=solicitante,
            estado="pendiente",
        )

        self.actualizaciones.append(actualizacion)

        return {
            "actualizacion_id": actualizacion_id,
            "mensaje": "Solicitud de actualización creada",
            "proximo_paso": "Revisión y aprobación",
        }

    def evaluar_actualizacion(self, actualizacion_id: str) -> Dict:
        actualizacion = next(
            (a for a in self.actualizaciones if a.id == actualizacion_id), None
        )

        if not actualizacion:
            return {"error": "Actualización no encontrada"}

        proceso = self.gestor_procesos.obtener_proceso(actualizacion.proceso_id)

        evaluacion = {
            "actualizacion_id": actualizacion_id,
            "proceso": proceso.nombre if proceso else "Desconocido",
            "tipo_cambio": actualizacion.tipo_cambio,
            "impacto_estimado": "Medio",
            "riesgos": ["Minor delay", "Learning curve"],
            "recomendacion": "Aprobar",
        }

        return evaluacion

    def aprobar_actualizacion(self, actualizacion_id: str, aprobador: str) -> Dict:
        actualizacion = next(
            (a for a in self.actualizaciones if a.id == actualizacion_id), None
        )

        if not actualizacion:
            return {"error": "Actualización no encontrada"}

        actualizacion.estado = "aprobada"
        actualizacion.fecha_aprobacion = datetime.now()
        actualizacion.aprobador = aprobador

        proceso = self.gestor_procesos.obtener_proceso(actualizacion.proceso_id)
        if proceso:
            version_actual = float(proceso.version)
            actualizacion.nueva_version = f"{version_actual + 0.1:.1f}"

        return {
            "actualizacion_id": actualizacion_id,
            "estado": "aprobada",
            "nueva_version": actualizacion.nueva_version,
            "proximo_paso": "Ejecutar actualización",
        }

    def ejecutar_actualizacion(self, actualizacion_id: str) -> Dict:
        actualizacion = next(
            (a for a in self.actualizaciones if a.id == actualizacion_id), None
        )

        if not actualizacion:
            return {"error": "Actualización no encontrada"}

        actualizacion.estado = "completada"

        proceso = self.gestor_procesos.obtener_proceso(actualizacion.proceso_id)
        if proceso:
            proceso.version = actualizacion.nueva_version
            proceso.fecha_ultima_actualizacion = datetime.now()

        return {
            "actualizacion_id": actualizacion_id,
            "estado": "completada",
            "proceso_id": actualizacion.proceso_id,
            "nueva_version": actualizacion.nueva_version,
            "documentacion_requerida": True,
        }

    def get_resumen_actualizaciones(self) -> Dict:
        return {
            "total": len(self.actualizaciones),
            "por_estado": {
                "pendientes": len(
                    [a for a in self.actualizaciones if a.estado == "pendiente"]
                ),
                "aprobadas": len(
                    [a for a in self.actualizaciones if a.estado == "aprobada"]
                ),
                "completadas": len(
                    [a for a in self.actualizaciones if a.estado == "completada"]
                ),
            },
        }


class MotorMejoraSGSI:
    def __init__(self):
        self.gestor_procesos = GestorProcesosSGSI()
        self.gestor_mejoras = GestorMejoras(self.gestor_procesos)
        self.gestor_actualizaciones = GestorActualizaciones(self.gestor_procesos)

    def analizar_y_mejorar(self, contexto: Dict) -> Dict:
        area = contexto.get("area", "")
        metricas = contexto.get("metricas", {})

        recomendaciones = []

        if area == "factoring":
            if metricas.get("acceso", 0) < 90:
                recomendaciones.append(
                    {
                        "tipo": "correctiva",
                        "titulo": "Mejorar controles de acceso en factoring",
                        "descripcion": "Los controles de acceso están por debajo del objetivo",
                        "prioridad": "alta",
                    }
                )

        if area == "pagos":
            if metricas.get("disponibilidad", 0) < 99.9:
                recomendaciones.append(
                    {
                        "tipo": "preventiva",
                        "titulo": "Mejorar disponibilidad de pagos",
                        "descripcion": "El uptime está por debajo del SLA",
                        "prioridad": "critica",
                    }
                )

        return {
            "area": area,
            "recomendaciones": recomendaciones,
            "mejoras_sugeridas": len(recomendaciones),
        }

    def ejecutar_mejora_completa(self, contexto: Dict) -> Dict:
        titulo = contexto.get("titulo", "")
        descripcion = contexto.get("descripcion", "")
        proceso_origen = contexto.get("proceso_origen", "")

        resultado_iden = self.gestor_mejoras.identificar_mejora(
            {
                "titulo": titulo,
                "descripcion": descripcion,
                "proceso_origen": proceso_origen,
                "tipo": "preventiva",
                "impacto": "alto",
                "urgencia": "media",
            }
        )

        resultado_eval = self.gestor_mejoras.evaluar_mejora(resultado_iden["mejora_id"])

        resultado_aprob = self.gestor_mejoras.aprobar_mejora(
            resultado_iden["mejora_id"], contexto.get("aprobador", "CISO")
        )

        resultado_plan = self.gestor_mejoras.planificar_implementacion(
            resultado_iden["mejora_id"], contexto
        )

        return {
            "mejora_id": resultado_iden["mejora_id"],
            "flujo_completo": {
                "identificacion": "completada",
                "evaluacion": "completada",
                "aprobacion": "completada",
                "planificacion": "completada",
            },
            "fases": resultado_plan["fases"],
            "duracion_total": resultado_plan["duracion_total"],
        }

    def get_estado_sgsi(self) -> Dict:
        return {
            "procesos": self.gestor_procesos.get_dashboard_procesos(),
            "mejoras": self.gestor_mejoras.get_resumen_mejoras(),
            "actualizaciones": self.gestor_actualizaciones.get_resumen_actualizaciones(),
            "indicadores_clave": {
                "procesos_operacionales": len(
                    self.gestor_procesos.get_procesos_por_estado(
                        EstadoProceso.OPERACION
                    )
                ),
                "mejoras_en_curso": len(
                    [
                        m
                        for m in self.gestor_mejoras.mejoras
                        if m.estado in ["aprobada", "en_planificacion"]
                    ]
                ),
                "actualizaciones_pendientes": len(
                    [
                        a
                        for a in self.gestor_actualizaciones.actualizaciones
                        if a.estado == "pendiente"
                    ]
                ),
            },
        }

    def generar_plan_mejora_anual(self) -> Dict:
        areas_mejora = [
            {
                "area": "Gestión de Acceso",
                "objetivo": "Alcanzar 95% de cumplimiento",
                "plazo": "Q1",
            },
            {
                "area": "Detección de Amenazas",
                "objetivo": "Reducir tiempo de detección a 15 min",
                "plazo": "Q2",
            },
            {
                "area": "Capacitación",
                "objetivo": "100% del personal capacitado",
                "plazo": "Q3",
            },
            {"area": "Continuidad", "objetivo": "Actualizar BCP", "plazo": "Q4"},
        ]

        return {
            "plan_anual": areas_mejora,
            "presupuesto_estimado": "Por definir",
            "recursos_necesarios": [
                "CISO",
                "Equipo de seguridad",
                "Consultores externos",
            ],
            "proximarevision": "Trimestral",
        }
