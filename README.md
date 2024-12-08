# Plantilla de Cookiecutter para Proyectos de Ciencia de Datos

[![Cookiecutter Template](https://img.shields.io/badge/Cookiecutter-Template-blue)](https://github.com/cookiecutter/cookiecutter)

¡Bienvenido! Esta es una plantilla para iniciar proyectos de ciencia de datos utilizando [Cookiecutter](https://cookiecutter.readthedocs.io/). Incluye una estructura básica y configuraciones necesarias para agilizar el desarrollo.

---

## 📁 Estructura del Proyecto

El proyecto generado tendrá la siguiente estructura:

```plaintext
project_name/
├── README.md            # Descripción del proyecto
├── environment.yml      # Dependencias para Conda
├── requirements.txt     # Dependencias para pip
├── data/                # Carpeta para los datos crudos y procesados
│   ├── raw/             # Datos crudos
│   └── processed/       # Datos procesados
├── models/              # Modelos entrenados (archivos .pkl, .h5, etc.)
├── notebooks/           # Jupyter notebooks para análisis y experimentación
├── reports/             # Visualizaciones y reportes generados
├── src/
│   ├── data/            # Scripts para gestión y procesamiento de datos
│   ├── models/          # Scripts para entrenamiento y evaluación de modelos
│   ├── utils/           # Funciones auxiliares
├── tests/               # Pruebas del proyecto
├── .gitignore           # Archivos y carpetas ignorados por git
└── LICENSE              # Licencia del proyecto
```

---

## 🚀 Cómo Usar Esta Plantilla
Sigue estos pasos para utilizar esta plantilla en tu próximo proyecto:

### 1. Instalar Cookiecutter

Asegúrate de tener instalado Cookiecutter:
```sh
pip install cookiecutter
```

### 2. Generar un Nuevo Proyecto

Ejecuta el siguiente comando para generar un proyecto basado en esta plantilla:
```sh
cookiecutter https://github.com/gianmarco-holm/data-science-cookiecutter-template.git
```

### 3. Configuración Inicial

Durante la configuración, se te pedirá ingresar información como:

* **"project_name":** "Predicción de ventas",
* **"project_slug":** "prediccion-de-ventas",
* **"project_short_description":** "Un sistema de predicción de ventas que utiliza machine learning para estimar el rendimiento mensual de una tienda minorista.",
* **"problem_statement":** "Las empresas minoristas necesitan predecir las ventas futuras para optimizar el inventario y los recursos. Este proyecto busca desarrollar un modelo predictivo basado en datos históricos de ventas y variables externas, como tendencias de mercado y estacionalidad.",
* **"repository_url":** "https://github.com/usuario/prediccion-de-ventas",
* **"year":** "2024",
* **"author_name":** "Gianmarco Holm",
* **"contact_email":** "gianmarco.holgado@gmail.com",
* **"author_linkedin":** "https://www.linkedin.com/in/gianmarco-holm/",
* **"install_mode":** ["Minimal", "All"],
* **"python_version":** ["3.12", "3.11", "3.10", "3.9", "3.8"]
    
### 4. Configurar el Entorno Virtual

El script post_gen_project.py configurará automáticamente tu entorno virtual. El flujo es el siguiente:

* Si hay un entorno Conda activo, instalará las dependencias de environment.yml.
* Si hay un entorno venv activo, instalará las dependencias de requirements.txt.
* Si no hay ningún entorno activo:
    * Si Conda está instalado, creará y activará un entorno Conda, e instalará las dependencias.
    * Si Conda no está disponible, creará y activará un entorno venv, e instalará las dependencias.

> Se recomienda no tener creado el entorno y tener instalado conda.

### 5. Inicializar Git

Si proporcionaste la URL de un repositorio remoto, el script inicializará un repositorio Git local, hará un primer commit y subirá los cambios al remoto, si el repositorio es invalido quedará como pendiente en el README del proyecto.

> Se recomienda tener creado el repositorio de github

---

## 📦 Requisitos Previos

* Python 3.8+: Requerido para ejecutar los scripts.
* Conda (opcional): Recomendado para manejo de entornos.
* Git: Para control de versiones.

---

## 🛠 Personalización de la Plantilla

Puedes ajustar la plantilla para que se adapte a tus necesidades:

* Modificar o agregar carpetas en la estructura.
* Actualizar los archivos de dependencias (environment.yml y requirements.txt).
* Personalizar los scripts de configuración (pre_gen_project.py y post_gen_project.py).

---

## 🧑‍💻 Autor

Creado por [Gianmarco Holm](https://www.linkedin.com/in/gianmarco-holm/).

¿Tienes preguntas o sugerencias? ¡Abre un issue en este repositorio!

---

¡Gracias por usar esta plantilla! 🎉