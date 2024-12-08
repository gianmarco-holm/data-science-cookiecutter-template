import os
import sys
import subprocess

# Variables obtenidas de cookiecutter
project_name = "{{cookiecutter.project_name}}"
project_short_description = "{{cookiecutter.project_short_description}}"
problem_statement = "{{cookiecutter.problem_statement}}"
author_name = "{{cookiecutter.author_name}}"
repository_url = "{{cookiecutter.repository_url}}"

# Colores para mostrar los mensajes
ERROR_COLOR = "\x1b[31m"  # Para cambiar el color a rojo
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

def validate_first_letter_uppercase(text, field_name):
    """Validar que el texto comience con mayúscula."""
    if not text:
        return False
    return text[0].isupper()

def check_repository_exists(repo_url):
    """Verificar si el repositorio ya existe en GitHub."""
    try:
        # Usamos git ls-remote para comprobar si el repositorio existe
        subprocess.check_output(['git', 'ls-remote', repo_url])
        return True
    except subprocess.CalledProcessError:
        return False

# Validación de cada campo
validations = {
    "project_name": project_name,
    "project_short_description": project_short_description,
    "problem_statement": problem_statement,
    "author_name": author_name
}

# Iterar sobre los campos y verificar que comiencen con mayúscula
for field, value in validations.items():
    if not validate_first_letter_uppercase(value, field):
        print(f"{ERROR_COLOR}ERROR: {field} debe comenzar con la primera letra en mayúscula.{RESET_ALL}")
        sys.exit(1)

# Verificación de existencia del repositorio
if repository_url:
    if not check_repository_exists(repository_url):
        print(f"{ERROR_COLOR}ADVERTENCIA: El repositorio {repository_url} no existe. Por favor, créalo sin README.{RESET_ALL}")
        sys.exit(1)
else:
    print(f"{ERROR_COLOR}ERROR: repository_url no proporcionada en la plantilla.{RESET_ALL}")
    sys.exit(1)

print(f"{MESSAGE_COLOR}¡Todo listo! Estás a punto de crear algo increíble.")
print(f"Creando el proyecto en {os.getcwd()}{RESET_ALL}")
