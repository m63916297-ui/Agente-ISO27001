"""RULES - Reglas del Sistema Multiagente ISO 27001"""

REGLAS_SISTEMA = {
    "version": "1.0.0",
    "reglas": [
        {
            "id": "R001",
            "categoria": "Gobierno",
            "nombre": "Autoridad del SGSI",
            "descripcion": "El CISO debe tener autoridad",
            "aplicabilidad": "todas",
        },
        {
            "id": "R002",
            "categoria": "Gobierno",
            "nombre": "Compromiso de la Direccion",
            "descripcion": "Compromiso con la seguridad",
            "aplicabilidad": "todas",
        },
        {
            "id": "R003",
            "categoria": "Planificacion",
            "nombre": "Evaluacion de Riesgos",
            "descripcion": "Evaluacion anual de riesgos",
            "aplicabilidad": "todas",
        },
        {
            "id": "R004",
            "categoria": "Planificacion",
            "nombre": "Tratamiento de Riesgos",
            "descripcion": "Plan de tratamiento documentado",
            "aplicabilidad": "todas",
        },
        {
            "id": "R005",
            "categoria": "Soporte",
            "nombre": "Competencia del Personal",
            "descripcion": "Capacitacion en seguridad",
            "aplicabilidad": "todas",
        },
        {
            "id": "R006",
            "categoria": "Soporte",
            "nombre": "Concienciacion",
            "descripcion": "Programa de concienciacion",
            "aplicabilidad": "todas",
        },
        {
            "id": "R007",
            "categoria": "Operacion",
            "nombre": "Gestion de Incidentes",
            "descripcion": "Proceso documentado",
            "aplicabilidad": "todas",
        },
        {
            "id": "R008",
            "categoria": "Operacion",
            "nombre": "Seguridad de Operaciones",
            "descripcion": "Procedimientos documentados",
            "aplicabilidad": "todas",
        },
        {
            "id": "R009",
            "categoria": "Operacion",
            "nombre": "Proteccion contra Malware",
            "descripcion": "Proteccion en endpoints",
            "aplicabilidad": "todas",
        },
        {
            "id": "R010",
            "categoria": "Operacion",
            "nombre": "Gestion de Vulnerabilidades",
            "descripcion": "Gestion por criticidad",
            "aplicabilidad": "todas",
        },
        {
            "id": "R011",
            "categoria": "Acceso",
            "nombre": "Control de Acceso Basado en Roles",
            "descripcion": "Acceso por roles",
            "aplicabilidad": "todas",
        },
        {
            "id": "R012",
            "categoria": "Acceso",
            "nombre": "Autenticacion Fuerte",
            "descripcion": "MFA obligatorio",
            "aplicabilidad": ["factoring", "confirming", "pagos_linea"],
        },
        {
            "id": "R013",
            "categoria": "Acceso",
            "nombre": "Revision de Accesos",
            "descripcion": "Revision trimestral",
            "aplicabilidad": "todas",
        },
        {
            "id": "R014",
            "categoria": "Criptografia",
            "nombre": "Cifrado de Datos en Reposo",
            "descripcion": "AES-256",
            "aplicabilidad": "todas",
        },
        {
            "id": "R015",
            "categoria": "Criptografia",
            "nombre": "Cifrado de Datos en Transito",
            "descripcion": "TLS 1.2 minimo",
            "aplicabilidad": "todas",
        },
        {
            "id": "R016",
            "categoria": "Criptografia",
            "nombre": "Gestion de Claves",
            "descripcion": "Rotacion anual",
            "aplicabilidad": "pagos_linea",
        },
        {
            "id": "R017",
            "categoria": "Fisico",
            "nombre": "Seguridad Fisica",
            "descripcion": "Controles de acceso fisico",
            "aplicabilidad": "todas",
        },
        {
            "id": "R018",
            "categoria": "Proveedores",
            "nombre": "Gestion de Proveedores",
            "descripcion": "Evaluacion anual",
            "aplicabilidad": "todas",
        },
        {
            "id": "R019",
            "categoria": "Proveedores",
            "nombre": "Acuerdos de Confidencialidad",
            "descripcion": "NDA obligatorio",
            "aplicabilidad": "todas",
        },
        {
            "id": "R020",
            "categoria": "Continuidad",
            "nombre": "Plan de Continuidad",
            "descripcion": "BCP documentado",
            "aplicabilidad": "todas",
        },
        {
            "id": "R021",
            "categoria": "Continuidad",
            "nombre": "Respaldo y Recuperacion",
            "descripcion": "Backups diarios",
            "aplicabilidad": "todas",
        },
        {
            "id": "R022",
            "categoria": "Continuidad",
            "nombre": "Alta Disponibilidad",
            "descripcion": "99.9% disponibilidad",
            "aplicabilidad": "pagos_linea",
        },
        {
            "id": "R023",
            "categoria": "Cumplimiento",
            "nombre": "Auditoria Interna",
            "descripcion": "Auditoria anual",
            "aplicabilidad": "todas",
        },
        {
            "id": "R024",
            "categoria": "Cumplimiento",
            "nombre": "Revision por la Direccion",
            "descripcion": "Revision trimestral",
            "aplicabilidad": "todas",
        },
        {
            "id": "R025",
            "categoria": "Cumplimiento",
            "nombre": "Gestion de No Conformidades",
            "descripcion": "Proceso documentado",
            "aplicabilidad": "todas",
        },
        {
            "id": "R026",
            "categoria": "Financiero",
            "nombre": "Proteccion de Datos Financieros",
            "descripcion": "Cumplimiento PCI-DSS",
            "aplicabilidad": "pagos_linea",
        },
        {
            "id": "R027",
            "categoria": "Financiero",
            "nombre": "Prevencion de Fraude",
            "descripcion": "Controles contra fraude",
            "aplicabilidad": ["factoring", "confirming"],
        },
        {
            "id": "R028",
            "categoria": "Financiero",
            "nombre": "Trazabilidad de Transacciones",
            "descripcion": "Transacciones auditables",
            "aplicabilidad": ["factoring", "confirming", "pagos_linea"],
        },
        {
            "id": "R029",
            "categoria": "Financiero",
            "nombre": "Segregacion de Funciones",
            "descripcion": "Separacion de responsabilidades",
            "aplicabilidad": ["factoring", "confirming"],
        },
        {
            "id": "R030",
            "categoria": "Datos",
            "nombre": "Proteccion de Datos Personales",
            "descripcion": "Cumplimiento GDPR/LGPD",
            "aplicabilidad": "todas",
        },
    ],
}

REGLAS_OPERATIVAS = {
    "incidentes": {
        "tiempo_respuesta": {"critico": 15, "alto": 60, "medio": 240, "bajo": 1440},
        "escalamiento": {
            "critico": ["CISO", "CEO"],
            "alto": ["CISO"],
            "medio": ["Team Leader"],
            "bajo": ["Analista"],
        },
    },
    "vulnerabilidades": {
        "slas_remediacion": {"critica": 24, "alta": 168, "media": 720, "baja": 2160}
    },
    "accesos": {
        "tiempo_aprobacion": {"temporal": 24, "permanente": 72},
        "caducidad": {"temporal": 72, "contrasena": 90},
    },
    "auditorias": {"frecuencia": {"interna": 365, "externa": 1095, "penetracion": 180}},
}

REGLAS_CUMPLIMIENTO_PCI_DSS = {
    "requisitos": [
        {"id": "1", "nombre": "Firewall"},
        {"id": "2", "nombre": "Valores por defecto"},
        {"id": "3", "nombre": "Datos de tarjeta"},
        {"id": "4", "nombre": "Cifrado transmision"},
        {"id": "5", "nombre": "Antivirus"},
        {"id": "6", "nombre": "Software seguro"},
        {"id": "7", "nombre": "Menor privilegio"},
        {"id": "8", "nombre": "Identificacion unica"},
        {"id": "9", "nombre": "Acceso fisico"},
        {"id": "10", "nombre": "Rastreo"},
        {"id": "11", "nombre": "Pruebas"},
        {"id": "12", "nombre": "Politica de seguridad"},
    ]
}


def obtener_regla(regla_id):
    for regla in REGLAS_SISTEMA["reglas"]:
        if regla["id"] == regla_id:
            return regla
    return None


def obtener_reglas_por_categoria(categoria):
    return [r for r in REGLAS_SISTEMA["reglas"] if r["categoria"] == categoria]


def obtener_reglas_por_actividad(actividad):
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


def validar_cumplimiento_regla(regla_id, evidencia):
    regla = obtener_regla(regla_id)
    if not regla:
        return {"error": "Regla no encontrada"}
    return {
        "regla_id": regla_id,
        "nombre": regla["nombre"],
        "categoria": regla["categoria"],
        "cumplimiento": evidencia.get("cumplido", False),
        "evidencia": evidencia.get("descripcion", ""),
        "fecha_verificacion": evidencia.get("fecha", ""),
    }
