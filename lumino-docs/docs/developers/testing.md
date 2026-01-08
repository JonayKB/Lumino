---
icon: lucide/test-tube
title: Testing
---

!!! abstract "Resumen"
    Este documento describe cómo se gestiona el **testing en Lumino**, incluyendo la estructura de las pruebas, las estrategias aplicadas, las herramientas utilizadas, la configuración del entorno de test y las convenciones seguidas para garantizar calidad, estabilidad y mantenibilidad del proyecto.

---

## Estructura del código de testing

!!! info "Enfoque general"
    Lumino utiliza una estrategia de **testing centralizado con pytest**, complementada por pruebas locales en cada app cuando es necesario. Esto permite mantener una visión global del sistema sin perder granularidad.

<div class="grid cards" markdown>

*    :lucide-folder-check: **Tests centralizados**

     ---

     La mayoría de pruebas viven en la carpeta `tests/`, organizadas por dominio funcional.

*    :lucide-layers: **Cobertura por capas**

     ---

     Se prueban modelos, vistas, formularios, señales y comandos de gestión.

*    :lucide-puzzle: **Reutilización de fixtures**

     ---

     Fixtures compartidas para evitar duplicación y mejorar consistencia.

</div>

??? note "Ejemplo de estructura de carpetas de testing"
    ```
    lumino/
    ├── pytest.ini
    ├── factories/
    │   ├── auth.py
    │   ├── extras.py
    │   ├── subjects.py
    │   └── users.py
    ├── fixtures/
    │   ├── auth.json
    │   ├── subjects.json
    │   └── users.json
    ├── tests/
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── test_accounts.py
    │   ├── test_admin.py
    │   ├── test_context_processors.py
    │   ├── test_core.py
    │   ├── test_design.py
    │   ├── test_management_commands.py
    │   ├── test_shared.py
    │   ├── test_signals.py
    │   ├── test_subjects.py
    │   └── test_users.py
    ```

---

## Estrategia de testing

!!! tip "Estrategia aplicada"
    Lumino sigue una **pirámide de testing**, priorizando pruebas rápidas, deterministas y fáciles de mantener.

<div class="grid cards" markdown>

*    :lucide-box: **Tests unitarios**

     ---

     Validan lógica aislada: modelos, formularios, utilidades, converters y decoradores.

*    :lucide-link: **Tests de integración**

     ---

     Verifican interacción entre componentes: vistas + URLs + permisos + templates.

*    :lucide-route: **Tests funcionales**

     ---

     Cubren flujos críticos de usuario sin necesidad de navegador real.

</div>

!!! note "Criterios clave"
       - No depender de servicios externos
       - Usar base de datos de test aislada
       - Ejecutarse en menos de unos segundos

---

## Casos de prueba cubiertos

!!! success "Cobertura funcional"
    Los tests están orientados a **comportamientos**, no a implementación interna.

??? note "Ejemplos de casos de prueba"
       - Creación y validación de usuarios
       - Permisos y roles de acceso
       - Formularios válidos e inválidos
       - Renderizado correcto de vistas
       - Ejecución de signals
       - Context processors
       - Management commands
       - Tareas asíncronas (nivel lógico)

!!! bug "Errores que se previenen"
       - Regresiones funcionales
       - Cambios de permisos no detectados
       - Formularios inconsistentes
       - Señales ejecutadas múltiples veces

---

## Herramientas y tecnologías de testing

!!! success "Stack de testing"
    El proyecto utiliza herramientas estándar y robustas del ecosistema Python y Django.

<div class="grid cards" markdown>

*    :lucide-check-circle: **pytest**

     ---

     Framework principal de testing.

*    :lucide-database: **pytest-django**

     ---

     Integración con Django y base de datos de test.

*    :lucide-factory: **factory_boy**

     ---

     Generación de datos de prueba coherentes.

*    :lucide-file-json: **Fixtures JSON**

     ---

     Carga de datos realistas para escenarios complejos.

</div>

---

## Configuración del entorno de testing

!!! info "Configuración centralizada"
    Toda la configuración de testing se centraliza en `pytest.ini`.

???+ success "Configuración mínima requerida"
    ```
    [pytest]
    DJANGO_SETTINGS_MODULE = main.settings
    python_files = test_*.py
    addopts = --reuse-db
    ```

!!! warning "Buenas prácticas"
       - Nunca usar la base de datos real
       - No depender de `.env` productivo
       - Tests reproducibles en cualquier entorno

---

## Automatización de tests

!!! info "Ejecución automatizada"
    Los tests están pensados para ejecutarse de forma **local y automatizada**.

<div class="grid cards" markdown>

*    :lucide-terminal: **Ejecución local**

     ---

    ```
    pytest
    ```

*    :lucide-refresh-cw: **Ejecución frecuente**

     ---

     Tests ejecutados antes de cada commit relevante.

</div>

!!! tip "Recomendación"
    Integrar pytest en CI (GitHub Actions o similar) para validación automática en Pull Requests.

---

## Convenciones del proyecto en testing

!!! success "Estándares aplicados"
    Las pruebas siguen convenciones claras para facilitar lectura y mantenimiento.

??? note "Convenciones principales"
       - Nombres de test descriptivos (`test_user_cannot_access_private_view`)
       - Un comportamiento por test
       - Uso extensivo de fixtures
       - Evitar lógica compleja dentro del test
       - No testear implementación interna

!!! bug "Antipatrones evitados"
       - Tests frágiles
       - Dependencias entre tests
       - Uso excesivo de mocks
       - Asserts múltiples no relacionados

---

## Flujo de testing

!!! quote "Principio guía"
    *“Si no está probado, no existe.”*

!!! info "Ciclo típico"
       1. Implementar funcionalidad
       2. Escribir o actualizar tests
       3. Ejecutar pytest localmente
       4. Revisar cobertura y fallos
       5. Subir cambios

---

## Ciclo típico de TDD

!!! info "Definición"
    TDD es una técnica de desarrollo donde **los tests se escriben antes del código funcional**, y el desarrollo avanza **ciclos cortos de prueba y refactorización**.

---

!!! info "Ciclo normal"

     1. **Red (Rojo)** – Escribir un test que falle

        * Define un comportamiento o requisito nuevo
        * Ejecutar el test para confirmar que **falla**, asegurando que el test es válido
        * Ejemplo: Test que verifica que un usuario no autenticado es redirigido al login

     2. **Green (Verde)** – Escribir el código mínimo que haga pasar el test

        * Implementar solo lo necesario para que el test pase
        * No optimizar ni añadir funcionalidades extra

     3. **Refactor (Refactorización)** – Mejorar el código

        * Limpiar duplicaciones y mejorar legibilidad
        * Mantener los tests pasando para asegurar que no se rompen los comportamientos

     4. **Repetir** – Iterar sobre nuevos tests

        * Cada nueva funcionalidad o caso de uso sigue el mismo ciclo: Red → Green → Refactor
        * Construye el sistema de manera incremental y segura

---

???+ tip "Resumen visual"

    ```mermaid
    flowchart TD
        A[Red: Write failing test] --> B[Green: Write minimal code to pass test]
        B --> C[Refactor: Clean up code while keeping tests green]
        C --> D[Repeat: Add new tests and iterate]
        D --> A
    ```

---

## Conclusión

!!! success "Resultado"
    El sistema de testing de Lumino garantiza **confianza en los cambios, detección temprana de errores y evolución segura del proyecto**, sin sacrificar velocidad de desarrollo ni claridad del código.

---