---
icon: lucide/list-check
title: Requisitos del proyecto
---

!!! success "Objetivo de este documento"
    Aquí se describen las especificaciones que definen el comportamiento, las limitaciones y el uso esperado del sistema **Lumino**, una plataforma de formación online.

---

## Requisitos funcionales

!!! success "¿Qué puede hacer el sistema?"
    Estas son las funcionalidades principales que Lumino debe ofrecer a sus usuarios.

<div class="grid cards" markdown>

-    :lucide-user: **Gestión de usuarios**  

     ---

     Registro, inicio de sesión y cierre de sesión de usuarios.  
     Diferenciación automática entre alumnado y profesorado.

-    :lucide-book-open: **Gestión de módulos**  

     ---

     Visualización de módulos disponibles y módulos matriculados según el rol del usuario.

-    :lucide-file-text: **Gestión de lecciones**  

     ---

     Creación, edición, visualización y eliminación de lecciones dentro de cada módulo.

-    :lucide-check-circle: **Matrícula y desmatrícula**  

     ---

     El alumnado puede matricularse y desmatricularse de módulos disponibles.

-    :lucide-award: **Calificaciones y certificados**  

     ---

     Asignación de notas por parte del profesorado y solicitud de certificados en PDF por parte del alumnado.

</div>

---

## Requisitos no funcionales

!!! success "Cómo debe comportarse el sistema"
    Estos requisitos definen la calidad, seguridad y usabilidad de la plataforma.

<div class="grid cards" markdown>

-    :lucide-zap: **Rendimiento**  

     ---

     El sistema debe responder de forma fluida incluso con múltiples usuarios conectados.

-    :lucide-lock: **Seguridad**  

     ---

     Acceso restringido mediante autenticación.  
     Protección de rutas según el rol del usuario.

-    :lucide-layout: **Usabilidad**  

     ---

     Interfaz clara, coherente y accesible para usuarios sin conocimientos técnicos.

-    :lucide-refresh-ccw: **Mantenibilidad**  

     ---

     Código organizado que permita añadir nuevas funcionalidades sin romper las existentes.

-    :lucide-globe: **Internacionalización**  

     ---

     Soporte para inglés y español sin modificar el idioma base del proyecto.

</div>

---

## Restricciones del sistema

!!! success "Limitaciones técnicas y de entorno"
    Estas condiciones deben cumplirse obligatoriamente para el correcto funcionamiento del proyecto.

<div class="grid cards" markdown>

-    :lucide-package: **Gestor de dependencias**  

     ---

     El proyecto utiliza **uv** como gestor de paquetes y entornos Python.

-    :lucide-code: **Versión de Python**  

     ---

     Se requiere **Python >= 3.14**.

-    :lucide-database: **Persistencia de datos**  

     ---

     El sistema depende de base de datos gestionada por Django ORM.

-    :lucide-server: **Servicios adicionales**  

     ---

     Uso obligatorio de Redis para tareas en segundo plano.

-    :lucide-shield-alert: **Configuraciones obligatorias**  

     ---

     No se permite modificar el idioma base (`LANGUAGE_CODE = 'en_us'`).

</div>

!!! info "Dependencias principales del proyecto"
    El proyecto Lumino depende, entre otras, de las siguientes librerías:
    
    - Django  
    - django-rq  
    - sorl-thumbnail  
    - weasyprint  
    - crispy-bootstrap5  

---

## Casos de uso del sistema

!!! success "Escenarios reales de uso"
    A continuación se describen situaciones habituales de interacción con la plataforma.

<div class="grid cards" markdown>

-    :lucide-log-in: **Acceso de un estudiante**  

     ---

     El estudiante inicia sesión, consulta sus módulos y accede a las lecciones disponibles.

-    :lucide-edit: **Gestión de contenidos por el profesorado**  

     ---

     El profesorado crea, edita o elimina lecciones dentro de un módulo que imparte.

-    :lucide-check-square: **Evaluación del alumnado**  

     ---

     El profesorado asigna calificaciones a los estudiantes matriculados.

-    :lucide-file-output: **Solicitud de certificado**  

     ---

     El estudiante solicita un certificado PDF con todas sus calificaciones aprobadas.

</div>

---

!!! success "Resumen"
    Estos requisitos garantizan que Lumino sea una plataforma educativa funcional, segura y fácil de usar, cumpliendo tanto las necesidades del alumnado como del profesorado.
