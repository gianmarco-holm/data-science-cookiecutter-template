import subprocess
import os
import sys
import platform

MESSAGE_COLOR = "\x1b[34m"
ERROR_COLOR = "\x1b[31m"
RESET_ALL = "\x1b[0m"

# Obtener la URL del repositorio desde Cookiecutter
repository_url = "{{cookiecutter.repository_url}}"

# Función para verificar si Conda está instalado
def is_conda_installed():
    try:
        subprocess.check_output(["conda", "--version"])
        return True
    except subprocess.CalledProcessError:
        return False

# Función para verificar si Conda está activo
def is_conda_active():
    # Verifica si el entorno de Conda está activo revisando las variables de entorno
    return 'CONDA_DEFAULT_ENV' in os.environ

# Función para verificar si venv está activo
def is_venv_active():
    # Verifica si el entorno venv está activo revisando la variable de entorno VIRTUAL_ENV
    return 'VIRTUAL_ENV' in os.environ

# Función para crear un entorno Conda
def create_conda_env():
    print(f"{MESSAGE_COLOR}Conda está instalado. Creando un entorno Conda...{RESET_ALL}")
    subprocess.call(["conda", "create", "--name", "myenv", "--file", "environment.yml", "--yes"])

# Función para crear un entorno venv
def create_venv():
    print(f"{MESSAGE_COLOR}Conda no encontrado. Creando un entorno Python venv...{RESET_ALL}")
    subprocess.call(["python", "-m", "venv", "venv"])

# Función para instalar dependencias usando Conda
def install_conda_dependencies():
    print(f"{MESSAGE_COLOR}Instalando dependencias usando Conda...{RESET_ALL}")
    subprocess.call(["conda", "env", "update", "--file", "environment.yml", "--prune"])

# Función para instalar dependencias usando venv
def install_venv_dependencies():
    print(f"{MESSAGE_COLOR}Instalando dependencias usando pip (desde requirements.txt)...{RESET_ALL}")
    subprocess.call(["pip", "install", "-r", "requirements.txt"])

# Función para activar el entorno Conda
def activate_conda_env():
    print(f"{MESSAGE_COLOR}Activando el entorno Conda...{RESET_ALL}")
    subprocess.call(["conda", "activate", "myenv"])

# Función para activar el entorno venv
def activate_venv():
    print(f"{MESSAGE_COLOR}Activando el entorno venv...{RESET_ALL}")
    if platform.system() == "Windows":
        subprocess.call([os.path.join("venv", "Scripts", "activate.bat")], shell=True)
    else:
        subprocess.call(["source", os.path.join("venv", "bin", "activate")], shell=True)

# Función para manejar la instalación de dependencias en el entorno activo
def install_dependencies():
    if is_conda_active():  # Si Conda está activo
        print(f"{MESSAGE_COLOR}El entorno Conda está activo. Instalando dependencias...{RESET_ALL}")
        install_conda_dependencies()
    elif is_venv_active():  # Si venv está activo
        print(f"{MESSAGE_COLOR}El entorno Python venv está activo. Instalando dependencias...{RESET_ALL}")
        install_venv_dependencies()
    else:  # Si no hay entorno activo, se crea uno
        if is_conda_installed():  # Si Conda está instalado
            create_conda_env()
            activate_conda_env()
            install_conda_dependencies()
        else:  # Si Conda no está instalado, se crea venv
            create_venv()
            activate_venv()
            install_venv_dependencies()

# Función para inicializar git
def init_git():
    print(f"{MESSAGE_COLOR}¡Casi listo!")
    print(f"Inicializando un repositorio git...{RESET_ALL}")

    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', 'README.md'])
    subprocess.call(['git', 'commit', '-m', 'primer commit'])
    subprocess.call(['git', 'branch', '-M', 'main'])
    
    # Usar la URL del repositorio desde la variable de entorno
    if repository_url:
        subprocess.call(['git', 'remote', 'add', 'origin', repository_url])
        subprocess.call(['git', 'push', '-u', 'origin', 'main'])
        print(f"{MESSAGE_COLOR}Repositorio git inicializado y subido a {repository_url}{RESET_ALL}")
    else:
        print(f"{ERROR_COLOR}ERROR: repository_url no proporcionada en la plantilla.{RESET_ALL}")

# Ejecutar la configuración del entorno, la instalación de dependencias y la inicialización de Git
install_dependencies()
init_git()

print(f"{MESSAGE_COLOR}¡El comienzo de tu destino está definido ahora! ¡Crea y diviértete!{RESET_ALL}")
