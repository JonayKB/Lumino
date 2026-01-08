---
icon: lucide/code
title: Implementación
---

!!! abstract "Resumen"
    Este documento describe cómo se implementa **Lumino**, incluyendo la estructura del código, las herramientas utilizadas, la configuración del entorno y las convenciones seguidas durante el desarrollo.

---

## Estructura del código

!!! info "Enfoque general"
    Lumino utiliza una arquitectura modular basada en aplicaciones Django independientes, lo que permite separar responsabilidades y reducir el acoplamiento entre componentes.

<div class="grid cards" markdown>

-    :lucide-folder: **Aplicaciones Django**  
  
     ---

     Cada funcionalidad principal vive en su propia app (`accounts`, `subjects`, `users`, etc.).

-    :lucide-layout-template: **Componentes reutilizables**  
  
     ---

     Elementos visuales y lógicos reutilizados para evitar duplicaciones.

-    :lucide-database: **Capa de datos**  
  
     ---

     Modelos Django responsables de la persistencia y validación de la información.

</div>

??? note "Ejemplo de estructura de carpetas"
    ```
    lumino/
    ├── .env
    ├── .gitignore
    ├── .pypas.toml
    ├── .venv/
    ├── accounts/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── locale/
    │   ├── migrations/
    │   ├── models.py
    │   ├── signals.py
    │   ├── templates/
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── docs/
    │   └── README.pdf
    ├── factories/
    │   ├── __init__.py
    │   ├── auth.py
    │   ├── extras.py
    │   ├── subjects.py
    │   └── users.py
    ├── fixtures/
    │   ├── auth.json
    │   ├── subjects.json
    │   └── users.json
    ├── justfile
    ├── main/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── media/
    │   ├── avatars/
    │   ├── cache/
    │   └── certificates/
    ├── node_modules/
    ├── package-lock.json
    ├── package.json
    ├── pyproject.toml
    ├── pytest.ini
    ├── shared/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── decorators.py
    │   ├── locale/
    │   ├── migrations/
    │   ├── models.py
    │   ├── static/
    │   ├── templates/
    │   ├── templatetags/
    │   ├── tests.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    ├── subjects/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── context_processors.py
    │   ├── converters.py
    │   ├── forms.py
    │   ├── locale/
    │   ├── management/
    │   ├── migrations/
    │   ├── models.py
    │   ├── tasks.py
    │   ├── templates/
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   └── widgets.py
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
    ├── users/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── converters.py
    │   ├── forms.py
    │   ├── locale/
    │   ├── migrations/
    │   ├── models.py
    │   ├── templates/
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── uv.lock
    ```

---

## Componentes reutilizables

!!! tip "Buenas prácticas aplicadas"
    Todo elemento que se utiliza más de una vez se implementa como **componente reutilizable**, ya sea visual (templates) o lógico (helpers, servicios).

??? question "¿Por qué usar componentes?"
    - Reduce código duplicado  
    - Facilita el mantenimiento  
    - Asegura coherencia visual y funcional  

!!! example "Ejemplos de componentes"
    - Tarjetas de módulos  
    - Formularios reutilizables  
    - Mensajes de estado (éxito, error, aviso)  

---

## Herramientas y tecnologías

!!! success "Stack tecnológico"
    El proyecto utiliza herramientas modernas y estables para garantizar fiabilidad y escalabilidad.

<div class="grid cards" markdown>

-    :lucide-server: **Django 5.2**  
  
     ---

     Framework principal del backend.

-    :lucide-image: **Pillow / sorl-thumbnail** 
   
     ---

     Gestión de imágenes y avatares.

-    :lucide-file-text: **WeasyPrint**  
  
     ---

     Generación de certificados PDF.

-    :lucide-clock: **django-rq**  
  
     ---

     Procesamiento de tareas en segundo plano.

</div>

!!! info "Dependencias principales"
    Todas las dependencias se gestionan mediante **uv**, asegurando versiones reproducibles y controladas.

---

## Configuración del entorno

!!! warning "Uso obligatorio de variables de entorno"
    Ninguna credencial sensible se almacena directamente en el código fuente.

???+ success "Archivo .env requerido"
    Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

    ```env
    EMAIL_HOST="correo_de_tu_host@correo.es"
    EMAIL_PORT=tu_puerto
    EMAIL_HOST_USER="tu_correo@tucorreo.es"
    EMAIL_HOST_PASSWORD="tu_contrania"
    DEFAULT_FROM_EMAIL="tu_correo_para_responder@tucorreo.es"
    ```

!!! danger "Seguridad"
    El archivo `.env` **nunca debe subirse a GitHub**.  
    Asegúrate de incluirlo en `.gitignore`.

---

## Control de versiones

!!! info "Gestión del código"
    El proyecto utiliza **Git** como sistema de control de versiones y **GitHub** como plataforma de colaboración.

<div class="grid cards" markdown>

-    :lucide-git-branch: **Ramas**  
  
     ---

     Uso de ramas para nuevas funcionalidades y correcciones.

-    :lucide-github: **Repositorio remoto**  
  
     ---

     Centraliza el código y permite revisiones mediante Pull Requests.

</div>

!!! tip "Convención recomendada"
    - `main`: versión estable  
    - `feature/*`: nuevas funcionalidades  
    - `fix/*`: corrección de errores  

---

## Convenciones del proyecto

!!! success "Estándares aplicados"
    Mantener convenciones claras mejora la legibilidad y reduce errores.

??? note "Convenciones principales"
    - Nombres descriptivos en inglés  
    - Separación clara entre lógica y presentación  
    - Uso de Markdown enriquecido para documentación  
    - Código comentado solo cuando aporta valor  

!!! bug "Errores evitados"
    Estas convenciones ayudan a prevenir:

    - Código duplicado  
    - Dependencias circulares  
    - Plantillas difíciles de mantener  

---

## Flujo de desarrollo

!!! quote "Filosofía del proyecto"
    *“Un código claro es más valioso que un código ingenioso.”*

!!! info "Ciclo típico"
    1. Crear rama  
    2. Implementar usando componentes  
    3. Probar localmente  
    4. Subir cambios  
    5. Revisar y fusionar  

---

## Conclusión

!!! success "Resultado"
    La implementación de Lumino prioriza **claridad, reutilización, seguridad y mantenibilidad**, permitiendo que el proyecto evolucione sin complejidad innecesaria.
