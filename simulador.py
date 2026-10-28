import csv

contLista = 0
tiempo = 0
listaNuevos = []
listaListos = []
listaListosYSuspendidos = []
listaEjecutando = []
listaTerminados = []
listaParticiones = []

nroParticiones = 0
sumaTiempoEspera = 0
sumaTiempoRetorno = 0
cantidadTerminados = 0
huboCambios = False

class Proceso:
    def __init__(self, id, tiempo_arribo, tiempo_irrupcion, tamanio):
        self.id = id
        self.tiempo_llegada = tiempo_arribo
        self.tiempo_irrupcion = tiempo_irrupcion
        self.tiempo_restante = tiempo_irrupcion
        self.tamanio = tamanio
        self.tiempo_espera = 0
        self.tiempo_finalizacion = 0


with open('procesos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)      
    for fila in lector_csv:
        while len(listaNuevos) < 10:
            id = int(fila[0])
            
            if id < 0:
                print(f"Error: El ID del proceso es negativo. Se omitirá este proceso.")
                break
            
            if tiempo_arribo < 0:
                print(f"Error: El tiempo de arribo del proceso con ID {id} es negativo. Se omitirá este proceso.")
                break
            tiempo_arribo = int(fila[1])
            
            if tiempo_irrupcion < 0:
                print(f"Error: El tiempo de irrupción del proceso con ID {id} es negativo. Se omitirá este proceso.")
                break
            tiempo_irrupcion = int(fila[2])
            
            if tamanio < 0 or tamanio > 450:
                print(f"Error: El tamaño del proceso con ID {id} es negativo o mayor a 450. Se omitirá este proceso.")
                break
            tamanio = int(fila[3])
            proceso = Proceso(id, tiempo_arribo, tiempo_irrupcion, tamanio)
            listaNuevos.append(proceso)

if len(listaNuevos) == 0:
    print("No se han cargado procesos válidos. El simulador no puede continuar.")
    exit()

print("Procesos cargados correctamente:")





