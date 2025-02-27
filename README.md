# Proyecto de Procesamiento de Archivos

Este proyecto procesa archivos de Excel que contienen datos de estudiantes y pruebas. La aplicación marca las pruebas pendientes para cada estudiante y genera archivos de salida por grado.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- Pandas
- Streamlit (si lo estás usando para la interfaz)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone <URL-del-repositorio>
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:
    - En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Para ejecutar el script principal, utiliza:

```bash
python src/main.py
