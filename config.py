"""
Configuración principal del Sistema Multiagente ISO 27001
para empresa de Factoring, Confirming y Pagos en Línea
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
REPORTES_DIR = BASE_DIR / "reportes"

for directory in [DATA_DIR, LOGS_DIR, REPORTES_DIR]:
    directory.mkdir(exist_ok=True)

EMPRESA_CONFIG = {
    "nombre": "Empresa de Factoring y Confirming",
    "sector": "Servicios Financieros",
    "actividades": ["factoring", "confirming", "pagos_linea"],
    "normativa": ["ISO27001:2022", "PCI-DSS", "GDPR", "LOC"],
    "tamano": "mediana",
}

CONTROL_CATEGORIES = [
    "A.5 - Controles Organizacionales",
    "A.6 - Controles de Personas",
    "A.7 - Controles Físicos",
    "A.8 - Controles Tecnológicos",
    "A.9 - Controles de Acceso",
    "A.10 - Criptografía",
    "A.11 - Operaciones de Seguridad",
    "A.12 - Seguridad de las Comunicaciones",
    "A.13 - Adquisición y Desarrollo",
    "A.14 - Relación con Proveedores",
    "A.15 - Gestión de Incidentes",
    "A.16 - Continuidad del Negocio",
    "A.17 - Cumplimiento",
]

RIESGOS_ESPECIFICOS = {
    "factoring": ["R01", "R02", "R03", "R04", "R05", "R06"],
    "confirming": ["C01", "C02", "C03", "C04", "C05", "C06"],
    "pagos_linea": ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08"],
}
