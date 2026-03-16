#!/usr/bin/env python3
"""
CLI del Sistema Multiagente ISO 27001
Interfaz de línea de comandos para gestión de certificación ISO 27001
"""

import sys
import json
from typing import Optional, List
from datetime import datetime

from metricas import GestorMetricas, TemplatesMetricas, TipoMetrica, CategoriaControl
from criterios import GestorCriterios, TipoOperacion
from agentes import (
    CoordinatorAgent,
    TipoAgente,
    AgenteAuditor,
    AgenteRiesgo,
    AgenteCumplimiento,
    AgenteIncidentes,
    AgenteMejora,
    AgenteCapacitacion,
    AgenteProveedores,
    AgentePoliticas,
)
from mejora_procesos import MotorMejoraSGSI, TipoProceso, EstadoProceso


class MenuPrincipal:
    def __init__(self):
        self.gestor_metricas = GestorMetricas()
        self.gestor_criterios = GestorCriterios()
        self.coordinador = CoordinatorAgent()
        self.motor_mejora = MotorMejoraSGSI()
        self.ejecutando = True

    def limpiar_pantalla(self):
        print("\n" + "=" * 60)

    def mostrar_banner(self):
        print("""
╔═══════════════════════════════════════════════════════════════╗
║         SISTEMA MULTIAGENTE ISO 27001                         ║
║    Gestión de Seguridad de la Información                    ║
║    Factoring | Confirming | Pagos en Línea                   ║
╚═══════════════════════════════════════════════════════════════╝
        """)

    def mostrar_menu_principal(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│                     MENÚ PRINCIPAL                           │
├─────────────────────────────────────────────────────────────┤
│  1. 📊 Métricas ISO 27001                                   │
│  2. 📋 Criterios por Actividad                               │
│  3. 🤖 Agentes del SGSI                                     │
│  4. 🔄 Mejora de Procesos                                    │
│  5. 📈 Dashboard General                                     │
│  6. ⚙️  Configuración                                        │
│  0. 🚪 Salir                                                 │
└─────────────────────────────────────────────────────────────┘
        """)

    def menu_metricas(self):
        while True:
            print("""
┌─────────────────────────────────────────────────────────────┐
│                     MÉTRICAS ISO 27001                       │
├─────────────────────────────────────────────────────────────┤
│  1. Listar todas las métricas                               │
│  2. Ver métricas por categoría                               │
│  3. Evaluar una métrica                                      │
│  4. Agregar registro de métrica                              │
│  5. Dashboard de métricas                                     │
│  0. Volver al menú principal                                │
└─────────────────────────────────────────────────────────────┘
            """)

            opcion = input("Seleccione opción: ").strip()

            if opcion == "1":
                self._listar_metricas()
            elif opcion == "2":
                self._metricas_por_categoria()
            elif opcion == "3":
                self._evaluar_metrica()
            elif opcion == "4":
                self._agregar_registro()
            elif opcion == "5":
                self._dashboard_metricas()
            elif opcion == "0":
                break
            else:
                print("❌ Opción inválida")

    def _listar_metricas(self):
        templates = self.gestor_metricas.templates
        print(f"\nTotal de métricas: {len(templates)}")
        print("-" * 60)
        for t in templates:
            print(f"  [{t.id}] {t.nombre}")
            print(f"       Categoría: {t.categoria.value} | Tipo: {t.tipo.value}")
            print(f"       Objetivo: {t.umbral.objetivo} {t.umbral.unidad}")
            print()

    def _metricas_por_categoria(self):
        print("\nCategorías disponibles:")
        for cat in CategoriaControl:
            print(f"  {cat.value}")

        categoria = input("\nIngrese categoría: ").strip().upper()
        try:
            cat_enum = CategoriaControl(categoria)
            metricas = [
                m for m in self.gestor_metricas.templates if m.categoria == cat_enum
            ]
            print(f"\nMétricas en {categoria}: {len(metricas)}")
            for m in metricas:
                print(f"  [{m.id}] {m.nombre}")
        except ValueError:
            print("❌ Categoría inválida")

    def _evaluar_metrica(self):
        metrica_id = input("Ingrese ID de métrica (ej: M-ISO-001): ").strip()
        try:
            valor = float(input("Ingrese valor a evaluar: ").strip())
            resultado = self.gestor_metricas.evaluar_metrica(metrica_id, valor)
            print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")
        except ValueError:
            print("❌ Error al evaluar métrica")

    def _agregar_registro(self):
        print("\nFuncionalidad de registro en desarrollo")

    def _dashboard_metricas(self):
        dashboard = self.gestor_metricas.get_dashboard_resumen()
        print(f"\n{'=' * 60}")
        print(f"DASHBOARD DE MÉTRICAS ISO 27001")
        print(f"{'=' * 60}")
        print(f"Total métricas configuradas: {dashboard['total_metricas']}")
        print(f"Total registros: {dashboard['registros_totales']}")

    def menu_criterios(self):
        while True:
            print("""
┌─────────────────────────────────────────────────────────────┐
│                  CRITERIOS POR ACTIVIDAD                     │
├─────────────────────────────────────────────────────────────┤
│  1. Criterios para Factoring                                │
│  2. Criterios para Confirming                               │
│  3. Criterios para Pagos en Línea                          │
│  4. Ver todos los criterios                                 │
│  5. Resumen por tipo                                        │
│  0. Volver al menú principal                                │
└─────────────────────────────────────────────────────────────┘
            """)

            opcion = input("Seleccione opción: ").strip()

            if opcion == "1":
                self._ver_criterios(TipoOperacion.FACTORING)
            elif opcion == "2":
                self._ver_criterios(TipoOperacion.CONFIRMING)
            elif opcion == "3":
                self._ver_criterios(TipoOperacion.PAGOS_LINEA)
            elif opcion == "4":
                self._ver_todos_criterios()
            elif opcion == "5":
                self._resumen_criterios()
            elif opcion == "0":
                break
            else:
                print("❌ Opción inválida")

    def _ver_criterios(self, tipo: TipoOperacion):
        criterios = self.gestor_criterios.get_criterios_por_tipo(tipo)
        print(f"\n{'=' * 60}")
        print(f"CRITERIOS PARA {tipo.value.upper()}")
        print(f"{'=' * 60}")

        for c in criterios:
            print(f"\n[{c.id}] {c.nombre}")
            print(f"  Descripción: {c.descripcion}")
            print(f"  Categoría: {c.categoria_riesgo.value}")
            print(f"  Peso: {c.peso}")
            print(f"  Controles: {', '.join(c.controles_relacionados)}")

    def _ver_todos_criterios(self):
        print(
            json.dumps(
                json.loads(self.gestor_criterios.get_all_criterios_json()),
                indent=2,
                ensure_ascii=False,
            )
        )

    def _resumen_criterios(self):
        resumen = self.gestor_criterios.get_resumen_por_tipo()
        print(f"\n{json.dumps(resumen, indent=2, ensure_ascii=False)}")

    def menu_agentes(self):
        while True:
            print("""
┌─────────────────────────────────────────────────────────────┐
│                    AGENTES DEL SGSI                          │
├─────────────────────────────────────────────────────────────┤
│  1. Estado del Sistema de Agentes                           │
│  2. Agente Auditor                                          │
│  3. Agente de Riesgos                                       │
│  4. Agente de Cumplimiento                                  │
│  5. Agente de Incidentes                                    │
│  6. Agente de Mejora                                        │
│  7. Agente de Capacitación                                  │
│  8. Agente de Proveedores                                   │
│  9. Agente de Políticas                                     │
│  0. Volver al menú principal                                │
└─────────────────────────────────────────────────────────────┘
            """)

            opcion = input("Seleccione opción: ").strip()

            if opcion == "1":
                self._estado_agentes()
            elif opcion == "2":
                self._agente_auditor()
            elif opcion == "3":
                self._agente_riesgos()
            elif opcion == "4":
                self._agente_cumplimiento()
            elif opcion == "5":
                self._agente_incidentes()
            elif opcion == "6":
                self._agente_mejora()
            elif opcion == "7":
                self._agente_capacitacion()
            elif opcion == "8":
                self._agente_proveedores()
            elif opcion == "9":
                self._agente_politicas()
            elif opcion == "0":
                break
            else:
                print("❌ Opción inválida")

    def _estado_agentes(self):
        estado = self.coordinador.get_estado_sistema()
        print(f"\n{json.dumps(estado, indent=2, ensure_ascii=False)}")

    def _agente_auditor(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│                  AGENTE AUDITOR                             │
├─────────────────────────────────────────────────────────────┤
│  1. Planificar auditoría                                    │
│  2. Ejecutar auditoría                                      │
│  3. Generar informe                                        │
└─────────────────────────────────────────────────────────────┘
        """)
        opcion = input("Seleccione: ").strip()
        contexto = {"accion": ""}

        if opcion == "1":
            contexto["accion"] = "planificar"
            contexto["alcance"] = input("Alcance: ").strip() or "general"
        elif opcion == "2":
            contexto["accion"] = "ejecutar"
            contexto["tarea_id"] = input("ID de tarea: ").strip()
        elif opcion == "3":
            contexto["accion"] = "reportar"
            contexto["tarea_id"] = input("ID de tarea: ").strip()

        resultado = self.coordinador.ejecutar_agente(TipoAgente.AUDITOR, contexto)
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def _agente_riesgos(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│                 AGENTE DE RIESGOS                            │
├─────────────────────────────────────────────────────────────┤
│  1. Identificar riesgos                                     │
│  2. Evaluar riesgo                                          │
│  3. Tratar riesgo                                          │
└─────────────────────────────────────────────────────────────┘
        """)
        opcion = input("Seleccione: ").strip()
        contexto = {"accion": ""}

        if opcion == "1":
            contexto["accion"] = "identificar"
            contexto["actividad"] = input(
                "Actividad (factoring/confirming/pagos_linea): "
            ).strip()
        elif opcion == "2":
            contexto["accion"] = "evaluar"
            contexto["riesgo_id"] = input("ID de riesgo: ").strip()
            contexto["probabilidad"] = int(input("Probabilidad (1-5): ").strip() or "3")
            contexto["impacto"] = int(input("Impacto (1-5): ").strip() or "3")
        elif opcion == "3":
            contexto["accion"] = "tratar"
            contexto["riesgo_id"] = input("ID de riesgo: ").strip()
            contexto["tratamiento"] = input("Tratamiento: ").strip()

        resultado = self.coordinador.ejecutar_agente(TipoAgente.RIESGO, contexto)
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def _agente_cumplimiento(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│               AGENTE DE CUMPLIMIENTO                         │
├─────────────────────────────────────────────────────────────┤
│  1. Verificar cumplimiento                                  │
│  2. Análisis Gap                                            │
│  3. Gestionar evidencia                                     │
└─────────────────────────────────────────────────────────────┘
        """)
        opcion = input("Seleccione: ").strip()
        contexto = {"accion": ""}

        if opcion == "1":
            contexto["accion"] = "verificar"
            contexto["norma"] = (
                input("Norma (ISO27001/PCI-DSS): ").strip() or "ISO27001"
            )
        elif opcion == "2":
            contexto["accion"] = "gap"
            contexto["norma"] = input("Norma: ").strip() or "ISO27001"
        elif opcion == "3":
            contexto["accion"] = "evidencia"
            contexto["control"] = input("Control (ej: A.9.1): ").strip()

        resultado = self.coordinador.ejecutar_agente(TipoAgente.CUMPLIMIENTO, contexto)
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def _agente_incidentes(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│               AGENTE DE INCIDENTES                          │
├─────────────────────────────────────────────────────────────┤
│  1. Detectar incidente                                      │
│  2. Clasificar incidente                                    │
│  3. Responder incidente                                     │
└─────────────────────────────────────────────────────────────┘
        """)
        opcion = input("Seleccione: ").strip()
        contexto = {"accion": ""}

        if opcion == "1":
            contexto["accion"] = "detectar"
            contexto["descripcion"] = input("Descripción: ").strip()
            contexto["fuente"] = input("Fuente: ").strip() or "SIEM"
        elif opcion == "2":
            contexto["accion"] = "clasificar"
            contexto["incidente_id"] = input("ID de incidente: ").strip()
            contexto["severidad"] = (
                input("Severidad (critica/alta/media/baja): ").strip() or "media"
            )
        elif opcion == "3":
            contexto["accion"] = "responder"
            contexto["incidente_id"] = input("ID de incidente: ").strip()
            contexto["accion"] = input("Fase (contener/erradicar/recuperar): ").strip()

        resultado = self.coordinador.ejecutar_agente(TipoAgente.INCIDENTES, contexto)
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def _agente_mejora(self):
        print("Agente de Mejora en desarrollo")

    def _agente_capacitacion(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│              AGENTE DE CAPACITACIÓN                         │
├─────────────────────────────────────────────────────────────┤
│  1. Evaluar necesidades                                     │
│  2. Planificar capacitación                                 │
│  3. Ejecutar capacitación                                   │
└─────────────────────────────────────────────────────────────┘
        """)
        opcion = input("Seleccione: ").strip()
        contexto = {"accion": ""}

        if opcion == "1":
            contexto["accion"] = "evaluar"
            roles = input("Roles (separados por coma): ").strip().split(",")
            contexto["roles"] = roles or ["general"]
        elif opcion == "2":
            contexto["accion"] = "planificar"
            contexto["programa"] = input("Programa: ").strip()
        elif opcion == "3":
            contexto["accion"] = "ejecutar"
            contexto["programa"] = input("Programa: ").strip()

        resultado = self.coordinador.ejecutar_agente(TipoAgente.CAPACITACION, contexto)
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def _agente_proveedores(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│             AGENTE DE PROVEEDORES                            │
├─────────────────────────────────────────────────────────────┤
│  1. Evaluar proveedor                                       │
│  2. Proceso de contratación                                │
│  3. Monitorear proveedor                                    │
└─────────────────────────────────────────────────────────────┘
        """)
        opcion = input("Seleccione: ").strip()
        contexto = {"accion": ""}

        if opcion == "1":
            contexto["accion"] = "evaluar"
            contexto["proveedor"] = input("Nombre del proveedor: ").strip()
            contexto["criticidad"] = (
                input("Criticidad (alta/media/baja): ").strip() or "media"
            )
        elif opcion == "2":
            contexto["accion"] = "contratar"
            contexto["proveedor"] = input("Nombre del proveedor: ").strip()
        elif opcion == "3":
            contexto["accion"] = "monitorear"
            contexto["proveedor"] = input("Nombre del proveedor: ").strip()

        resultado = self.coordinador.ejecutar_agente(TipoAgente.PROVEEDORES, contexto)
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def _agente_politicas(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│               AGENTE DE POLÍTICAS                           │
├─────────────────────────────────────────────────────────────┤
│  1. Gestionar política                                      │
│  2. Actualizar política                                     │
│  3. Difundir política                                       │
└─────────────────────────────────────────────────────────────┘
        """)
        opcion = input("Seleccione: ").strip()
        contexto = {"accion": ""}

        if opcion == "1":
            contexto["accion"] = "gestionar"
            contexto["politica"] = input(
                "Política (sgsi/contrasenas/uso_acceptable): "
            ).strip()
        elif opcion == "2":
            contexto["accion"] = "actualizar"
            contexto["politica"] = input("Política: ").strip()
            contexto["motivo"] = input("Motivo: ").strip()
        elif opcion == "3":
            contexto["accion"] = "diffundir"
            contexto["politica"] = input("Política: ").strip()
            contexto["audiencia"] = input("Audiencia: ").strip() or "general"

        resultado = self.coordinador.ejecutar_agente(TipoAgente.POLITICAS, contexto)
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def menu_mejora(self):
        while True:
            print("""
┌─────────────────────────────────────────────────────────────┐
│                MEJORA DE PROCESOS SGSI                      │
├─────────────────────────────────────────────────────────────┤
│  1. Ver procesos del SGSI                                   │
│  2. Identificar mejora                                      │
│  3. Planificar mejora                                       │
│  4. Estado del SGSI                                        │
│  5. Plan anual de mejora                                    │
│  0. Volver al menú principal                               │
└─────────────────────────────────────────────────────────────┘
            """)

            opcion = input("Seleccione opción: ").strip()

            if opcion == "1":
                self._ver_procesos()
            elif opcion == "2":
                self._identificar_mejora()
            elif opcion == "3":
                self._planificar_mejora()
            elif opcion == "4":
                self._estado_sgsi()
            elif opcion == "5":
                self._plan_anual()
            elif opcion == "0":
                break
            else:
                print("❌ Opción inválida")

    def _ver_procesos(self):
        procesos = self.motor_mejora.gestor_procesos.get_dashboard_procesos()
        print(f"\n{json.dumps(procesos, indent=2, ensure_ascii=False)}")

    def _identificar_mejora(self):
        titulo = input("Título de la mejora: ").strip()
        descripcion = input("Descripción: ").strip()
        proceso_origen = input("Proceso origen: ").strip()

        resultado = self.motor_mejora.gestor_mejoras.identificar_mejora(
            {
                "titulo": titulo,
                "descripcion": descripcion,
                "proceso_origen": proceso_origen,
                "tipo": "preventiva",
                "impacto": "alto",
                "urgencia": "media",
            }
        )
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def _planificar_mejora(self):
        mejora_id = input("ID de mejora: ").strip()
        resultado = self.motor_mejora.gestor_mejoras.planificar_implementacion(
            mejora_id, {}
        )
        print(f"\n{json.dumps(resultado, indent=2, ensure_ascii=False)}")

    def _estado_sgsi(self):
        estado = self.motor_mejora.get_estado_sgsi()
        print(f"\n{json.dumps(estado, indent=2, ensure_ascii=False)}")

    def _plan_anual(self):
        plan = self.motor_mejora.generar_plan_mejora_anual()
        print(f"\n{json.dumps(plan, indent=2, ensure_ascii=False)}")

    def _dashboard_general(self):
        dashboard = self.coordinador.get_dashboard()
        print(f"\n{json.dumps(dashboard, indent=2, ensure_ascii=False)}")

    def _configuracion(self):
        print("""
┌─────────────────────────────────────────────────────────────┐
│                     CONFIGURACIÓN                            │
├─────────────────────────────────────────────────────────────┤
│  1. Exportar métricas (JSON)                                │
│  2. Exportar criterios (JSON)                              │
│  3. Ver templates de métricas                               │
│  0. Volver al menú principal                               │
└─────────────────────────────────────────────────────────────┘
        """)

        opcion = input("Seleccione: ").strip()

        if opcion == "1":
            print(TemplatesMetricas.get_template_json())
        elif opcion == "2":
            print(self.gestor_criterios.get_all_criterios_json())
        elif opcion == "3":
            self._listar_metricas()

    def iniciar(self):
        self.mostrar_banner()

        while self.ejecutando:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.menu_metricas()
            elif opcion == "2":
                self.menu_criterios()
            elif opcion == "3":
                self.menu_agentes()
            elif opcion == "4":
                self.menu_mejora()
            elif opcion == "5":
                self._dashboard_general()
            elif opcion == "6":
                self._configuracion()
            elif opcion == "0":
                print("\n¡Gracias por usar el Sistema Multiagente ISO 27001!")
                self.ejecutando = False
            else:
                print("❌ Opción inválida")


def main():
    menu = MenuPrincipal()
    menu.iniciar()


if __name__ == "__main__":
    main()
