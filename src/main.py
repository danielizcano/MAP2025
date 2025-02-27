import pandas as pd

# Ruta de entrada (archivo original) y salida (directorio donde se guardarán los archivos procesados)
input_file = '/Users/julopez/MAP2025/MAP_WINTER/PENDING_MAP_WINTER.xlsx'
output_folder = '/Users/julopez/MAP2025/MAP_WINTER_PENDING/'

# Leer el archivo de entrada con todas las hojas
df = pd.read_excel(input_file, sheet_name=None)

# Función para procesar los datos de una hoja de grado
def process_grade(sheet_name, data):
    """
    Procesa los datos de un grado específico, marcando las pruebas pendientes
    y generando un archivo de salida con los resultados.

    Parámetros:
    sheet_name (str): El nombre de la hoja (grado) a procesar (Ej: G5, G6, etc.).
    data (pd.DataFrame): Los datos de esa hoja.
    """
    # Definir las pruebas que estamos buscando
    tests = ['Reading', 'Math', 'Language', 'Spanish']
    
    # Crear un DataFrame con solo las columnas ID y Name (eliminando duplicados)
    students = data[['ID', 'Name']].drop_duplicates()

    # Inicializar las columnas para las pruebas con valores vacíos
    students[tests] = ''
    
    # Iterar sobre los datos y marcar las pruebas pendientes con "X"
    for _, row in data.iterrows():
        student_id = row['ID']
        test = row['Test']
        
        # Si la prueba está en la lista, marcar con "X"
        if test in tests:
            students.loc[students['ID'] == student_id, test] = 'X'
    
    # Añadir una columna que cuente el total de pruebas pendientes para cada estudiante
    students['Total Test Pending'] = students[tests].apply(lambda row: row.isna().sum(), axis=1)
    
    # Guardar el archivo procesado con el nombre adecuado en la carpeta de salida
    output_file = f"{output_folder}pending_{sheet_name}.xlsx"
    students.to_excel(output_file, index=False)
    print(f"Archivo procesado y guardado como: {output_file}")

# Elige la hoja que quieres procesar aquí (puedes cambiar G5 por la hoja que desees)
sheet_to_process = 'G5'  # Cambia 'G5' por la hoja que quieres procesar, por ejemplo: 'G8'

# Verifica si la hoja seleccionada existe y luego procesa solo esa hoja
if sheet_to_process in df:
    process_grade(sheet_to_process, df[sheet_to_process])
else:
    print(f"La hoja {sheet_to_process} no se encuentra en el archivo.")
