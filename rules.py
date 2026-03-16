"""
RULES - Reglas del Sistema Multiagente ISO 27001
=================================================
Este archivo define las reglas fundamentales que rigen el comportamiento
de todos los agentes en el sistema de gestión de certificación ISO 27001.
"""

REGLAS_SISTEMA = {
    "version": "1.0.0",
    "actualizacion": "2026-03-16",
    "reglas": [
        {
            "id": "R001",
            "categoria": "Gobierno",
            "nombre": "Autoridad del SGSI",
            "descripcion": "El CISO debe tener autoridad suficiente para implementar y mantener el SGSI",
            "aplicabilidad": "todas"
        },
        {
            "id": "R002",
            "categoria": "Gobierno",
            "nombre": "Compromiso de la Dirección",
            "descripcion": "La dirección debe demostrar compromiso visible con la seguridad",
            "aplicabilidad": "todas"
        },
        {
            "id": "R003",
            "categoria": "Planificacion",
            "nombre": "Evaluación de Riesgos Obligatoria",
            "descripcion": "Debe realizarse evaluación de riesgos al menos anualmente",
            "aplicabilidad": "todas"
        },
        {
            "id": "R004",
            "categoria": "Planificacion",
            "nombre": "Tratamiento de Riesgos",
            "descripcion": "Todos los riesgos identificados deben tener un plan de tratamiento documentado",
            "aplicabilidad": "todas"
        },
        {
            "id": "R005",
            "categoria": "Soporte",
            "nombre": "Competencia del Personal",
            "descripcion": "Todo el personal debe recibir capacitación en seguridad de la información",
            "aplicabilidad": "todas"
        },
        {
            "id": "R006",
            "categoria": "Soporte",
            "nombre": "Concienciación Continua",
            "descripcion": "Programa de concienciación debe ser continuo y medible",
            "aplicabilidad": "todas"
        },
        {
            "id": "R007",
            "categoria": "Operacion",
            "nombre": "Gestión de Incidentes",
            "descripcion": "Debe existir proceso documentado de gestión de incidentes",
            "aplicabilidad": "todas"
        },
        {
            "id": "R008",
            "categoria": "Operacion",
            "nombre": "Seguridad de Operaciones",
            "descripcion": "Los procedimientos operativos deben estar documentados y actualizados",
            "aplicabilidad": "todas"
        },
        {
            "id": "R009",
            "categoria": "Operacion",
            "nombre": "Protección contra Malware",
            "descripcion": "Debe implementarse protección contra malware en todos los endpoints",
            "aplicabilidad": "todas"
        },
        {
            "id": "R010",
            "categoria": "Operacion",
            "nombre": "Gestión de Vulnerabilidades",
            "descripcion": "Las vulnerabilidades deben ser gestionadas según criticidad",
            "aplicabilidad": "todas"
        },
        {
            "id": "R011",
            "categoria": "Acceso",
            "nombre": "Control de Acceso Basado en Roles",
            "descripcion": "El acceso debe basarse en roles y principio de menor privilegio",
            "aplicabilidad": "todas"
        },
        {
            "id": "R012",
            "categoria": "Acceso",
            "nombre": "Autenticación Fuerte",
            "descripcion": "MFA obligatorio para acceso a sistemas críticos",
            "aplicabilidad": "factoring", "confirming", "pagos_linea"
        },
        {
            "id": "R013",
            "categoria": "Acceso",
            "nombre": "Revisión de Accesos",
            "descripcion": "Revisión trimestral de accesos a sistemas críticos",
            "aplicabilidad": "todas"
        },
        {
            "id": "R014",
            "categoria": "Criptografia",
            "nombre": "Cifrado de Datos en Reposo",
            "descripcion": "Datos sensibles deben estar cifrados en reposo con AES-256",
            "aplicabilidad": "todas"
        },
        {
            "id": "R015",
            "categoria": "Criptografia",
            "nombre": "Cifrado de Datos en Tránsito",
            "descripcion": "TLS 1.2 mínimo para todas las comunicaciones",
            "aplicabilidad": "todas"
        },
        {
            "id": "R016",
            "categoria": "Criptografia",
            "nombre": "Gestión de Claves",
            "descripcion": "Las claves criptográficas deben rotarse anualmente mínimo",
            "aplicabilidad": "pagos_linea"
        },
        {
            "id": "R017",
            "categoria": "Fisico",
            "nombre": "Seguridad Física",
            "descripcion": "Controles de acceso físico a centros de datos y áreas sensibles",
            "aplicabilidad": "todas"
        },
        {
            "id": "R018",
            "categoria": "Proveedores",
            "nombre": "Gestión de Proveedores",
            "descripcion": "Proveedores críticos deben ser evaluados anualmente",
            "aplicabilidad": "todas"
        },
        {
            "id": "R019",
            "categoria": "Proveedores",
            "nombre": "Acuerdos de Confidencialidad",
            "descripcion": "NDA obligatorio con todos los proveedores que manejen información sensible",
            "aplicabilidad": "todas"
        },
        {
            "id": "R020",
            "categoria": "Continuidad",
            "nombre": "Plan de Continuidad",
            "descripcion": "BCP documentado y probado anualmente",
            "aplicabilidad": "todas"
        },
        {
            "id": "R021",
            "categoria": "Continuidad",
            "nombre": "Respaldo y Recuperación",
            "descripcion": "Backups diarios con prueba de restauración mensual",
            "aplicabilidad": "todas"
        },
        {
            "id": "R022",
            "categoria": "Continuidad",
            "nombre": "Alta Disponibilidad",
            "descripcion": "Sistemas críticos con 99.9% de disponibilidad",
            "aplicabilidad": "pagos_linea"
        },
        {
            "id": "R023",
            "categoria": "Cumplimiento",
            "nombre": "Auditoría Interna",
            "descripcion": "Auditoría interna al menos anualmente",
            "aplicabilidad": "todas"
        },
        {
            "id": "R024",
            "categoria": "Cumplimiento",
            "nombre": "Revisión por la Dirección",
            "descripcion": "Revisión formal del SGSI trimestral",
            "aplicabilidad": "todas"
        },
        {
            "id": "R025",
            "categoria": "Cumplimiento",
            "nombre": "Gestión de No Conformidades",
            "descripcion": "Proceso documentado para gestionar no conformidades",
            "aplicabilidad": "todas"
        },
        {
            "id": "R026",
            "categoria": "Financiero",
            "nombre": "Protección de Datos Financieros",
            "descripcion": "Cumplimiento PCI-DSS para procesamiento de pagos",
            "aplicabilidad": "pagos_linea"
        },
        {
            "id": "R027",
            "categoria": "Financiero",
            "nombre": "Prevención de Fraude",
            "descripcion": "Controles específicos para prevenir fraude en operaciones",
            "aplicabilidad": "factoring", "confirming"
        },
        {
            "id": "R028",
            "categoria": "Financiero",
            "nombre": "Trazabilidad de Transacciones",
            "descripcion": "Todas las transacciones deben ser auditables",
            "aplicabilidad": "factoring", "confirming", "pagos_linea"
        },
        {
            "id": "R029",
            "categoria": "Financiero",
            "nombre": "Segregación de Funciones",
            "descripcion": "Separación de responsabilidades en procesos críticos",
            "aplicabilidad": "factoring", "confirming"
        },
        {
            "id": "R030",
            "categoria": "Datos",
            "nombre": "Protección de Datos Personales",
            "descripcion": "Cumplimiento con GDPR/LGPD para datos personales",
            "aplicabilidad": "todas"
        }
    ]
}


REGLAS_OPERATIVAS = {
    "incidentes": {
        "tiempo_respuesta": {
            "critico": 15,
            "alto": 60,
            "medio": 240,
            "bajo": 1440
        },
        "escalamiento": {
            "critico": ["CISO", "CEO", "Abogado"],
            "alto": ["CISO", "Director Area"],
            "medio": ["Team Leader Seguridad"],
            "bajo": ["Analista Seguridad"]
        }
    },
    "vulnerabilidades": {
        "slas_remediacion": {
            "critica": 24,
            "alta": 168,
            "media": 720,
            "baja": 2160
        }
    },
    "accesos": {
        "tiempo_aprobacion": {
            "temporal": 24,
            "permanente": 72
        },
        "caducidad": {
            "temporal": 72,
            "contrasena": 90
        }
    },
    "auditorias": {
        "frecuencia": {
            "interna": 365,
            "externa": 1095,
            "penetracion": 180
        }
    }
}


REGLAS_CUMPLIMIENTO_PCI_DSS = {
    "requisitos": [
        {"id": "1", "nombre": "Instalar y mantener configuración de firewall"},
        {"id": "2", "nombre": "No usar valores por defecto de vendor"},
        {"id": "3", "nombre": "Proteger datos de tarjeta almacenados"},
        {"id": "4", "nombre": "Cifrar transmisión de datos de titular"},
        {"id": "5", "nombre": "Mantener programa de antivirus"},
        {"id": "6", "nombre": "Desarrollar software seguro"},
        {"id": "7", "nombre": "Restringir acceso a datos por necesidad"},
        {"id": "8", "nombre": "Asignar identificación única a cada usuario"},
        {"id": "9", "nombre": "Restringir acceso físico a datos de tarjeta"},
        {"id": "10", "nombre": "Rastrear acceso a recursos de red"},
        {"id": "11", "nombre": "Probar seguridad de sistemas regularmente"},
        {"id": "12", "nombre": "Mantener política de seguridad"}
    ],
    "niveles_compliance": {
        "1": {"transacciones": ">6M, cualquier canal},
        "2": {"transacciones": "1M-6M"},
        "3": {"transacciones": "20K-1M e-commerce"},
        "4": {"transacciones": "<20K e-commerce o <1M otro"}
    }
}


def obtener_regla(regla_id: str) -> dict:
    """Obtiene una regla específica por su ID"""
    for regla in REGLAS_SISTEMA["reglas"]:
        if regla["id"] == regla_id:
            return regla
    return None


def obtener_reglas_por_categoria(categoria: str) -> list:
    """Obtiene todas las reglas de una categoría específica"""
    return [r for r in REGLAS_SISTEMA["reglas"] if r["categoria"] == categoria]


def obtener_reglas_por_actividad(actividad: str) -> list:
    """Obtiene las reglas aplicables a una actividad específica"""
    reglas = []
    for regla in REGLAS_SISTEMA["reglas"]:
        applicability = regla.get("aplicabilidad", "todas")
        if isinstance(applicability, str):
            if applicability == "todas" or applicability == actividad:
                reglas.append(regla)
        elif isinstance(applicability, list):
            if "todas" in applicability or actividad in applicability:
                reglas.append(regla)
    return reglas


def validar_cumplimiento_regla(regla_id: str, evidencia: dict) -> dict:
    """Valida el cumplimiento de una regla específica"""
    regla = obtener_regla(regla_id)
    if not regla:
        return {"error": "Regla no encontrada"}
    
    return {
        "regla_id": regla_id,
        "nombre": regla["nombre"],
        "categoria": regla["categoria"],
        "cumplimiento": evidencia.get("cumplido", False),
        "evidencia": evidencia.get("descripcion", ""),
        "fecha_verificacion": evidencia.get("fecha", "")
    }
