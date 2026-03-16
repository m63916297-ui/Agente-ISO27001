"""
SECCIONES ISO 27001:2022
Templates con ejemplos para empresa de Factoring y Confirming
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class TipoSeccion(Enum):
    CLAUSULAS = "clausulas"
    CONTROLES = "controles"
    ANEXO = "anexo"
    IMPLEMENTACION = "implementacion"


@dataclass
class Seccion:
    numero: str
    titulo: str
    descripcion: str
    importancia: str
    aplicabilidad_factoring: str
    aplicabilidad_confirming: str
    requisitos_clave: List[str]
    entregables: List[str]
    ejemplo_practico: str
    tiempo_estimado: str
    responsable: str
    dependencias: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "numero": self.numero,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "importancia": self.importancia,
            "aplicabilidad_factoring": self.aplicabilidad_factoring,
            "aplicabilidad_confirming": self.aplicabilidad_confirming,
            "requisitos_clave": self.requisitos_clave,
            "entregables": self.entregables,
            "ejemplo_practico": self.ejemplo_practico,
            "tiempo_estimado": self.tiempo_estimado,
            "responsable": self.responsable,
            "dependencias": self.dependencias,
        }


class SeccionesISO27001:
    @staticmethod
    def get_all() -> List[Seccion]:
        return [
            # SECCION 1: CONTEXTO ORGANIZACIONAL
            Seccion(
                numero="1",
                titulo="Contexto de la Organización",
                descripcion="Establecer el contexto interno y externo de la organizacion para el SGSI",
                importancia="Fundamental para determinar el alcance y requisitos del SGSI",
                aplicabilidad_factoring="Alta - Requiere definir procesos de factoring",
                aplicabilidad_confirming="Alta - Requiere definir procesos de confirming",
                requisitos_clave=[
                    "Determinar contexto externo (regulatorio, mercado)",
                    "Determinar contexto interno (estructura, recursos)",
                    "Definir alcance del SGSI",
                    "Identificar partes interesadas",
                ],
                entregables=[
                    "Documento de contexto organizacional",
                    "Alcance del SGSI",
                    "Mapa de partes interesadas",
                    "Analisis FODA",
                ],
                ejemplo_practico="Una empresa de factoring debe documentar que opera bajo regulacion financiera y que maneja datos sensibles de clientes y deudores",
                tiempo_estimado="2-4 semanas",
                responsable="Equipo SGSI / Consultor",
                dependencias=[],
            ),
            # SECCION 2: LIDERAZGO
            Seccion(
                numero="2",
                titulo="Liderazgo",
                descripcion="Demostrar liderazgo y compromiso de la alta direccion con el SGSI",
                importancia="El compromiso de la direccion es critico para el exito del SGSI",
                aplicabilidad_factoring="Critica - Requiere sponsorizacion ejecutiva",
                aplicabilidad_confirming="Critica - Requiere recursos dedicados",
                requisitos_clave=[
                    "Establecer politica de seguridad",
                    "Asignar roles y responsabilidades",
                    "Asegurar integracion del SGSI en procesos",
                    "Proveer recursos necesarios",
                ],
                entregables=[
                    "Politica de seguridad de la informacion",
                    "Organigrama de seguridad",
                    "Actas de direccion",
                    "Designacion de CISO",
                ],
                ejemplo_practico="ElCEO y elComite de Direccion deben aprobar la politica de seguridad y asignar presupuesto para implementar controles",
                tiempo_estimado="1-2 semanas",
                responsable="Alta Direccion / CISO",
                dependencias=["Seccion 1"],
            ),
            # SECCION 3: PLANIFICACION
            Seccion(
                numero="3",
                titulo="Planificacion",
                descripcion="Planificar acciones para abordar riesgos y oportunidades",
                importancia="Establece el enfoque de gestion de riesgos",
                aplicabilidad_factoring="Alta - Riesgos financieros especificos",
                aplicabilidad_confirming="Alta - Riesgos de pagos a proveedores",
                requisitos_clave=[
                    "Identificar riesgos de seguridad",
                    "Evaluar y analizar riesgos",
                    "Determinar tratamiento de riesgos",
                    "Planificar acciones de tratamiento",
                ],
                entregables=[
                    "Evaluacion de riesgos",
                    "Matriz de riesgos",
                    "Plan de tratamiento de riesgos",
                    "Declaracion de aplicabilidad",
                ],
                ejemplo_practico="Identificar riesgos como robo de credenciales, fraude en cesion de facturas, compromiso de datos de clientes, y definir controles para mitigarlos",
                tiempo_estimado="4-8 semanas",
                responsable="CISO / Risk Manager",
                dependencias=["Seccion 1", "Seccion 2"],
            ),
            # SECCION 4: APOYO
            Seccion(
                numero="4",
                titulo="Apoyo",
                descripcion="Proporcionar recursos, competencia, conciencia y comunicacion",
                importancia="Asegura que la organizacion tenga los recursos necesarios",
                aplicabilidad_factoring="Alta - Requiere personal capacitado",
                aplicabilidad_confirming="Alta - Requiere especializacion",
                requisitos_clave=[
                    "Determinar y proporcionar recursos",
                    "Asegurar competencia del personal",
                    "Generar conciencia",
                    "Establecer comunicacion",
                ],
                entregables=[
                    "Presupuesto de seguridad",
                    "Plan de capacitacion",
                    "Programa de concienciacion",
                    "Plan de comunicaciones",
                ],
                ejemplo_practico="Capacitar a analistas de factoring en manejo de datos sensibles y en politicas de confidencialidad",
                tiempo_estimado="2-4 semanas",
                responsable="RRHH / CISO",
                dependencias=["Seccion 2"],
            ),
            # SECCION 5: OPERACION
            Seccion(
                numero="5",
                titulo="Operacion",
                descripcion="Planificar, implementar y controlar procesos del SGSI",
                importancia="Traduce la planificacion en accion",
                aplicabilidad_factoring="Critica - Procesos diarios de factoring",
                aplicabilidad_confirming="Critica - Procesamiento de pagos",
                requisitos_clave=[
                    "Planificar procesos",
                    "Implementar controles",
                    "Gestionar cambios",
                    "Evaluar riesgos operacionalmente",
                ],
                entregables=[
                    "Procedimientos operativos",
                    "Registros de operacion",
                    "Informes de seguimiento",
                    "Gestion de cambios",
                ],
                ejemplo_practico="Establecer procedimientos para procesamiento de facturas cedidas, validacion de deudores, yGestion de cartera",
                tiempo_estimado="8-12 semanas",
                responsable="Operaciones / IT",
                dependencias=["Seccion 3", "Seccion 4"],
            ),
            # SECCION 6: EVALUACION DEL DESEMPEÑO
            Seccion(
                numero="6",
                titulo="Evaluación del Desempeño",
                descripcion="Monitorear, medir, analizar y evaluar el SGSI",
                importancia="Permite verificar efectividad del SGSI",
                aplicabilidad_factoring="Alta - Monitoreo de operaciones",
                aplicabilidad_confirming="Alta - Auditoria de pagos",
                requisitos_clave=[
                    "Monitorear y medir",
                    "Realizar auditorias internas",
                    "Efectuar revision por la direccion",
                    "Analizar y evaluar",
                ],
                entregables=[
                    "KPIs de seguridad",
                    "Informes de auditoria interna",
                    "Actas de revision por direccion",
                    "Dashboard de seguridad",
                ],
                ejemplo_practico="Medir tiempo de respuesta a incidentes, porcentaje de empleados capacitados, y cumplimiento de politicas",
                tiempo_estimado="2-4 semanas",
                responsable="CISO / Auditor Interno",
                dependencias=["Seccion 5"],
            ),
            # SECCION 7: MEJORA
            Seccion(
                numero="7",
                titulo="Mejora",
                descripcion="Tratar no conformidades y tomar acciones correctivas",
                importancia="Asegura mejora continua del SGSI",
                aplicabilidad_factoring="Continua - Mejora de procesos",
                aplicabilidad_confirming="Continua - Optimizacion de pagos",
                requisitos_clave=[
                    "Identificar no conformidades",
                    "Tomar acciones correctivas",
                    "Implementar mejoras",
                    "Documentar lecciones aprendidas",
                ],
                entregables=[
                    "Registro de no conformidades",
                    "Acciones correctivas",
                    "Mejoras implementadas",
                    "Informe de lecciones aprendidas",
                ],
                ejemplo_practico="Tras un incidente de seguridad, implementar acciones correctivas y actualizar procedimientos",
                tiempo_estimado="Continua",
                responsable="CISO / Mejora Continua",
                dependencias=["Seccion 6"],
            ),
            # ANEXO A: CONTROLES
            Seccion(
                numero="A",
                titulo="Controles del Anexo A",
                descripcion="Conjunto de 93 controles de seguridad organizados en 4 secciones",
                importancia="Proporciona controles especificos para implementar",
                aplicabilidad_factoring="Completa - Todos los controles aplicables",
                aplicabilidad_confirming="Completa - Controles de pagos",
                requisitos_clave=[
                    "A.5 Controles organizacionales (5)",
                    "A.6 Controles de personas (2)",
                    "A.7 Controles fisicos (2)",
                    "A.8 Controles tecnológicos (34)",
                    "A.9 Controles de acceso (9)",
                    "A.10 Criptografia (2)",
                    "A.11 Operaciones (14)",
                    "A.12 Comunicaciones (10)",
                    "A.13 Adquisicion (7)",
                    "A.14 Proveedores (5)",
                    "A.15 Incidentes (9)",
                    "A.16 Continuidad (4)",
                    "A.17 Cumplimiento (2)",
                ],
                entregables=[
                    "Inventario de controles implementados",
                    "Evidencias de cumplimiento",
                    "Declaracion de aplicabilidad (SoA)",
                    "Mapa de controles",
                ],
                ejemplo_practico="Implementar controles de acceso con MFA, cifrado de datos con AES-256, y gestion de incidentes con equipo CSIRT",
                tiempo_estimado="6-12 meses",
                responsable="CISO / Equipo SGSI",
                dependencias=["Seccion 3"],
            ),
        ]

    @staticmethod
    def get_template_json() -> str:
        import json

        sections = SeccionesISO27001.get_all()
        return json.dumps([s.to_dict() for s in sections], indent=2, ensure_ascii=False)

    @staticmethod
    def get_resumen_ejecutivo() -> Dict:
        return {
            "total_secciones": 8,
            "total_controles_anexo_a": 93,
            "tiempo_estimado_total": "12-18 meses",
            "fases": [
                {
                    "fase": 1,
                    "nombre": "Inicio y Análisis",
                    "semanas": "1-8",
                    "secciones": ["1", "2", "3"],
                },
                {
                    "fase": 2,
                    "nombre": "Diseño",
                    "semanas": "9-16",
                    "secciones": ["4", "A"],
                },
                {
                    "fase": 3,
                    "nombre": "Implementación",
                    "semanas": "17-40",
                    "secciones": ["5", "A"],
                },
                {
                    "fase": 4,
                    "nombre": "Operación y Mejora",
                    "semanas": "41-52+",
                    "secciones": ["6", "7"],
                },
            ],
        }
