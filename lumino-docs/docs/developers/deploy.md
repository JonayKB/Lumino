---
icon: lucide/server
title: Despliegue
---

!!! abstract "Resumen"
    Este documento describe el procedimiento para publicar **Lumino** en un entorno de producción y el despliegue de la documentación mediante **Zensical** usando **GitHub Pages**.

---

## Entorno de producción

!!! info "Descripción general"
    El entorno de producción es el conjunto de servidores, servicios y configuraciones donde la aplicación funciona para los usuarios finales.

<div class="grid cards" markdown>

-    :lucide-cloud: **Servidor de aplicación**
    
     ---

     Ejecuta Django y gestiona las peticiones HTTP.

-    :lucide-database: **Base de datos**  
  
     ---

     Almacena usuarios, módulos y calificaciones.

-    :lucide-mail: **Servidor de correo**  

     ---

     Envía notificaciones y certificados PDF.

</div>

!!! note "Requisitos mínimos del servidor"
    - Sistema Linux  
    - Python ≥ 3.14  
    - Acceso a base de datos  
    - Dominio o IP pública  

---

## Preparación para el despliegue

!!! warning "Antes de publicar"
    Asegúrate de que el proyecto ha sido probado y configurado correctamente.

???+ tip "Checklist previa"
    - Variables de entorno configuradas  
    - Migraciones aplicadas  
    - Archivos estáticos recopilados  
    - Certificados PDF funcionando  

!!! example "Variables de entorno"
    ```env
    EMAIL_HOST="correo_de_tu_host@correo.es"
    EMAIL_PORT=tu_puerto
    EMAIL_HOST_USER="tu_correo@tucorreo.es"
    EMAIL_HOST_PASSWORD="tu_contrania"
    DEFAULT_FROM_EMAIL="tu_correo_para_responder@tucorreo.es"
    ```

---

## Procedimiento de despliegue del software

!!! success "Flujo recomendado"
    El despliegue sigue un proceso ordenado para minimizar errores.

??? question "Pasos principales"
    1. Clonar el repositorio en el servidor  
    2. Crear entorno virtual  
    3. Instalar dependencias  
    4. Configurar variables de entorno  
    5. Ejecutar migraciones  
    6. Iniciar el servidor  

???+ example "Ejemplo de comandos"
    ```bash
    git clone https://github.com/JonayKB/Lumino
    cd lumino
    uv sync
    python manage.py migrate
    python manage.py collectstatic
    python manage.py runserver
    ```

!!! danger "Producción real"
    En producción se debe usar un servidor WSGI (como Gunicorn) y un proxy inverso (como Nginx).  
    `runserver` **solo es válido para desarrollo**.

---

## Gestión de errores en producción

!!! failure "Posibles problemas"
    - Errores de migración  
    - Fallos de conexión al correo  
    - Archivos estáticos no visibles  

??? tip "Buenas prácticas"
    - Revisar logs del servidor  
    - Probar en entorno de staging  
    - Mantener copias de seguridad  

---

## Despliegue de la documentación con Zensical

!!! info "Documentación accesible"
    La documentación de Lumino se genera con **Zensical** y se publica automáticamente en **GitHub Pages**.

<div class="grid cards" markdown>

-    :lucide-book-open: **Zensical**  

     ---

     Generador de documentación estática.

-    :lucide-github: **GitHub Pages**  

     ---
     
     Servicio gratuito de hosting estático.

</div>

---

## Procedimiento de despliegue en GitHub Pages

!!! success "Publicación automática"
    GitHub Pages permite desplegar la documentación directamente desde el repositorio.

???+ example "Pasos básicos"
    1. Configurar el repositorio en GitHub  
    2. Activar GitHub Pages  
    3. Seleccionar la rama de despliegue  
    4. Construir la documentación  

??? example "Comando de construcción"
    ```bash
    zensical build
    ```

!!! note "Resultado"
    Tras el despliegue, la documentación estará disponible en una URL pública, por ejemplo:  
    `https://usuario.github.io/lumino-docs/`

---

## Automatización del despliegue

!!! tip "CI/CD recomendado"
    Se recomienda usar **GitHub Actions** para automatizar la construcción y publicación de la documentación.

??? question "¿Por qué automatizar?"
    - Evita errores manuales  
    - Garantiza documentación actualizada  
    - Reduce tiempo de despliegue  

---

## Seguridad y mantenimiento

!!! warning "Aspectos críticos"
    - No exponer claves en repositorios  
    - Actualizar dependencias regularmente  
    - Supervisar el estado del servidor  

!!! quote "Principio clave"
    *“Un buen despliegue es aquel que los usuarios no notan.”*

---

!!! success "Conclusión"
    Un despliegue bien definido garantiza estabilidad del sistema y acceso continuo a la documentación, facilitando el uso y mantenimiento de Lumino.
