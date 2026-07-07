# Página Web Institucional - Fundación

Este es el repositorio oficial de la plataforma web de la fundación, un proyecto desarrollado con el framework **Django (Python)** y diseñado para dar visibilidad a las iniciativas de paz, cartografía social y memoria histórica en los territorios.

La plataforma permite la difusión de publicaciones institucionales, artículos de investigación y la integración de contenido multimedia para conectar de manera transparente con comunidades, académicos y aliados estratégicos.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.x & Django Framework
* **Base de Datos:** SQLite (Entorno de producción ligero)
* **Frontend:** HTML5, CSS3, Bootstrap (Diseño responsivo y adaptabilidad móvil)
* **Servidor de Producción:** Gunicorn
* **Plataforma de Despliegue:** Render (Alojamiento en la nube)
* **Gestión de Dominios:** Namecheap

---

## 🚀 Características del Proyecto

* **Gestión de Contenidos:** Panel de administración dinámico para la carga y actualización de publicaciones institucionales.
* **Multimedia Integrado:** Soporte nativo para la visualización de material audiovisual e incrustaciones de plataformas externas (YouTube).
* **Arquitectura Modular:** Estructura limpia dividida en aplicaciones independientes (`publicaciones`, `pagina_fundacion`) para facilitar el mantenimiento y escalabilidad del código.
* **Optimización para Producción:** Configuración segura de variables de entorno, manejo eficiente de archivos estáticos (`collectstatic`) y restricción de accesos mediante hosts autorizados (`ALLOWED_HOSTS`).

---

## 💻 Configuración Local y Despliegue

### Requisitos Previos
Es necesario contar con Python y Git instalados en el sistema local.

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/kikeconk/pagina_fundacion.git](https://github.com/kikeconk/pagina_fundacion.git)
