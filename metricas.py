"""
Templates de Métricas ISO 27001:2022
Sistema de Gestión de Seguridad de la Información (SGSI)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum
from datetime import datetime
import json


class CategoriaControl(Enum):
    ORGANIZACIONAL = "A.5"
    PERSONAS = "A.6"
    FISICO = "A.7"
    TECNOLOGICO = "A.8"
    ACCESO = "A.9"
    CRIPTOGRAFIA = "A.10"
    OPERACIONES = "A.11"
    COMUNICACIONES = "A.12"
    ADQUISICION = "A.13"
    PROVEEDORES = "A.14"
    INCIDENTES = "A.15"
    CONTINUIDAD = "A.16"
    CUMPLIMIENTO = "A.17"


class TipoMetrica(Enum):
    CUMPLIMIENTO = "cumplimiento"
    EFECTIVIDAD = "efectividad"
    RIESGO = "riesgo"
    INCIDENTE = "incidente"
    AUDITORIA = "auditoria"
    MEJORA = "mejora"


class EstadoCumplimiento(Enum):
    CUMPLIDO = "cumplido"
    PARCIAL = "parcial"
    NO_CUMPLIDO = "no_cumplido"
    NO_APLICA = "no_aplica"
    EN_PROCESO = "en_proceso"


@dataclass
class UmbralMetrica:
    minimo: float
    objetivo: float
    maximo: float
    unidad: str

    def evaluar(self, valor: float) -> EstadoCumplimiento:
        if valor >= self.objetivo:
            return EstadoCumplimiento.CUMPLIDO
        elif valor >= self.minimo:
            return EstadoCumplimiento.PARCIAL
        else:
            return EstadoCumplimiento.NO_CUMPLIDO


@dataclass
class MetricaTemplate:
    id: str
    nombre: str
    descripcion: str
    categoria: CategoriaControl
    tipo: TipoMetrica
    formula: str
    umbral: UmbralMetrica
    fuente_datos: List[str]
    frecuencia: str
    responsable: str
    controles_relacionados: List[str]
    aplicabilidad: List[str] = field(default_factory=list)
    notas: str = ""

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "categoria": self.categoria.value,
            "tipo": self.tipo.value,
            "formula": self.formula,
            "umbral": {
                "minimo": self.umbral.minimo,
                "objetivo": self.umbral.objetivo,
                "maximo": self.umbral.maximo,
                "unidad": self.umbral.unidad,
            },
            "fuente_datos": self.fuente_datos,
            "frecuencia": self.frecuencia,
            "responsable": self.responsable,
            "controles_relacionados": self.controles_relacionados,
            "aplicabilidad": self.aplicabilidad,
            "notas": self.notas,
        }


class TemplatesMetricas:
    @staticmethod
    def get_templates_financieros() -> List[MetricaTemplate]:
        return [
            MetricaTemplate(
                id="M-ISO-001",
                nombre="Tasa de Cumplimiento de Controles de Acceso",
                descripcion="Porcentaje de controles de acceso implementados y operativos",
                categoria=CategoriaControl.ACCESO,
                tipo=TipoMetrica.CUMPLIMIENTO,
                formula="(controles_implementados / total_controles) * 100",
                umbral=UmbralMetrica(minimo=70, objetivo=95, maximo=100, unidad="%"),
                fuente_datos=["IAM", "AD", "SIEM"],
                frecuencia="mensual",
                responsable="CISO",
                controles_relacionados=["A.9.1", "A.9.2", "A.9.3", "A.9.4"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Crítico para protección de datos financieros",
            ),
            MetricaTemplate(
                id="M-ISO-002",
                nombre="Tiempo de Detección de Intrusiones",
                descripcion="Tiempo promedio desde detección hasta notificación de incidentes de seguridad",
                categoria=CategoriaControl.OPERACIONES,
                tipo=TipoMetrica.EFECTIVIDAD,
                formula="SUM(tiempo_deteccion) / total_incidentes",
                umbral=UmbralMetrica(
                    minimo=60, objetivo=15, maximo=5, unidad="minutos"
                ),
                fuente_datos=["SIEM", "IPS/IDS", "SOC"],
                frecuencia="mensual",
                responsable="SOC Manager",
                controles_relacionados=["A.12.1", "A.12.2", "A.12.3"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="PCI-DSS requiere detección en minutos",
            ),
            MetricaTemplate(
                id="M-ISO-003",
                nombre="Porcentaje de Transacciones Fraudulentas Detectadas",
                descripcion="Tasa de detección de intentos de fraude en operaciones de factoring y confirming",
                categoria=CategoriaControl.COMUNICACIONES,
                tipo=TipoMetrica.RIESGO,
                formula="(transacciones_fraude_detectadas / total_transacciones_sospechosas) * 100",
                umbral=UmbralMetrica(minimo=80, objetivo=98, maximo=100, unidad="%"),
                fuente_datos=["Sistema antiscore", "Monitoring"],
                frecuencia="diaria",
                responsable="Fraude Manager",
                controles_relacionados=["A.13.1", "A.13.2"],
                aplicabilidad=["factoring", "confirming"],
                notas="Crítico para operaciones financieras",
            ),
            MetricaTemplate(
                id="M-ISO-004",
                nombre="Disponibilidad de Sistemas de Pago",
                descripcion="Porcentaje de disponibilidad de sistemas de pagos en línea",
                categoria=CategoriaControl.CONTINUIDAD,
                tipo=TipoMetrica.EFECTIVIDAD,
                formula="((total_minutos - minutos_indisponibilidad) / total_minutos) * 100",
                umbral=UmbralMetrica(
                    minimo=99.5, objetivo=99.99, maximo=100, unidad="%"
                ),
                fuente_datos=["Monitoring", "APM"],
                frecuencia="mensual",
                responsable="COO",
                controles_relacionados=["A.17.1", "A.17.2"],
                aplicabilidad=["pagos_linea"],
                notas="SLA crítico para servicios financieros",
            ),
            MetricaTemplate(
                id="M-ISO-005",
                nombre="Cumplimiento de Política de Contraseñas",
                descripcion="Porcentaje de cuentas que cumplen política de contraseñas robusta",
                categoria=CategoriaControl.ACCESO,
                tipo=TipoMetrica.CUMPLIMIENTO,
                formula="(cuentas_cumplen / total_cuentas) * 100",
                umbral=UmbralMetrica(minimo=90, objetivo=100, maximo=100, unidad="%"),
                fuente_datos=["IAM", "AD"],
                frecuencia="semanal",
                responsable="Seguridad IT",
                controles_relacionados=["A.9.4", "A.9.5"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Control crítico A.9.4.1",
            ),
            MetricaTemplate(
                id="M-ISO-006",
                nombre="Incidentes de Seguridad por Categoría",
                descripcion="Distribución de incidentes de seguridad por tipo y severidad",
                categoria=CategoriaControl.INCIDENTES,
                tipo=TipoMetrica.INCIDENTE,
                formula="COUNT(incidentes_por_categoria) GROUP BY severidad",
                umbral=UmbralMetrica(
                    minimo=0, objetivo=0, maximo=5, unidad="incidentes"
                ),
                fuente_datos=["ServiceDesk", "SIEM", "Ticketing"],
                frecuencia="mensual",
                responsable="CISO",
                controles_relacionados=["A.16.1", "A.16.1.1"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Tracking de tendencias",
            ),
            MetricaTemplate(
                id="M-ISO-007",
                nombre="Cobertura de Capacitación en Seguridad",
                descripcion="Porcentaje de empleados capacitados en seguridad de la información",
                categoria=CategoriaControl.PERSONAS,
                tipo=TipoMetrica.CUMPLIMIENTO,
                formula="(empleados_capacitados / total_empleados) * 100",
                umbral=UmbralMetrica(minimo=80, objetivo=100, maximo=100, unidad="%"),
                fuente_datos=["LMS", "RRHH"],
                frecuencia="trimestral",
                responsable="RRHH",
                controles_relacionados=["A.7.2", "A.7.2.1"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Capacitación obligatoria anual",
            ),
            MetricaTemplate(
                id="M-ISO-008",
                nombre="Auditorías Internas Completadas",
                descripcion="Porcentaje de auditorías internas programadas completadas",
                categoria=CategoriaControl.CUMPLIMIENTO,
                tipo=TipoMetrica.AUDITORIA,
                formula="(auditorias_completadas / auditorias_programadas) * 100",
                umbral=UmbralMetrica(minimo=90, objetivo=100, maximo=100, unidad="%"),
                fuente_datos=["Plan Auditoría", "Informes"],
                frecuencia="trimestral",
                responsable="Auditor Interno",
                controles_relacionados=["A.18.1", "A.18.2"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Requisito ISO 27001",
            ),
            MetricaTemplate(
                id="M-ISO-009",
                nombre="Vulnerabilidades Críticas Pendientes",
                descripcion="Número de vulnerabilidades críticas sin remediar",
                categoria=CategoriaControl.TECNOLOGICO,
                tipo=TipoMetrica.RIESGO,
                formula="COUNT(vulnerabilidades_criticas WHERE estado != 'remediado')",
                umbral=UmbralMetrica(
                    minimo=5, objetivo=0, maximo=0, unidad="vulnerabilidades"
                ),
                fuente_datos=["VA Scanner", "GRC"],
                frecuencia="semanal",
                responsable="Vuln Manager",
                controles_relacionados=["A.12.6", "A.12.6.1"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="SLAs: Críticas 24h, Altas 7 días",
            ),
            MetricaTemplate(
                id="M-ISO-010",
                nombre="Cumplimiento de Proveedores Críticos",
                descripcion="Porcentaje de proveedores críticos que cumplen requisitos de seguridad",
                categoria=CategoriaControl.PROVEEDORES,
                tipo=TipoMetrica.CUMPLIMIENTO,
                formula="(proveedores_cumplen / proveedores_criticos) * 100",
                umbral=UmbralMetrica(minimo=85, objetivo=100, maximo=100, unidad="%"),
                fuente_datos=["VRM", "Contratos"],
                frecuencia="trimestral",
                responsable="Vendor Manager",
                controles_relacionados=["A.15.1", "A.15.2", "A.15.3"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Evaluación anual mínima",
            ),
            MetricaTemplate(
                id="M-ISO-011",
                nombre="Tasa de Cifrado de Datos en Tránsito",
                descripcion="Porcentaje de comunicaciones cifradas correctamente",
                categoria=CategoriaControl.CRIPTOGRAFIA,
                tipo=TipoMetrica.CUMPLIMIENTO,
                formula="(comunicaciones_cifradas / total_comunicaciones) * 100",
                umbral=UmbralMetrica(minimo=95, objetivo=100, maximo=100, unidad="%"),
                fuente_datos=["WAF", "Proxy", "Firewall"],
                frecuencia="mensual",
                responsable="Infraestructura",
                controles_relacionados=["A.10.1", "A.10.1.1"],
                aplicabilidad=["pagos_linea"],
                notas="TLS 1.2+ requerido",
            ),
            MetricaTemplate(
                id="M-ISO-012",
                nombre="Eficacia del Plan de Continuidad",
                descripcion="Porcentaje de pruebas de continuidad exitosas",
                categoria=CategoriaControl.CONTINUIDAD,
                tipo=TipoMetrica.MEJORA,
                formula="(pruebas_exitosas / total_pruebas) * 100",
                umbral=UmbralMetrica(minimo=70, objetivo=90, maximo=100, unidad="%"),
                fuente_datos=["BCP", "Drills"],
                frecuencia="semestral",
                responsable="BCM Manager",
                controles_relacionados=["A.17.1", "A.17.2"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Mínimo 2 pruebas anuales",
            ),
            MetricaTemplate(
                id="M-ISO-013",
                nombre="Evaluación de Riesgo Actualizada",
                descripcion="Días desde última evaluación de riesgos",
                categoria=CategoriaControl.ORGANIZACIONAL,
                tipo=TipoMetrica.CUMPLIMIENTO,
                formula="DIFERENCIA(fecha_actual, fecha_ultima_evaluacion)",
                umbral=UmbralMetrica(
                    minimo=365, objetivo=180, maximo=90, unidad="días"
                ),
                fuente_datos=["GRC", "Risk Register"],
                frecuencia="trimestral",
                responsable="Risk Manager",
                controles_relacionados=["A.6.1", "A.6.1.1"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Evaluación anual mínima, trimestral preferible",
            ),
            MetricaTemplate(
                id="M-ISO-014",
                nombre="Backups Exitosos",
                descripcion="Porcentaje de backups completados exitosamente",
                categoria=CategoriaControl.OPERACIONES,
                tipo=TipoMetrica.EFECTIVIDAD,
                formula="(backups_exitosos / total_backups_programados) * 100",
                umbral=UmbralMetrica(minimo=98, objetivo=100, maximo=100, unidad="%"),
                fuente_datos=["Backup Manager"],
                frecuencia="diaria",
                responsable=" DBA",
                controles_relacionados=["A.12.3", "A.12.3.1"],
                aplicabilidad=["factoring", "confirming", "pagos_linea"],
                notas="Pruebas de restauración mensuales",
            ),
            MetricaTemplate(
                id="M-ISO-015",
                nombre="Tokens de Pago Seguro Emitidos",
                descripcion="Porcentaje de transacciones que usan tokenización",
                categoria=CategoriaControl.CRIPTOGRAFIA,
                tipo=TipoMetrica.EFECTIVIDAD,
                formula="(transacciones_tokenizadas / total_transacciones) * 100",
                umbral=UmbralMetrica(minimo=50, objetivo=85, maximo=100, unidad="%"),
                fuente_datos=["Payment Gateway", "Tokenization Service"],
                frecuencia="mensual",
                responsable="Pagos Manager",
                controles_relacionados=["A.10.1", "A.10.2"],
                aplicabilidad=["pagos_linea"],
                notas="PCI-DSS requirement",
            ),
        ]

    @staticmethod
    def get_template_json() -> str:
        templates = TemplatesMetricas.get_templates_financieros()
        return json.dumps(
            [t.to_dict() for t in templates], indent=2, ensure_ascii=False
        )


@dataclass
class RegistroMetrica:
    metrica_id: str
    fecha: datetime
    valor: float
    estado: EstadoCumplimiento
    observaciones: str = ""
    evidencia: List[str] = field(default_factory=list)
    responsable: str = ""

    def to_dict(self) -> Dict:
        return {
            "metrica_id": self.metrica_id,
            "fecha": self.fecha.isoformat(),
            "valor": self.valor,
            "estado": self.estado.value,
            "observaciones": self.observaciones,
            "evidencia": self.evidencia,
            "responsable": self.responsable,
        }


class GestorMetricas:
    def __init__(self):
        self.templates: List[MetricaTemplate] = (
            TemplatesMetricas.get_templates_financieros()
        )
        self.registros: List[RegistroMetrica] = []

    def get_metrica(self, metrica_id: str) -> Optional[MetricaTemplate]:
        for t in self.templates:
            if t.id == metrica_id:
                return t
        return None

    def evaluar_metrica(self, metrica_id: str, valor: float) -> Dict:
        metrica = self.get_metrica(metrica_id)
        if not metrica:
            return {"error": "Métrica no encontrada"}

        estado = metrica.umbral.evaluar(valor)
        return {
            "metrica_id": metrica_id,
            "nombre": metrica.nombre,
            "valor": valor,
            "estado": estado.value,
            "umbral": {
                "minimo": metrica.umbral.minimo,
                "objetivo": metrica.umbral.objetivo,
                "unidad": metrica.umbral.unidad,
            },
        }

    def agregar_registro(self, registro: RegistroMetrica):
        self.registros.append(registro)

    def get_registros_por_metrica(self, metrica_id: str) -> List[Dict]:
        return [r.to_dict() for r in self.registros if r.metrica_id == metrica_id]

    def get_dashboard_resumen(self) -> Dict:
        total = len(self.templates)
        evaluados = len([r for r in self.registros])

        return {
            "total_metricas": total,
            "registros_totales": evaluados,
            "metricas": [t.to_dict() for t in self.templates],
        }
