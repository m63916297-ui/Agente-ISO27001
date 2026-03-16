"""
CLAUSULAS ISO 27001:2022
Templates con ejemplos para empresa de Factoring y Confirming
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class EstadoClausula(Enum):
    NO_IMPLEMENTADA = "no_implementada"
    EN_IMPLEMENTACION = "en_implementacion"
    IMPLEMENTADA = "implementada"
    EN_MANTENIMIENTO = "en_mantenimiento"


@dataclass
class Clausula:
    numero: str
    titulo: str
    descripcion: str
    requisitos: List[str]
    evidenciarequerida: List[str]
    aplicabilidad_factoring: bool = True
    aplicabilidad_confirming: bool = True
    estado: EstadoClausula = EstadoClausula.NO_IMPLEMENTADA
    observaciones: str = ""

    def to_dict(self) -> Dict:
        return {
            "numero": self.numero,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "requisitos": self.requisitos,
            "evidencia_requerida": self.evidenciarequerida,
            "aplicabilidad_factoring": self.aplicabilidad_factoring,
            "aplicabilidad_confirming": self.aplicabilidad_confirming,
            "estado": self.estado.value,
            "observaciones": self.observaciones,
        }


class ClausesISO27001:
    @staticmethod
    def get_all() -> List[Clausula]:
        return [
            Clausula(
                numero="4",
                titulo="Contexto de la organización",
                descripcion="La organización debe determinar cuestiones externas e internas relevantes para su SGSI",
                requisitos=[
                    "Determinar el contexto externo",
                    "Determinar el contexto interno",
                    "Determinar el alcance del SGSI",
                    "Sistema de gestión de seguridad de la información",
                ],
                evidenciarequerida=[
                    "Documento de contexto organizacional",
                    "Alcance del SGSI definido",
                    "Mapa de partes interesadas",
                ],
                aplicabilidad_factoring=True,
                aplicabilidad_confirming=True,
            ),
            Clausula(
                numero="5",
                titulo="Liderazgo",
                descripcion="La alta dirección debe demostrar liderazgo y compromiso con el SGSI",
                requisitos=[
                    "Liderazgo y compromiso",
                    "Política de seguridad de la información",
                    "Roles, responsabilidades y autoridades",
                ],
                evidenciarequerida=[
                    "Política de seguridad aprobada por dirección",
                    "Actas de dirección",
                    "Designación de CISO",
                    "Matriz de roles y responsabilidades",
                ],
                aplicabilidad_factoring=True,
                aplicabilidad_confirming=True,
            ),
            Clausula(
                numero="6",
                titulo="Planificación",
                descripcion="La organización debe planificar acciones para abordar riesgos",
                requisitos=[
                    "Acciones para abordar riesgos y oportunidades",
                    "Evaluación de riesgos de seguridad de la información",
                    "Tratamiento de riesgos de seguridad de la información",
                ],
                evidenciarequerida=[
                    "Evaluación de riesgos documentada",
                    "Plan de tratamiento de riesgos",
                    "Matriz de riesgos actualizada",
                ],
                aplicabilidad_factoring=True,
                aplicabilidad_confirming=True,
            ),
            Clausula(
                numero="7",
                titulo="Soporte",
                descripcion="La organización debe proporcionar recursos y competencia necesaria",
                requisitos=[
                    "Recursos",
                    "Competencia",
                    "Concienciación",
                    "Comunicación",
                    "Información documentada",
                ],
                evidenciarequerida=[
                    "Presupuesto de seguridad aprobado",
                    "Registros de capacitación",
                    "Programa de concienciación",
                    "Plan de comunicaciones",
                ],
                aplicabilidad_factoring=True,
                aplicabilidad_confirming=True,
            ),
            Clausula(
                numero="8",
                titulo="Operación",
                descripcion="La organización debe planificar, implementar y controlar procesos",
                requisitos=[
                    "Planificación operativa",
                    "Evaluación de riesgos de seguridad de la información",
                    "Tratamiento de riesgos de seguridad de la información",
                ],
                evidenciarequerida=[
                    "Procedimientos operativos",
                    "Registros de ejecución",
                    "Informes de seguimiento",
                ],
                aplicabilidad_factoring=True,
                aplicabilidad_confirming=True,
            ),
            Clausula(
                numero="9",
                titulo="Evaluación del desempeño",
                descripcion="La organización debe monitorear, medir y analizar el SGSI",
                requisitos=[
                    "Seguimiento, medición, análisis y evaluación",
                    "Auditoría interna",
                    "Revisión por la dirección",
                ],
                evidenciarequerida=[
                    "Indicadores de desempeño (KPIs)",
                    "Informes de auditoría interna",
                    "Actas de revisión por dirección",
                ],
                aplicabilidad_factoring=True,
                aplicabilidad_confirming=True,
            ),
            Clausula(
                numero="10",
                titulo="Mejora",
                descripcion="La organización debe tratar no conformidades y tomar acciones",
                requisitos=["No conformidad y acción correctiva", "Mejora continua"],
                evidenciarequerida=[
                    "Registro de no conformidades",
                    "Acciones correctivas documentadas",
                    "Mejoras implementadas",
                ],
                aplicabilidad_factoring=True,
                aplicabilidad_confirming=True,
            ),
        ]

    @staticmethod
    def get_template_json() -> str:
        import json

        clauses = ClausesISO27001.get_all()
        return json.dumps([c.to_dict() for c in clauses], indent=2, ensure_ascii=False)
