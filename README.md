# Line Counter Script

## Description
This script is designed to count the number of lines of code in a project directory. It recursively traverses through all subdirectories and files, summing up the total number of lines.

## How to Use

### Prerequisites
- Python 3.x

### Installation
Clone this repository or download the `count_lines.py` script.

### Usage
Navigate to the directory where `count_lines.py` is located and run the following command:

```sh
python3 count_lines.py /path/to/project/directory
```

### Example
If your project directory is located at `/home/user/my_project`, run:

```sh
python3 count_lines.py /home/user/my_project
```

This will output the total number of lines of code in the project.

## Code Explanation
The script uses the `os` module to navigate directories and the `argparse` module to handle command-line arguments.

- **count_lines_in_file(file_path)**: This function opens a file and counts the number of lines in it.
- **count_lines_in_directory(directory)**: This function traverses all files and subdirectories, summing up the number of lines in each file.
- **main()**: This function handles the command-line arguments and calls the counting functions. It also checks if the provided directory is valid.

## Author
Jorge Salgado Miranda

---

# Script de Contador de Líneas

## Descripción
Este script está diseñado para contar la cantidad de líneas de código en un directorio de proyecto. Recorre recursivamente todos los subdirectorios y archivos, sumando el número total de líneas.

## Cómo Usar

### Requisitos
- Python 3.x

### Instalación
Clona este repositorio o descarga el script `count_lines.py`.

### Uso
Navega al directorio donde se encuentra `count_lines.py` y ejecuta el siguiente comando:

```sh
python3 count_lines.py /ruta/al/directorio/proyecto
```

### Ejemplo
Si tu directorio de proyecto está ubicado en `/home/usuario/mi_proyecto`, ejecuta:

```sh
python3 count_lines.py /home/usuario/mi_proyecto
```

Esto mostrará el número total de líneas de código en el proyecto.

## Explicación del Código
El script utiliza el módulo `os` para navegar por los directorios y el módulo `argparse` para manejar los argumentos de la línea de comandos.

- **count_lines_in_file(file_path)**: Esta función abre un archivo y cuenta el número de líneas en él.
- **count_lines_in_directory(directory)**: Esta función recorre todos los archivos y subdirectorios, sumando el número de líneas en cada archivo.
- **main()**: Esta función maneja los argumentos de la línea de comandos y llama a las funciones de conteo. También verifica si el directorio proporcionado es válido.

## Autor
Jorge Salgado Miranda
