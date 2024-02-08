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
  consultas_respuestas = [["Realizar fumigación para controlar plagas", 10, 13, 16, 17, 23, 24, 37, 38, 53, 61],
                          ["Recortar ramas de la planta", 11, 33, 39, 65], 
                          ["Echar agua a la planta", 12, 41, 54, 55, 57],
                          ["Recolectar tomates", 20, 21, 42, 64], 
                          ["Quitar las malas hierbas", 3, 8, 58], 
                          ["Eliminar hongo de las plantas", 0], 
                          ["Eliminar pestes de la planta",0], 
                          ["Germinar semilla", 0], 
                          ["Fertilizar la tierra", 0], 
                          ["limpiar hierbas no deseadas", 0], 
                          ["colocar soportes a una planta",0], 
                          ["Generar abono orgánico",0], 
                          ["Hidratar las semillas de tomate", 0], 
                          ["Aportar agua a las plantas", 0] , 
                          ["Pasar planta del almácigo a la tierra", 0], 
                          ["Curar planta enferma con hongos", 0] ]
  return consultas_respuestas
