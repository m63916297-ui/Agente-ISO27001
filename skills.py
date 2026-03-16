"""
SKILLS - Habilidades y Capacidades de los Agentes ISO 27001
===========================================================
Este archivo define las habilidades, competencias y capacidades
de cada agente del sistema multiagente.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class CategoriaSkill(Enum):
    AUDITORIA = "auditoria"
    RIESGO = "riesgo"
    CUMPLIMIENTO = "cumplimiento"
    TECNICO = "tecnico"
    PROCESO = "proceso"
    NEGOCIO = "negocio"
    COMUNICACION = "comunicacion"


@dataclass
class Skill:
    id: str
    nombre: str
    descripcion: str
    categoria: CategoriaSkill
    nivel: int
    herramientas: List[str] = field(default_factory=list)
    certificaciones: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "categoria": self.categoria.value,
            "nivel": self.nivel,
            "herramientas": self.herramientas,
            "certificaciones": self.certificaciones,
        }


@dataclass
class AgenteSkills:
    nombre_agente: str
    rol: str
    skills: List[Skill]
    competencias_clave: List[str]
    limitantes: List[str]

    def to_dict(self) -> Dict:
        return {
            "nombre_agente": self.nombre_agente,
            "rol": self.rol,
            "skills": [s.to_dict() for s in self.skills],
            "competencias_clave": self.competencias_clave,
            "limitantes": self.limitantes,
        }


class SkillsAgentes:
    @staticmethod
    def get_agente_auditor() -> AgenteSkills:
        skills = [
            Skill(
                id="AUD-001",
                nombre="Planificación de Auditorías",
                descripcion="Capacidad para planificar y organizar auditorías internas ISO 27001",
                categoria=CategoriaSkill.AUDITORIA,
                nivel=5,
                herramientas=["ISO 27001", "ISO 19011", "Plan de Auditoría"],
                certificaciones=["CISA", "ISO 27001 LA"],
            ),
            Skill(
                id="AUD-002",
                nombre="Ejecución de Auditorías",
                descripcion="Realización de auditorías in-situ y remotas",
                categoria=CategoriaSkill.AUDITORIA,
                nivel=5,
                herramientas=["Checklists", "Entrevistas", "Evidencias"],
                certificaciones=["CISA"],
            ),
            Skill(
                id="AUD-003",
                nombre="Análisis de Hallazgos",
                descripcion="Identificación y clasificación de no conformidades",
                categoria=CategoriaSkill.AUDITORIA,
                nivel=4,
                herramientas=["Matriz de hallazgos", "Informes"],
                certificaciones=[],
            ),
            Skill(
                id="AUD-004",
                nombre="Comunicación de Resultados",
                descripcion="Elaboración de informes de auditoría",
                categoria=CategoriaSkill.COMUNICACION,
                nivel=4,
                herramientas=["Informes", "Presentaciones"],
                certificaciones=[],
            ),
        ]

        return AgenteSkills(
            nombre_agente="Agente Auditor",
            rol="Planificar y ejecutar auditorías internas de cumplimiento ISO 27001",
            skills=skills,
            competencias_clave=[
                "Conocimiento profundo de ISO 27001:2022",
                "Técnicas de auditoría",
                "Análisis de riesgos",
                "Elaboración de informes",
            ],
            limitantes=[
                "No puede tomar decisiones ejecutivas",
                "Requiere evidencia documentada",
            ],
        )

    @staticmethod
    def get_agente_riesgo() -> AgenteSkills:
        skills = [
            Skill(
                id="RSG-001",
                nombre="Identificación de Riesgos",
                descripcion="Identificar amenazas y vulnerabilidades en el SGSI",
                categoria=CategoriaSkill.RIESGO,
                nivel=5,
                herramientas=["Mapa de riesgos", "Análisis FODA", "Threat Modeling"],
                certificaciones=["CRISC", "CISM"],
            ),
            Skill(
                id="RSG-002",
                nombre="Evaluación de Riesgos",
                descripcion="Calcular impacto y probabilidad de riesgos",
                categoria=CategoriaSkill.RIESGO,
                nivel=5,
                herramientas=["Matriz de riesgo", "ISO 31000", "NIST"],
                certificaciones=["CRISC"],
            ),
            Skill(
                id="RSG-003",
                nombre="Tratamiento de Riesgos",
                descripcion="Desarrollar planes de tratamiento de riesgos",
                categoria=CategoriaSkill.RIESGO,
                nivel=4,
                herramientas=["Plan de tratamiento", "Apetito de riesgo"],
                certificaciones=[],
            ),
            Skill(
                id="RSG-004",
                nombre="Análisis de Riesgos Financieros",
                descripcion="Evaluar riesgos específicos de operaciones financieras",
                categoria=CategoriaSkill.NEGOCIO,
                nivel=4,
                herramientas=["Basilea III", "PCI-DSS", "Modelos de riesgo"],
                certificaciones=["CFR"],
            ),
        ]

        return AgenteSkills(
            nombre_agente="Agente de Riesgos",
            rol="Identificar, evaluar y gestionar riesgos de seguridad de la información",
            skills=skills,
            competencias_clave=[
                "Metodologías de análisis de riesgos",
                "Conocimiento del negocio financiero",
                "Normativas de seguridad",
                "Modelado de amenazas",
            ],
            limitantes=[
                "Requiere datos actualizados del negocio",
                "Las evaluaciones son recomendaciones",
            ],
        )

    @staticmethod
    def get_agente_cumplimiento() -> AgenteSkills:
        skills = [
            Skill(
                id="CMP-001",
                nombre="Verificación de Cumplimiento",
                descripcion="Verificar conformidad con ISO 27001 y otras normativas",
                categoria=CategoriaSkill.CUMPLIMIENTO,
                nivel=5,
                herramientas=["ISO 27001", "PCI-DSS", "GDPR"],
                certificaciones=["ISO 27001 LA", "CIPP"],
            ),
            Skill(
                id="CMP-002",
                nombre="Análisis Gap",
                descripcion="Identificar brechas entre estado actual y requerido",
                categoria=CategoriaSkill.CUMPLIMIENTO,
                nivel=5,
                herramientas=["Matriz GAP", "Roadmaps"],
                certificaciones=[],
            ),
            Skill(
                id="CMP-003",
                nombre="Gestión de Evidencias",
                descripcion="Recopilar y organizar evidencias de cumplimiento",
                categoria=CategoriaSkill.CUMPLIMIENTO,
                nivel=4,
                herramientas=["GRC", "SharePoint"],
                certificaciones=[],
            ),
            Skill(
                id="CMP-004",
                nombre="Cumplimiento PCI-DSS",
                descripcion="Verificar cumplimiento con estándar de tarjetas de pago",
                categoria=CategoriaSkill.CUMPLIMIENTO,
                nivel=4,
                herramientas=["PCI-DSS", "SAQ", "ROC"],
                certificaciones=["PCIP", "QSA"],
            ),
        ]

        return AgenteSkills(
            nombre_agente="Agente de Cumplimiento",
            rol="Verificar cumplimiento normativo y gestionar evidencias",
            skills=skills,
            competencias_clave=[
                "Conocimiento de normativas",
                "Gestión de evidencias",
                "Análisis de controles",
                "Preparacion para auditorías",
            ],
            limitantes=[
                "No替代 decisiones de negocio",
                "Limitado a verificación documental",
            ],
        )

    @staticmethod
    def get_agente_incidentes() -> AgenteSkills:
        skills = [
            Skill(
                id="INC-001",
                nombre="Detección de Incidentes",
                descripcion="Identificar y detectar incidentes de seguridad",
                categoria=CategoriaSkill.TECNICO,
                nivel=5,
                herramientas=["SIEM", "EDR", "IDS/IPS"],
                certificaciones=["GCFA", "GCIH"],
            ),
            Skill(
                id="INC-002",
                nombre="Clasificación de Incidentes",
                descripcion="Categorizar y priorizar incidentes",
                categoria=CategoriaSkill.TECNICO,
                nivel=4,
                herramientas=["Taxonomía MITRE", "Matrices de severidad"],
                certificaciones=[],
            ),
            Skill(
                id="INC-003",
                nombre="Respuesta a Incidentes",
                descripcion="Coordinar respuesta y contención",
                categoria=CategoriaSkill.TECNICO,
                nivel=5,
                herramientas=["Playbooks", "CSIRT", "SOAR"],
                certificaciones=["GCIH", "GCFA"],
            ),
            Skill(
                id="INC-004",
                nombre="Análisis Forense",
                descripcion="Investigar y preservar evidencias digitales",
                categoria=CategoriaSkill.TECNICO,
                nivel=4,
                herramientas=["FTK", "EnCase", "Wireshark"],
                certificaciones=["GCFE"],
            ),
        ]

        return AgenteSkills(
            nombre_agente="Agente de Incidentes",
            rol="Detectar, clasificar y coordinar respuesta a incidentes de seguridad",
            skills=skills,
            competencias_clave=[
                "Gestión de incidentes CSIRT",
                "Análisis forense",
                "Coordinación con equipos",
                "Comunicación de crisis",
            ],
            limitantes=[
                "Requiere herramientas especializadas",
                "Limitado a incidentes de seguridad",
            ],
        )

    @staticmethod
    def get_agente_mejora() -> AgenteSkills:
        skills = [
            Skill(
                id="MJR-001",
                nombre="Análisis de Mejoras",
                descripcion="Identificar oportunidades de mejora en el SGSI",
                categoria=CategoriaSkill.PROCESO,
                nivel=4,
                herramientas=["PDCA", "Kaizen", "Mejora continua"],
                certificaciones=["Lean IT"],
            ),
            Skill(
                id="MJR-002",
                nombre="Diseño de Procesos",
                descripcion="Diseñar y optimizar procesos de seguridad",
                categoria=CategoriaSkill.PROCESO,
                nivel=4,
                herramientas=["BPMN", "SIPOC", "Value Stream"],
                certificaciones=[],
            ),
            Skill(
                id="MJR-003",
                nombre="Gestión de Cambios",
                descripcion="Gestionar cambios en procesos y sistemas",
                categoria=CategoriaSkill.PROCESO,
                nivel=3,
                herramientas=["ITIL", "Mermaid", "Diagramas"],
                certificaciones=["ITIL"],
            ),
            Skill(
                id="MJR-004",
                nombre="Métricas de Eficacia",
                descripcion="Medir efectividad de las mejoras",
                categoria=CategoriaSkill.PROCESO,
                nivel=4,
                herramientas=["KPIs", "Dashboards", "Informes"],
                certificaciones=[],
            ),
        ]

        return AgenteSkills(
            nombre_agente="Agente de Mejora Continua",
            rol="Identificar, proponer e implementar mejoras en el SGSI",
            skills=skills,
            competencias_clave=[
                "Metodologías de mejora",
                "Diseño de procesos",
                "Análisis de métricas",
                "Gestión del cambio",
            ],
            limitantes=[
                "Requiere aprobación para implementación",
                "Limitado a procesos de seguridad",
            ],
        )

    @staticmethod
    def get_agente_capacitacion() -> AgenteSkills:
        skills = [
            Skill(
                id="CAP-001",
                nombre="Diseño de Programas",
                descripcion="Desarrollar programas de formación en seguridad",
                categoria=CategoriaSkill.COMUNICACION,
                nivel=4,
                herramientas=["ADDIE", "Bloom", "LMS"],
                certificaciones=["CSE", "CST"],
            ),
            Skill(
                id="CAP-002",
                nombre="Concienciación",
                descripcion="Programas de concienciación para empleados",
                categoria=CategoriaSkill.COMUNICACION,
                nivel=4,
                herramientas=["Phishing simulation", "Campañas", "Games"],
                certificaciones=[],
            ),
            Skill(
                id="CAP-003",
                nombre="Capacitación Técnica",
                descripcion="Formar en competencias técnicas de seguridad",
                categoria=CategoriaSkill.TECNICO,
                nivel=4,
                herramientas=["Labs", "CTFs", "Certificaciones"],
                certificaciones=["CompTIA", "EC-Council"],
            ),
            Skill(
                id="CAP-004",
                nombre="Evaluación de Efectividad",
                descripcion="Medir impacto de las capacitaciones",
                categoria=CategoriaSkill.COMUNICACION,
                nivel=3,
                herramientas=["Encuestas", "Tests", "KPIs"],
                certificaciones=[],
            ),
        ]

        return AgenteSkills(
            nombre_agente="Agente de Capacitación",
            rol="Gestionar programas de formación y concienciación en seguridad",
            skills=skills,
            competencias_clave=[
                "Diseño instruccional",
                "Concienciación",
                "Gestión del conocimiento",
                "Evaluación de efectividad",
            ],
            limitantes=[
                "Dependiente de recursos de formación",
                "No puede certificar usuarios",
            ],
        )

    @staticmethod
    def get_agente_proveedores() -> AgenteSkills:
        skills = [
            Skill(
                id="PRV-001",
                nombre="Evaluación de Proveedores",
                descripcion="Evaluar postura de seguridad de terceros",
                categoria=CategoriaSkill.CUMPLIMIENTO,
                nivel=4,
                herramientas=["Cuestionarios", "SIG", "Due Diligence"],
                certificaciones=["ISO 27001 LA"],
            ),
            Skill(
                id="PRV-002",
                nombre="Gestión de Contratos",
                descripcion="Verificar cláusulas de seguridad en contratos",
                categoria=CategoriaSkill.NEGOCIO,
                nivel=3,
                herramientas=["Contratos", "SLAs", "NDA"],
                certificaciones=["CCSP"],
            ),
            Skill(
                id="PRV-003",
                nombre="Monitoreo Continuo",
                descripcion="Supervisar desempeño de proveedores",
                categoria=CategoriaSkill.CUMPLIMIENTO,
                nivel=4,
                herramientas=["VRM", "Ratings", "Alertas"],
                certificaciones=[],
            ),
            Skill(
                id="PRV-004",
                nombre="Riesgo de Cadena de Suministro",
                descripcion="Evaluar riesgos en la cadena de suministro",
                categoria=CategoriaSkill.RIESGO,
                nivel=4,
                herramientas=["Mapa de cadena", "Análisis de impacto"],
                certificaciones=["CISM"],
            ),
        ]

        return AgenteSkills(
            nombre_agente="Agente de Proveedores",
            rol="Evaluar y gestionar riesgos de seguridad de terceros",
            skills=skills,
            competencias_clave=[
                "Evaluación de terceros",
                "Gestión contractual",
                "Análisis de riesgos",
                "Monitoreo continuo",
            ],
            limitantes=[
                "Dependiente de información del proveedor",
                "No puede modificar contratos",
            ],
        )

    @staticmethod
    def get_agente_politicas() -> AgenteSkills:
        skills = [
            Skill(
                id="POL-001",
                nombre="Desarrollo de Políticas",
                descripcion="Crear y mantener políticas de seguridad",
                categoria=CategoriaSkill.PROCESO,
                nivel=5,
                herramientas=["ISO 27001", "NIST", "COBIT"],
                certificaciones=["CISM", "ISO 27001 LA"],
            ),
            Skill(
                id="POL-002",
                nombre="Revisión y Actualización",
                descripcion="Mantener políticas actualizadas y relevantes",
                categoria=CategoriaSkill.PROCESO,
                nivel=4,
                herramientas=["Versionado", "Reviews", "Aprobaciones"],
                certificaciones=[],
            ),
            Skill(
                id="POL-003",
                nombre="Comunicación de Políticas",
                descripcion="Difundir políticas a la organización",
                categoria=CategoriaSkill.COMUNICACION,
                nivel=4,
                herramientas=["Intranet", "Email", "Capacitación"],
                certificaciones=[],
            ),
            Skill(
                id="POL-004",
                nombre="Análisis de Cumplimiento",
                descripcion="Verificar adherencia a políticas",
                categoria=CategoriaSkill.CUMPLIMIENTO,
                nivel=4,
                herramientas=["Auditorías", "Métricas", "Informes"],
                certificaciones=[],
            ),
        ]

        return AgenteSkills(
            nombre_agente="Agente de Políticas",
            rol="Administrar y mantener políticas de seguridad de la información",
            skills=skills,
            competencias_clave=[
                "Desarrollo de políticas",
                "Normativas ISO/NIST",
                "Comunicación organizacional",
                "Gestión documental",
            ],
            limitantes=[
                "Requiere aprobación de dirección",
                "No puede crear excepciones",
            ],
        )

    @staticmethod
    def get_all_skills() -> Dict:
        return {
            "auditor": SkillsAgentes.get_agente_auditor().to_dict(),
            "riesgo": SkillsAgentes.get_agente_riesgo().to_dict(),
            "cumplimiento": SkillsAgentes.get_agente_cumplimiento().to_dict(),
            "incidentes": SkillsAgentes.get_agente_incidentes().to_dict(),
            "mejora": SkillsAgentes.get_agente_mejora().to_dict(),
            "capacitacion": SkillsAgentes.get_agente_capacitacion().to_dict(),
            "proveedores": SkillsAgentes.get_agente_proveedores().to_dict(),
            "politicas": SkillsAgentes.get_agente_politicas().to_dict(),
        }


def get_skills_agente(nombre_agente: str) -> Optional[AgenteSkills]:
    """Obtiene los skills de un agente específico"""
    agentes = {
        "auditor": SkillsAgentes.get_agente_auditor,
        "riesgo": SkillsAgentes.get_agente_riesgo,
        "cumplimiento": SkillsAgentes.get_agente_cumplimiento,
        "incidentes": SkillsAgentes.get_agente_incidentes,
        "mejora": SkillsAgentes.get_agente_mejora,
        "capacitacion": SkillsAgentes.get_agente_capacitacion,
        "proveedores": SkillsAgentes.get_agente_proveedores,
        "politicas": SkillsAgentes.get_agente_politicas,
    }

    func = agentes.get(nombre_agente.lower())
    return func() if func else None
