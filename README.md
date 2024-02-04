# TimelessEchoes

## Descripción del proyecto:

Este proyecto tiene como objetivo proporcionar a las personas una plataforma donde puedan llevar un diario personal. Cada entrada del diario puede contener un título, un párrafo principal. La aplicación permite a los usuarios ver, crear, editar y eliminar sus entradas.

## Enfoque y Metodología

### Maquetación del proyecto:

    https://miro.com/app/board/uXjVNxCLvyk=/?share_link_id=3048078825

### Tecnologías Utilizadas

- Python
- Flask
- SQLAlchemy
- HTML/CSS
- Javascript
- SQLite

### Implementación:

Desarrollo de la aplicación utilizando el marco web Flask para Python.
Integración de Flask-SQLAlchemy para la gestión de la base de datos.
Implementación de funciones CRUD (Crear, Leer, Actualizar, Eliminar).

### Despliegue:

Configuración del entorno virtual y del sistema de gestión de base de datos SQLite.
Despliegue de la aplicación en un entorno local.

### Estructura del proyecto:
    Timelessechoes/
    │
    ├── app.py
    ├── modelos.py
    ├── init_db.py
    ├── static/
    │   ├── images/
    │   │   ├── profile.jpg
    │   │   └── ... (otras imágenes)
    │   ├── styles/
    │   │   ├── style.css
    │   │   └── ... (otros estilos)
    │   └── ... (otros archivos estáticos)
    │
    ├── templates/
    │   ├── crear.html
    │   ├── editar.html
    │   ├── sign-up.html
    │   ├── login.html
    │   ├── landing-page.html
    │   └── index.html│   
    │
    ├── venv/ (entorno virtual)
    │
    ├── database.sqlite3 (base de datos SQLite)
    └── README.md



## Configuración del Proyecto

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/tuusuario/tuproyecto.git
   cd tuproyecto

2. **Configuracion del entorno virtual:**

python -m venv venv
source venv/bin/activate  **Linux / macOS**
# O
.\venv\Scripts\activate  **Windows**


3. **Instalar dependencias:**

Asegúrate de tener instaladas las siguientes dependencias en tu entorno virtual:

- Flask

    pip install Flask

- SQLalchemy

    pip install SQLalchemy

- Flask-SQLalchemy

    pip install Flask-SQLalchemy

- requests

    pip install requests


5. **Crear la base de datos**

    python init_db.py

4. **Ejecutar la aplicación en la terminal**
    python app.py


#### Credits

    Pictures credits to @wacca005 https://twitter.com/wacca005
