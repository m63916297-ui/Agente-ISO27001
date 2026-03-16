"""
Criterios Específicos ISO 27001 para Operaciones de Factoring, Confirming y Pagos en Línea
Sistema Multiagente de Certificación
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
import json


class TipoOperacion(Enum):
    FACTORING = "factoring"
    CONFIRMING = "confirming"
    PAGOS_LINEA = "pagos_linea"


class CategoriaRiesgo(Enum):
    CREDITICIO = "crediticio"
    OPERACIONAL = "operacional"
    CIBERSEGURIDAD = "ciberseguridad"
    CUMPLIMIENTO = "cumplimiento"
    REPUTACIONAL = "reputacional"
    LEGAL = "legal"


class NivelCriticidad(Enum):
    CRITICO = "critico"
    ALTO = "alto"
    MEDIO = "medio"
    BAJO = "bajo"


@dataclass
class ControlISO:
    codigo: str
    nombre: str
    descripcion: str
    aplicabilidad: List[TipoOperacion]
    criticidad: NivelCriticidad
    implementado: bool = False
    evidencia: List[str] = field(default_factory=list)
    observaciones: str = ""

    def to_dict(self) -> Dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "aplicabilidad": [a.value for a in self.aplicabilidad],
            "criticidad": self.criticidad.value,
            "implementado": self.implementado,
            "evidencia": self.evidencia,
            "observaciones": self.observaciones,
        }


@dataclass
class CriterioEvaluacion:
    id: str
    nombre: str
    descripcion: str
    tipo_operacion: TipoOperacion
    categoria_riesgo: CategoriaRiesgo
    controles_relacionados: List[str]
    requisitos_normativos: List[str]
    preguntas_evaluacion: List[str]
    evidencia_requerida: List[str]
    peso: float = 1.0

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "tipo_operacion": self.tipo_operacion.value,
            "categoria_riesgo": self.categoria_riesgo.value,
            "controles_relacionados": self.controles_relacionados,
            "requisitos_normativos": self.requisitos_normativos,
            "preguntas_evaluacion": self.preguntas_evaluacion,
            "evidencia_requerida": self.evidencia_requerida,
            "peso": self.peso,
        }


class CriteriosFactoring:
    @staticmethod
    def get_criterios() -> List[CriterioEvaluacion]:
        return [
            CriterioEvaluacion(
                id="CF-001",
                nombre="Protección de Datos de Cartera Cedida",
                descripcion="Garantizar la confidencialidad e integridad de los datos de facturas y cartera cedida",
                tipo_operacion=TipoOperacion.FACTORING,
                categoria_riesgo=CategoriaRiesgo.CIBERSEGURIDAD,
                controles_relacionados=["A.10.1", "A.10.2", "A.9.1", "A.9.2"],
                requisitos_normativos=["ISO27001 A.10", "PCI-DSS 3.4", "LOPD"],
                preguntas_evaluacion=[
                    "¿Los datos de facturas están cifrados en reposo?",
                    "¿Se usa cifrado AES-256 para datos sensibles?",
                    "¿Existe control de acceso basado en roles para datos de cartera?",
                ],
                evidencia_requerida=[
                    "Política de cifrado",
                    "Certificados de cifrado",
                    "Matriz de controles de acceso",
                ],
                peso=2.0,
            ),
            CriterioEvaluacion(
                id="CF-002",
                nombre="Autenticación en Sistema de Factoring",
                descripcion="Verificar la identidad de usuarios en el sistema de factoring",
                tipo_operacion=TipoOperacion.FACTORING,
                categoria_riesgo=CategoriaRiesgo.CIBERSEGURIDAD,
                controles_relacionados=["A.9.1", "A.9.2", "A.9.4", "A.9.5"],
                requisitos_normativos=["ISO27001 A.9", "PSD2", "SCA"],
                preguntas_evaluacion=[
                    "¿Se implementa MFA para acceso al sistema?",
                    "¿Los protocolos de autenticación son robustos?",
                    "¿Existe bloqueo automático de sesiones?",
                ],
                evidencia_requerida=[
                    "Configuración IAM",
                    "Logs de autenticación",
                    "Política de contraseñas",
                ],
                peso=2.5,
            ),
            CriterioEvaluacion(
                id="CF-003",
                nombre="Integridad de Procesos de Cesión",
                descripcion="Garantizar que los procesos de cesión de facturas sean auditables e inmutables",
                tipo_operacion=TipoOperacion.FACTORING,
                categoria_riesgo=CategoriaRiesgo.OPERACIONAL,
                controles_relacionados=["A.12.3", "A.12.4", "A.16.1"],
                requisitos_normativos=["ISO27001 A.12", "SOX"],
                preguntas_evaluacion=[
                    "¿Los registros de cesión son inmutables?",
                    "¿Existe trazabilidad completa de operaciones?",
                    "¿Se guardan logs de todas las operaciones?",
                ],
                evidencia_requerida=[
                    "Logs de auditoría",
                    "Procedimientos de backup",
                    "Políticas de retención",
                ],
                peso=1.5,
            ),
            CriterioEvaluacion(
                id="CF-004",
                nombre="Gestión de Riesgos Crediticios",
                descripcion="Evaluar y gestionar riesgos asociados a deudores y cedentes",
                tipo_operacion=TipoOperacion.FACTORING,
                categoria_riesgo=CategoriaRiesgo.CREDITICIO,
                controles_relacionados=["A.6.1", "A.6.1.1", "A.6.1.2"],
                requisitos_normativos=["ISO27001 A.6", "Basilea III"],
                preguntas_evaluacion=[
                    "¿Existe evaluación de riesgos crediticios documentada?",
                    "¿Se actualiza periódicamente la evaluación de riesgos?",
                    "¿Se tienen controles para prevenir fraude en cesiones?",
                ],
                evidencia_requerida=[
                    "Matriz de riesgos",
                    "Politicas de underwriting",
                    "Informes de riesgo",
                ],
                peso=2.0,
            ),
            CriterioEvaluacion(
                id="CF-005",
                nombre="Continuidad en Cobranza",
                descripcion="Garantizar la continuidad de operaciones de cobranza",
                tipo_operacion=TipoOperacion.FACTORING,
                categoria_riesgo=CategoriaRiesgo.OPERACIONAL,
                controles_relacionados=["A.17.1", "A.17.2", "A.17.3"],
                requisitos_normativos=["ISO27001 A.17", "BCP"],
                preguntas_evaluacion=[
                    "¿Existe plan de continuidad para cobranza?",
                    "¿Se prueban los procedimientos de recuperación?",
                    "¿Se tienen sistemas alternativos de cobranza?",
                ],
                evidencia_requerida=[
                    "Plan de continuidad",
                    "Resultados de simulacros",
                    "RTO/RPO definidos",
                ],
                peso=1.5,
            ),
            CriterioEvaluacion(
                id="CF-006",
                nombre="Protección de Información de Clientes",
                descripcion="Salvaguardar datos personales y financieros de clientes de factoring",
                tipo_operacion=TipoOperacion.FACTORING,
                categoria_riesgo=CategoriaRiesgo.LEGAL,
                controles_relacionados=["A.8.2", "A.8.3", "A.8.4"],
                requisitos_normativos=["ISO27001 A.8", "GDPR", "LGPD"],
                preguntas_evaluacion=[
                    "¿Se tiene aviso de privacidad actualizado?",
                    "¿Los clientes pueden ejercer sus derechos ARCO?",
                    "¿Existe gestión de consentimiento?",
                ],
                evidencia_requerida=[
                    "Aviso de privacidad",
                    "Registros de consentimiento",
                    "Procedimientos ARCO",
                ],
                peso=2.0,
            ),
        ]


class CriteriosConfirming:
    @staticmethod
    def get_criterios() -> List[CriterioEvaluacion]:
        return [
            CriterioEvaluacion(
                id="CC-001",
                nombre="Seguridad en Gestión de Pagos a Proveedores",
                descripcion="Proteger operaciones de pago a proveedores a través de confirming",
                tipo_operacion=TipoOperacion.CONFIRMING,
                categoria_riesgo=CategoriaRiesgo.CIBERSEGURIDAD,
                controles_relacionados=["A.13.1", "A.13.2", "A.9.4"],
                requisitos_normativos=["ISO27001 A.13", "PCI-DSS", "PSD2"],
                preguntas_evaluacion=[
                    "¿Los pagos a proveedores requieren aprobación multiple?",
                    "¿Se validan las cuentas beneficiarias?",
                    "¿Existe control dual en pagos mayores a umbral?",
                ],
                evidencia_requerida=[
                    "Flujo de aprobación",
                    "Listas negras de cuentas",
                    "Logs de pagos",
                ],
                peso=2.5,
            ),
            CriterioEvaluacion(
                id="CC-002",
                nombre="Integración con Sistemas ERP",
                descripcion="Garantizar seguridad en integración con sistemas ERP de clientes",
                tipo_operacion=TipoOperacion.CONFIRMING,
                categoria_riesgo=CategoriaRiesgo.OPERACIONAL,
                controles_relacionados=["A.13.2", "A.14.1", "A.14.3"],
                requisitos_normativos=["ISO27001 A.13", "A.14", "SOX"],
                preguntas_evaluacion=[
                    "¿Las integraciones usan APIs seguras?",
                    "¿Se validan datos recibidos de sistemas externos?",
                    "¿Existe logging de todas las integraciones?",
                ],
                evidencia_requerida=[
                    "Documentación de APIs",
                    "Certificados SSL/TLS",
                    "Logs de integración",
                ],
                peso=1.5,
            ),
            CriterioEvaluacion(
                id="CC-003",
                nombre="Protección de Datos Bancarios",
                descripcion="Salvaguardar información bancaria y financiera de proveedores",
                tipo_operacion=TipoOperacion.CONFIRMING,
                categoria_riesgo=CategoriaRiesgo.LEGAL,
                controles_relacionados=["A.10.1", "A.10.2", "A.8.2"],
                requisitos_normativos=["ISO27001 A.10", "PCI-DSS", "GDPR"],
                preguntas_evaluacion=[
                    "¿Los datos bancarios están cifrados?",
                    "¿Se mascara información sensible en pantallas?",
                    "¿Existe tokenización de datos de cuentas?",
                ],
                evidencia_requerida=[
                    "Política de cifrado",
                    "Configuración masking",
                    "Certificados PCI-DSS",
                ],
                peso=2.0,
            ),
            CriterioEvaluacion(
                id="CC-004",
                nombre="Control de Fraude en Confirming",
                descripcion="Prevenir fraudes en operaciones de confirming",
                tipo_operacion=TipoOperacion.CONFIRMING,
                categoria_riesgo=CategoriaRiesgo.CREDITICIO,
                controles_relacionados=["A.12.2", "A.12.3", "A.16.1"],
                requisitos_normativos=["ISO27001 A.12", "AML"],
                preguntas_evaluacion=[
                    "¿Se detectan patrones de fraude?",
                    "¿Existe lista OFAC actualizada?",
                    "¿Se realizan verificaciones de beneficiarios?",
                ],
                evidencia_requerida=[
                    "Sistema de detección de fraude",
                    "Listas de verificación",
                    "Alertas de fraude",
                ],
                peso=2.5,
            ),
            CriterioEvaluacion(
                id="CC-005",
                nombre="Auditoría de Operaciones de Pago",
                descripcion="Mantener trazabilidad completa de operaciones de pago",
                tipo_operacion=TipoOperacion.CONFIRMING,
                categoria_riesgo=CategoriaRiesgo.CUMPLIMIENTO,
                controles_relacionados=["A.12.4", "A.18.1", "A.18.2"],
                requisitos_normativos=["ISO27001 A.12", "SOX", "Basilea III"],
                preguntas_evaluacion=[
                    "¿Todas las operaciones tienen ID de auditoría?",
                    "¿Los logs son inmutables?",
                    "¿Se retain datos por período requerido?",
                ],
                evidencia_requerida=[
                    "Logs de auditoría",
                    "Política de retención",
                    "Informes de auditoría",
                ],
                peso=1.5,
            ),
            CriterioEvaluacion(
                id="CC-006",
                nombre="Gestión de Proveedores de Confirming",
                descripcion="Evaluar y gestionar riesgos de terceros en confirming",
                tipo_operacion=TipoOperacion.CONFIRMING,
                categoria_riesgo=CategoriaRiesgo.CUMPLIMIENTO,
                controles_relacionados=["A.15.1", "A.15.2", "A.15.3"],
                requisitos_normativos=["ISO27001 A.15", "VRM"],
                preguntas_evaluacion=[
                    "¿Se evalúa seguridad de bancos corresponsales?",
                    "¿Los contratos incluyen cláusulas de seguridad?",
                    "¿Se realiza due diligence periódico?",
                ],
                evidencia_requerida=[
                    "Evaluaciones de proveedores",
                    "Contratos con cláusulas",
                    "Registro de due diligence",
                ],
                peso=1.5,
            ),
        ]


class CriteriosPagosLinea:
    @staticmethod
    def get_criterios() -> List[CriterioEvaluacion]:
        return [
            CriterioEvaluacion(
                id="CP-001",
                nombre="Cumplimiento PCI-DSS",
                descripcion="Cumplir con los requisitos del estándar de seguridad de datos de tarjetas",
                tipo_operacion=TipoOperacion.PAGOS_LINEA,
                categoria_riesgo=CategoriaRiesgo.CUMPLIMIENTO,
                controles_relacionados=["A.10.1", "A.10.2", "A.8.1", "A.9.1"],
                requisitos_normativos=["PCI-DSS 4.0", "ISO27001 A.10"],
                preguntas_evaluacion=[
                    "¿La empresa es PCI-DSS Compliant?",
                    "¿Se escanea trimestralmente con ASV?",
                    "¿Los datos de tarjeta se procesan en entorno seguro?",
                ],
                evidencia_requerida=[
                    "Certificado PCI-DSS",
                    "Informes ASV",
                    "Documentación de red",
                ],
                peso=3.0,
            ),
            CriterioEvaluacion(
                id="CP-002",
                nombre="Tokenización y Cifrado de Pagos",
                descripcion="Implementar tokenización y cifrado para transacciones",
                tipo_operacion=TipoOperacion.PAGOS_LINEA,
                categoria_riesgo=CategoriaRiesgo.CIBERSEGURIDAD,
                controles_relacionados=["A.10.1", "A.10.2", "A.10.3"],
                requisitos_normativos=["PCI-DSS 3.4", "ISO27001 A.10", "PSD2"],
                preguntas_evaluacion=[
                    "¿Se usa tokenización para datos de tarjeta?",
                    "¿El cifrado usa TLS 1.2 o superior?",
                    "¿Las claves de cifrado se gestionan adecuadamente?",
                ],
                evidencia_requerida=[
                    "Configuración de tokenización",
                    "Certificados TLS",
                    "Gestión de claves",
                ],
                peso=2.5,
            ),
            CriterioEvaluacion(
                id="CP-003",
                nombre="Autenticación Fuerte de Clientes",
                descripcion="Implementar SCA (Strong Customer Authentication)",
                tipo_operacion=TipoOperacion.PAGOS_LINEA,
                categoria_riesgo=CategoriaRiesgo.CIBERSEGURIDAD,
                controles_relacionados=["A.9.1", "A.9.4", "A.9.5"],
                requisitos_normativos=["PSD2", "SCA", "3DSecure"],
                preguntas_evaluacion=[
                    "¿Se implementa 3DSecure para transacciones?",
                    "¿La autenticación usa al menos 2 factores?",
                    "¿Existe autenticación biométrica?",
                ],
                evidencia_requerida=[
                    "Configuración 3DS",
                    "MFA implementado",
                    "Logs de autenticación",
                ],
                peso=2.5,
            ),
            CriterioEvaluacion(
                id="CP-004",
                nombre="Protección contra Fraude en Tiempo Real",
                descripcion="Detectar y prevenir fraude en tiempo real",
                tipo_operacion=TipoOperacion.PAGOS_LINEA,
                categoria_riesgo=CategoriaRiesgo.CREDITICIO,
                controles_relacionados=["A.12.2", "A.12.3", "A.13.1"],
                requisitos_normativos=["ISO27001 A.12", "AML", "PCI-DSS"],
                preguntas_evaluacion=[
                    "¿Existe sistema de detección de fraude en tiempo real?",
                    "¿Se usan reglas de scoring de riesgo?",
                    "¿Hay límites de transacción por cliente?",
                ],
                evidencia_requerida=[
                    "Sistema antifraude",
                    "Reglas de scoring",
                    "Alertas de fraude",
                ],
                peso=2.0,
            ),
            CriterioEvaluacion(
                id="CP-005",
                nombre="Seguridad de APIs de Pago",
                descripcion="Proteger APIs de integración con pasarelas de pago",
                tipo_operacion=TipoOperacion.PAGOS_LINEA,
                categoria_riesgo=CategoriaRiesgo.CIBERSEGURIDAD,
                controles_relacionados=["A.13.1", "A.13.2", "A.14.3"],
                requisitos_normativos=["ISO27001 A.13", "OWASP API", "PCI-DSS"],
                preguntas_evaluacion=[
                    "¿Las APIs usan autenticación OAuth/API Key?",
                    "¿Se implementa rate limiting?",
                    "¿Existe protección contra inyecciones?",
                ],
                evidencia_requerida=[
                    "Documentación de APIs",
                    "Configuración WAF",
                    "Tests de penetración",
                ],
                peso=2.0,
            ),
            CriterioEvaluacion(
                id="CP-006",
                nombre="Continuidad de Pagos Electrónicos",
                descripcion="Garantizar disponibilidad de sistemas de pago 24/7",
                tipo_operacion=TipoOperacion.PAGOS_LINEA,
                categoria_riesgo=CategoriaRiesgo.OPERACIONAL,
                controles_relacionados=["A.17.1", "A.17.2", "A.17.3"],
                requisitos_normativos=["ISO27001 A.17", "PCI-DSS 12.10"],
                preguntas_evaluacion=[
                    "¿El uptime es mínimo 99.9%?",
                    "¿Existe plan de contingencia de pagos?",
                    "¿Se tienen redundancias geográficas?",
                ],
                evidencia_requerida=[
                    "Informes de uptime",
                    "Plan de contingencia",
                    "Infraestructura redundante",
                ],
                peso=2.0,
            ),
            CriterioEvaluacion(
                id="CP-007",
                nombre="Gestión de Incidentes de Pago",
                descripcion="Responder efectivamente a incidentes de seguridad en pagos",
                tipo_operacion=TipoOperacion.PAGOS_LINEA,
                categoria_riesgo=CategoriaRiesgo.OPERACIONAL,
                controles_relacionados=["A.16.1", "A.16.1.1", "A.16.1.2"],
                requisitos_normativos=["ISO27001 A.16", "PCI-DSS 12.10"],
                preguntas_evaluacion=[
                    "¿Existe equipo de respuesta a incidentes?",
                    "¿Se tienen procedimientos de notificación de brechas?",
                    "¿Se notifica a usuarios afectados?",
                ],
                evidencia_requerida=[
                    "Plan de respuesta",
                    "Contactos de emergencia",
                    "Comunicados de incidentes",
                ],
                peso=1.5,
            ),
            CriterioEvaluacion(
                id="CP-008",
                nombre="Monitoreo de Transacciones",
                descripcion="Monitorear y analizar transacciones en tiempo real",
                tipo_operacion=TipoOperacion.PAGOS_LINEA,
                categoria_riesgo=CategoriaRiesgo.CIBERSEGURIDAD,
                controles_relacionados=["A.12.1", "A.12.2", "A.12.3"],
                requisitos_normativos=["ISO27001 A.12", "PCI-DSS 10"],
                preguntas_evaluacion=[
                    "¿Se registran todas las transacciones?",
                    "¿Existe monitoreo en tiempo real?",
                    "¿Se generan alertas automáticas?",
                ],
                evidencia_requerida=[
                    "SIEM configurado",
                    "Alertas configuradas",
                    "Dashboards de monitoreo",
                ],
                peso=1.5,
            ),
        ]


class GestorCriterios:
    def __init__(self):
        self.criterios: List[CriterioEvaluacion] = []
        self.criterios.extend(CriteriosFactoring.get_criterios())
        self.criterios.extend(CriteriosConfirming.get_criterios())
        self.criterios.extend(CriteriosPagosLinea.get_criterios())

    def get_criterios_por_tipo(self, tipo: TipoOperacion) -> List[CriterioEvaluacion]:
        return [c for c in self.criterios if c.tipo_operacion == tipo]

    def get_criterio(self, criterio_id: str) -> Optional[CriterioEvaluacion]:
        for c in self.criterios:
            if c.id == criterio_id:
                return c
        return None

    def get_all_criterios_json(self) -> str:
        return json.dumps(
            [c.to_dict() for c in self.criterios], indent=2, ensure_ascii=False
        )

    def get_resumen_por_tipo(self) -> Dict:
        return {
            "factoring": {
                "total": len(CriteriosFactoring.get_criterios()),
                "criterios": [c.id for c in CriteriosFactoring.get_criterios()],
            },
            "confirming": {
                "total": len(CriteriosConfirming.get_criterios()),
                "criterios": [c.id for c in CriteriosConfirming.get_criterios()],
            },
            "pagos_linea": {
                "total": len(CriteriosPagosLinea.get_criterios()),
                "criterios": [c.id for c in CriteriosPagosLinea.get_criterios()],
            },
        }
