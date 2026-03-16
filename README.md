# Sistema Multiagente ISO 27001 para Empresas de Factoring, Confirming y Pagos en Línea

## 📋 Índice

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Acerca de ISO 27001](#acerca-de-iso-27001)
3. [Alcance del Sistema](#alcance-del-sistema)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Arquitectura Multiagente](#arquitectura-multiagente)
6. [Reglas del Sistema](#reglas-del-sistema)
7. [Habilidades de los Agentes](#habilidades-de-los-agentes)
8. [Métricas ISO 27001](#métricas-iso-27001)
9. [Criterios por Actividad](#criterios-por-actividad)
10. [Guía de Implementación](#guía-de-implementación)
11. [Requisitos de Certificación](#requisitos-de-certificación)
12. [Normativas Adicionales](#normativas-adicionales)
13. [Roadmap de Implementación](#roadmap-de-implementación)

---

## 1. Resumen Ejecutivo

Este sistema multiagente está diseñado para apoyar a empresas especializadas en **operaciones de factoring, confirming y pagos en línea** en el proceso de obtención y mantenimiento de la certificación **ISO 27001:2022**.

El sistema cuenta con:
- **8 agentes especializados** que automatizan diferentes aspectos del SGSI
- **30 reglas de seguridad** específicas para el sector financiero
- **15 métricas** configurables para medir el desempeño
- **20 criterios de evaluación** específicos por tipo de operación
- **Interfaz web** construida con Streamlit

---

## 2. Acerca de ISO 27001

### ¿Qué es ISO 27001?

ISO/IEC 27001 es la norma internacional más reconocida para los Sistemas de Gestión de Seguridad de la Información (SGSI). Proporciona un marco para gestionar la información sensible de una organización mediante:

- **Confidencialidad**: Protección de información contra acceso no autorizado
- **Integridad**: Salvaguardia de la precisión y completitud de la información
- **Disponibilidad**: Garantizar que los usuarios autorizados tengan acceso cuando lo necesiten

### Versión Actual: ISO 27001:2022

La versión actual fue publicada en octubre de 2022 e incluye:
- 11 nuevos controles (total: 93)
- 4 controles eliminados
- Terminología actualizada
- Mayor enfoque en amenazas emergentes

### Controles del Anexo A (ISO 27001:2022)

| Categoría | Controles | Descripción |
|-----------|-----------|-------------|
| A.5 | 5 | Controles organizacionales |
| A.6 | 2 | Controles de personas |
| A.7 | 2 | Controles físicos |
| A.8 | 13 | Controles tecnológicos |
| A.9 | 9 | Controles de acceso |
| A.8 | 2 | Criptografía |
| A.11 | 14 | Operaciones de seguridad |
| A.12 | 10 | Seguridad de las comunicaciones |
| A.13 | 7 | Adquisición y desarrollo |
| A.14 | 5 | Relación con proveedores |
| A.15 | 9 | Gestión de incidentes |
| A.16 | 4 | Continuidad del negocio |
| A.17 | 2 | Cumplimiento |

---

## 3. Alcance del Sistema

### Empresa Objetivo

**Tipo**: Empresa de servicios financieros especializada en:
- **Factoring**: Cesión de facturas y gestión de cartera
- **Confirming**: Gestión de pagos a proveedores
- **Pagos en Línea**: Procesamiento de transacciones electrónicas

### Requisitos del Sistema

Para implementar este SGSI, la empresa debe considerar:

| Área | Requisitos Mínimos |
|------|-------------------|
| Tecnología | Sistemas de información, redes, bases de datos |
| Personas | Personal capacitado, roles definidos |
| Procesos | Procedimientos documentados |
| Legal | Cumplimiento regulatorio financiero |
| Física | Controles de acceso físico |

---

## 4. Estructura del Proyecto

```
auditoria/
├── config.py              # Configuración general
├── metricas.py            # Templates de métricas ISO 27001
├── criterios.py          # Criterios por actividad
├── rules.py              # Reglas del sistema (30 reglas)
├── skills.py             # Habilidades de los agentes
├── agentes.py           # Implementación de los 8 agentes
├── mejora_procesos.py   # Módulo de mejora de procesos
├── main.py              # Interfaz CLI
├── app.py               # Aplicación Streamlit (Frontend)
├── requirements.txt     # Dependencias Python
└── README.md            # Este archivo
```

---

## 5. Arquitectura Multiagente

### Agentes del Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│                    COORDINATOR AGENT                           │
│                   (Orquestador Central)                        │
└─────────────────────────────────────────────────────────────────┘
         │        │        │        │        │        │
    ┌────┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐
    │AUDITOR││RIESGO ││CUMPL  ││INCID  ││MEJORA ││CAPACIT│
    │       ││       ││       ││       ││       ││       │
    └────┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘
         │        │        │        │        │        │
    ┌────┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐
    │AUDITOR││RIESGO ││CUMPL  ││INCID  ││MEJORA ││CAPACIT│
    │       ││       ││       ││       ││       ││       │
    └────┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘
         │        │        │        │        │        │
    ┌────┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐
    │AUDITOR││RIESGO ││CUMPL  ││INCID  ││MEJORA ││CAPACIT│
    │       ││       ││       ││       ││       ││       │
    └────┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘
         │        │        │        │        │        │
    ┌────┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐
    │AUDITOR││RIESGO ││CUMPL  ││INCID  ││MEJORA ││CAPACIT│
    │       ││       ││       ││       ││       ││       │
    └────┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘
```

### Descripción de Agentes

| Agente | Función Principal | Controles ISO Clave |
|--------|-------------------|---------------------|
| **Auditor** | Planificar y ejecutar auditorías internas | A.18.1, A.18.2 |
| **Riesgo** | Identificar y evaluar riesgos de seguridad | A.6.1 |
| **Cumplimiento** | Verificar conformidad con normativas | A.18.1 |
| **Incidentes** | Detectar y responder a incidentes | A.16.1 |
| **Mejora** | Proponer e implementar mejoras | A.10.1 |
| **Capacitación** | Gestionar formación en seguridad | A.7.2 |
| **Proveedores** | Evaluar terceros | A.15.1 |
| **Políticas** | Administrar políticas de seguridad | A.5.1 |

---

## 6. Reglas del Sistema

### 6.1 Reglas por Categoría

#### Gobierno (R001-R002)
- R001: Autoridad del SGSI
- R002: Compromiso de la Dirección

#### Planificación (R003-R004)
- R003: Evaluación de Riesgos Obligatoria
- R004: Tratamiento de Riesgos

#### Soporte (R005-R006)
- R005: Competencia del Personal
- R006: Concienciación Continua

#### Operación (R007-R010)
- R007: Gestión de Incidentes
- R008: Seguridad de Operaciones
- R009: Protección contra Malware
- R010: Gestión de Vulnerabilidades

#### Acceso (R011-R013)
- R011: Control de Acceso Basado en Roles
- R012: Autenticación Fuerte
- R013: Revisión de Accesos

#### Criptografía (R014-R016)
- R014: Cifrado de Datos en Reposo
- R015: Cifrado de Datos en Tránsito
- R016: Gestión de Claves

#### Física (R017)
- R017: Seguridad Física

#### Proveedores (R018-R019)
- R018: Gestión de Proveedores
- R019: Acuerdos de Confidencialidad

#### Continuidad (R020-R022)
- R020: Plan de Continuidad
- R021: Respaldo y Recuperación
- R022: Alta Disponibilidad

#### Cumplimiento (R023-R025)
- R023: Auditoría Interna
- R024: Revisión por la Dirección
- R025: Gestión de No Conformidades

#### Financiera (R026-R029)
- R026: Protección de Datos Financieros (PCI-DSS)
- R027: Prevención de Fraude
- R028: Trazabilidad de Transacciones
- R029: Segregación de Funciones

#### Datos (R030)
- R030: Protección de Datos Personales

### 6.2 SLAs Operativos

| Tipo | Criticidad | Tiempo Máximo |
|------|------------|---------------|
| Respuesta a Incidentes | Crítica | 15 min |
| Respuesta a Incidentes | Alta | 60 min |
| Respuesta a Incidentes | Media | 4 horas |
| Respuesta a Incidentes | Baja | 24 horas |
| Remediación de Vulnerabilidades | Crítica | 24 horas |
| Remediación de Vulnerabilidades | Alta | 7 días |
| Aprobación de Acceso | Temporal | 24 horas |
| Aprobación de Acceso | Permanente | 72 horas |

---

## 7. Habilidades de los Agentes

### 7.1 Agente Auditor

**Skills:**
- AUD-001: Planificación de Auditorías (Nivel 5)
- AUD-002: Ejecución de Auditorías (Nivel 5)
- AUD-003: Análisis de Hallazgos (Nivel 4)
- AUD-004: Comunicación de Resultados (Nivel 4)

**Certificaciones:** CISA, ISO 27001 LA

### 7.2 Agente de Riesgos

**Skills:**
- RSG-001: Identificación de Riesgos (Nivel 5)
- RSG-002: Evaluación de Riesgos (Nivel 5)
- RSG-003: Tratamiento de Riesgos (Nivel 4)
- RSG-004: Análisis de Riesgos Financieros (Nivel 4)

**Certificaciones:** CRISC, CISM, CFR

### 7.3 Agente de Cumplimiento

**Skills:**
- CMP-001: Verificación de Cumplimiento (Nivel 5)
- CMP-002: Análisis Gap (Nivel 5)
- CMP-003: Gestión de Evidencias (Nivel 4)
- CMP-004: Cumplimiento PCI-DSS (Nivel 4)

**Certificaciones:** ISO 27001 LA, CIPP, PCIP, QSA

### 7.4 Agente de Incidentes

**Skills:**
- INC-001: Detección de Incidentes (Nivel 5)
- INC-002: Clasificación de Incidentes (Nivel 4)
- INC-003: Respuesta a Incidentes (Nivel 5)
- INC-004: Análisis Forense (Nivel 4)

**Certificaciones:** GCFA, GCIH, GCFE

### 7.5 Agente de Mejora

**Skills:**
- MJR-001: Análisis de Mejoras (Nivel 4)
- MJR-002: Diseño de Procesos (Nivel 4)
- MJR-003: Gestión de Cambios (Nivel 3)
- MJR-004: Métricas de Eficacia (Nivel 4)

**Certificaciones:** Lean IT, ITIL

### 7.6 Agente de Capacitación

**Skills:**
- CAP-001: Diseño de Programas (Nivel 4)
- CAP-002: Concienciación (Nivel 4)
- CAP-003: Capacitación Técnica (Nivel 4)
- CAP-004: Evaluación de Efectividad (Nivel 3)

**Certificaciones:** CSE, CST

### 7.7 Agente de Proveedores

**Skills:**
- PRV-001: Evaluación de Proveedores (Nivel 4)
- PRV-002: Gestión de Contratos (Nivel 3)
- PRV-003: Monitoreo Continuo (Nivel 4)
- PRV-004: Riesgo de Cadena de Suministro (Nivel 4)

**Certificaciones:** ISO 27001 LA, CCSP

### 7.8 Agente de Políticas

**Skills:**
- POL-001: Desarrollo de Políticas (Nivel 5)
- POL-002: Revisión y Actualización (Nivel 4)
- POL-003: Comunicación de Políticas (Nivel 4)
- POL-004: Análisis de Cumplimiento (Nivel 4)

**Certificaciones:** CISM, ISO 27001 LA

---

## 8. Métricas ISO 27001

### 8.1 Métricas Definidas

| ID | Nombre | Objetivo | Categoría |
|----|--------|----------|-----------|
| M-ISO-001 | Tasa de Cumplimiento de Controles de Acceso | ≥95% | Acceso |
| M-ISO-002 | Tiempo de Detección de Intrusiones | ≤15 min | Operaciones |
| M-ISO-003 | Transacciones Fraudulentas Detectadas | ≥98% | Comunicaciones |
| M-ISO-004 | Disponibilidad de Sistemas de Pago | ≥99.99% | Continuidad |
| M-ISO-005 | Cumplimiento de Política de Contraseñas | 100% | Acceso |
| M-ISO-006 | Incidentes de Seguridad por Categoría | 0 críticos | Incidentes |
| M-ISO-007 | Cobertura de Capacitación | 100% | Personas |
| M-ISO-008 | Auditorías Internas Completadas | 100% | Cumplimiento |
| M-ISO-009 | Vulnerabilidades Críticas Pendientes | 0 | Tecnológico |
| M-ISO-010 | Cumplimiento de Proveedores Críticos | 100% | Proveedores |
| M-ISO-011 | Tasa de Cifrado de Datos en Tránsito | 100% | Criptografía |
| M-ISO-012 | Eficacia del Plan de Continuidad | ≥90% | Continuidad |
| M-ISO-013 | Evaluación de Riesgo Actualizada | ≤180 días | Organizacional |
| M-ISO-014 | Backups Exitosos | 100% | Operaciones |
| M-ISO-015 | Tokens de Pago Seguro | ≥85% | Criptografía |

---

## 9. Criterios por Actividad

### 9.1 Criterios para Factoring (6)

| ID | Nombre | Controles ISO | Peso |
|----|--------|---------------|------|
| CF-001 | Protección de Datos de Cartera Cedida | A.10.1, A.10.2, A.9.1, A.9.2 | 2.0 |
| CF-002 | Autenticación en Sistema de Factoring | A.9.1, A.9.2, A.9.4, A.9.5 | 2.5 |
| CF-003 | Integridad de Procesos de Cesión | A.12.3, A.12.4, A.16.1 | 1.5 |
| CF-004 | Gestión de Riesgos Crediticios | A.6.1, A.6.1.1, A.6.1.2 | 2.0 |
| CF-005 | Continuidad en Cobranza | A.17.1, A.17.2, A.17.3 | 1.5 |
| CF-006 | Protección de Información de Clientes | A.8.2, A.8.3, A.8.4 | 2.0 |

### 9.2 Criterios para Confirming (6)

| ID | Nombre | Controles ISO | Peso |
|----|--------|---------------|------|
| CC-001 | Seguridad en Gestión de Pagos | A.13.1, A.13.2, A.9.4 | 2.5 |
| CC-002 | Integración con Sistemas ERP | A.13.2, A.14.1, A.14.3 | 1.5 |
| CC-003 | Protección de Datos Bancarios | A.10.1, A.10.2, A.8.2 | 2.0 |
| CC-004 | Control de Fraude en Confirming | A.12.2, A.12.3, A.16.1 | 2.5 |
| CC-005 | Auditoría de Operaciones de Pago | A.12.4, A.18.1, A.18.2 | 1.5 |
| CC-006 | Gestión de Proveedores de Confirming | A.15.1, A.15.2, A.15.3 | 1.5 |

### 9.3 Criterios para Pagos en Línea (8)

| ID | Nombre | Controles ISO | Peso |
|----|--------|---------------|------|
| CP-001 | Cumplimiento PCI-DSS | A.10.1, A.10.2, A.8.1, A.9.1 | 3.0 |
| CP-002 | Tokenización y Cifrado de Pagos | A.10.1, A.10.2, A.10.3 | 2.5 |
| CP-003 | Autenticación Fuerte de Clientes | A.9.1, A.9.4, A.9.5 | 2.5 |
| CP-004 | Protección contra Fraude en Tiempo Real | A.12.2, A.12.3, A.13.1 | 2.0 |
| CP-005 | Seguridad de APIs de Pago | A.13.1, A.13.2, A.14.3 | 2.0 |
| CP-006 | Continuidad de Pagos Electrónicos | A.17.1, A.17.2, A.17.3 | 2.0 |
| CP-007 | Gestión de Incidentes de Pago | A.16.1, A.16.1.1, A.16.1.2 | 1.5 |
| CP-008 | Monitoreo de Transacciones | A.12.1, A.12.2, A.12.3 | 1.5 |

---

## 10. Guía de Implementación

### Fase 1: Inicio (Semanas 1-4)

1. **Definir Alcance**
   - Identificar sistemas críticos
   - Definir límites del SGSI

2. **Obtener Compromiso**
   - Presentación a dirección
   - Asignación de recursos

3. **Constituir Equipo SGSI**
   - Designar CISO
   - Seleccionar equipo core

### Fase 2: Análisis (Semanas 5-12)

1. **Evaluación de Riesgos**
   - Identificar activos
   - Analizar amenazas
   - Evaluar vulnerabilidades

2. **Análisis Gap**
   - Comparar estado actual vs ISO 27001
   - Identificar brechas

3. **Diseño de Controles**
   - Seleccionar controles del Anexo A
   - Documentar implementación

### Fase 3: Implementación (Semanas 13-26)

1. **Controles Técnicos**
   - Configurar firewalls
   - Implementar cifrado
   - Configurar IAM

2. **Controles Organizacionales**
   - Publicar políticas
   - Definir procedimientos
   - Establecer roles

3. **Controles de Personas**
   - Capacitación inicial
   - Programa de concienciación

### Fase 4: Operación (Semanas 27-52)

1. **Gestión de Incidentes**
   - Activar proceso de respuesta
   - Monitoreo continuo

2. **Mantenimiento**
   - Revisión de accesos
   - Actualización de vulnerabilidades

3. **Auditorías**
   - Auditoría interna
   - Preparación para certificación

---

## 11. Requisitos de Certificación

### 11.1 Requisitos Obligatorios (Cláusulas 4-10)

| Cláusula | Requisito | Evidencia Requerida |
|----------|-----------|---------------------|
| 4 | Contexto de la organización | Documento de contexto |
| 5 | Liderazgo | Política de seguridad, asignaciones |
| 6 | Planificación | Evaluación de riesgos, tratamiento |
| 7 | Soporte | Recursos, competencia, comunicación |
| 8 | Operación | Planificación, evaluación de riesgos |
| 9 | Evaluación de desempeño | Mediciones, auditorías |
| 10 | Mejora | No conformidades, acciones correctivas |

### 11.2 Controles del Anexo A Obligatorios

Todos los 93 controles del Anexo A deben ser evaluados:
- 5 controles organizacionales (A.5)
- 2 controles de personas (A.6)
- 2 controles físicos (A.7)
- 34 controles tecnológicos (A.8-A.14)
- 15 controles de gestión (A.15-A.17)

### 11.3 Documentación Mínima Requerida

1. **Política de Seguridad de la Información**
2. **Alcance del SGSI**
3. **Evaluación de Riesgos**
4. **Declaración de Aplicabilidad (SoA)**
5. **Plan de Tratamiento de Riesgos**
6. **Definición de Roles de Seguridad**
7. **Inventario de Activos**
8. **Procedimientos de Gestión de Incidentes**
9. **Plan de Continuidad del Negocio**
10. **Registros de Auditoría**

---

## 12. Normativas Adicionales

### 12.1 PCI-DSS (Pagos en Línea)

Para operaciones de pagos en línea, se requiere cumplimiento con PCI-DSS 4.0:

| Requisito | Descripción |
|-----------|-------------|
| 1 | Instalar y mantener configuración de firewall |
| 2 | No usar valores por defecto de vendor |
| 3 | Proteger datos de tarjeta almacenados |
| 4 | Cifrar transmisión de datos |
| 5 | Mantener programa de antivirus |
| 6 | Desarrollar software seguro |
| 7 | Restringir acceso por necesidad |
| 8 | Asignar identificación única |
| 9 | Restringir acceso físico |
| 10 | Rastrear acceso a recursos |
| 11 | Probar seguridad regularmente |
| 12 | Mantener política de seguridad |

### 12.2 PSD2 (Servicios de Pago)

Para operaciones de confirming y pagos:
- Autenticación fuerte (SCA)
- Open Banking APIs seguras
- Protección contra fraude

### 12.3 GDPR/LGPD (Protección de Datos)

- Consentimiento explícito
- Derechos ARCO/ LGPD
- Notificación de brechas (72 horas)
- DPO designado

### 12.4 SOX (Controles Financieros)

- Trazabilidad de transacciones
- Segregación de funciones
- Controles de acceso
- Retención de registros

### 12.5 Basilea III (Riesgos Bancarios)

- Gestión de riesgos operativos
- Controles de seguridad
- Continuidad del negocio

---

## 13. Roadmap de Implementación

```
Mes 1-3:    ████████░░░░░░░░░░░░░░░░░░░ 30% - Inicio y Análisis
Mes 4-6:    ████████████████░░░░░░░░░░░░ 50% - Diseño y Planificación
Mes 7-12:   ██████████████████████████░░ 90% - Implementación
Mes 13:     ████████████████████████████ 100% - Auditoría y Certificación
```

---

## Contacto y Soporte

Para consultas sobre el sistema:
- Documentación técnica disponible en `/docs`
- Contacto: soporte@empresa.com

---

**Versión del Documento**: 1.0  
**Fecha de Creación**: 2026-03-16  
**Próxima Revisión**: 2026-06-16
