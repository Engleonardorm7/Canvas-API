import pandas as pd
from main import post, read
from groups_and_activities import codigos_guias, codigos_grupos, columnas

curso="10"
guia="B4/L2"
name_of_the_group="10th Gandhi"


group=codigos_grupos[curso]
class_guide=codigos_guias[curso][guia]
colum_class_guide =columnas[curso][guia]

"6Th Le Clezio"
"6Th Brown"
"6Th Mistral"
"7Th Nakamura"
"7Th Ebadi"
"8Th Borges"
"8Th Wiles"
"9Th Mandela"
"9Th Mutis"
"10Th Gavalda"
"10th Gandhi"
"11Th Gentry"
"11Th Clinton"
"11Th Brundtland"
# Cargar el archivo Excel
ruta_archivo  = 'Calificaciones 2022-2023.xlsx'

notas_excel = pd.read_excel(ruta_archivo, sheet_name=name_of_the_group)

# Diccionario para almacenar las notas de cada estudiante


#     # Iterar sobre cada fila de la tabla de calificaciones
for index, fila in notas_excel.iterrows():
    # Obtener el ID y nombre del estudiante
    
    ID_estudiante = fila[0]
    nombre_estudiante = fila[1]
    
    notas_estudiantes = {}
    Class_guide=fila[colum_class_guide]
    if Class_guide!=guia:
        Class_guide=round((Class_guide),1)
    
    print(Class_guide)
    if ID_estudiante not in notas_estudiantes:
        notas_estudiantes[ID_estudiante] = {}
    
    # Agregar la nota de Class_guide al diccionario de notas del estudiante
    notas_estudiantes[ID_estudiante] = Class_guide
    post(ID_estudiante,Class_guide, group, class_guide)
    #read(group, class_guide)

print("Grades submitted successfully!")



