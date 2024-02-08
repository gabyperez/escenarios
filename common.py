def limpiar_frases(lista):
  frases_limpias = []
  for frase in lista:
    frase_limpia = agregar_punto_al_final(frase)
    frases_limpias.append(frase_limpia)
  return frases_limpias

def agregar_punto_al_final(oracion):
  nueva = oracion.strip()
  if oracion[-1] != ".":
    nueva = oracion + "."
  return nueva

def descargar_archivo(ruta_archivo):
  with open(ruta_archivo, 'r') as archivo:
    contenido = archivo.read()
  lista = contenido.splitlines()
  return lista
  
def imprimir_lista(lista):
    for indice, oracion in enumerate(lista):
      print(f"Escenario {indice+1}: {oracion}")

def get_consultas_respuestas_esperadas():
  return {
    "Realizar fumigación para controlar plagas": ["Control de plaga", "Control enfermedades bacterianas", "Manejo enfermedades fungosas", "Controlar plagas e insectos", "Control de enfermedades virales"],
    "Recortar ramas de la planta": ["Despunte de inflorescencias", "Podar planta de tomate", "Podar manualmente"],
    "Echar agua a la planta": ["Regar", "Regar la huerta "],
    "Recolectar tomates": ["Cosechar tomates"],
    "Quitar las malas hierbas": ["Desmalezar", "Deshierbe", "Quita de malezas"],
    "Eliminar hongo de las plantas": [0],
    "Eliminar pestes de la planta": [0],
    "Germinar semilla": [0],
    "Fertilizar la tierra": [0],
    "limpiar hierbas no deseadas": [0],
    "colocar soportes a una planta": [0],
    "Generar abono orgánico": [0],
    "Hidratar las semillas de tomate": [0],
    "Aportar agua a las plantas": [0],
    "Pasar planta del almácigo a la tierra": [0],
    "Curar planta enferma con hongos": [0]
}

