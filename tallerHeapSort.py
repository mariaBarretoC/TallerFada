import numpy as numpy

""" Se crea la plantilla del objeto Paciente """
class Paciente:
    def __init__(self, nombre, edad, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.prioridad = prioridad
    
    def __str__(self):
        return f"Paciente(nombre='{self.nombre}', edad={self.edad}, prioridad={self.prioridad})"

""" Pide la cantidad de pacientes """
CantidadPacientes = int(input("Ingrese la cantidad de pacientes: "))

""" Se incializa el arreglo """
pacientes = numpy.array([]) 

""" Pide los datos y los almacena en el arreglo pacientes """
for i in range(CantidadPacientes):
    nombrePaciente = (input("\nIngrese el nombre: "))
    edadPaciente = (input("Ingrese la edad: "))
    prioridadPaciente = (int(input("Ingrese la prioridad: ")))

    paciente = Paciente(nombrePaciente, edadPaciente, prioridadPaciente) 

    pacientes = numpy.append(pacientes, paciente)

""" Se incializa el arreglo y hallamos si existe un "Hijo" que sea mayor al padre, si esto ocurre lo intercambiamos
    para de esta manera conservar su objetivo principal """
def heapify(pacientes, i, heapsize):
    izquierda = 2 * i + 1
    derecha = 2 * i + 2 
    minIndice = i

    if izquierda < heapsize and pacientes[izquierda].prioridad < pacientes[minIndice].prioridad:
        minIndice = izquierda
    
    if derecha < heapsize and pacientes[derecha].prioridad < pacientes[minIndice].prioridad:
        minIndice = derecha
    
    if minIndice != i:
        [pacientes[minIndice], pacientes[i]] = [pacientes[i], pacientes[minIndice]]
        heapify(pacientes, minIndice, heapsize)

""" Función heapSort - En el primer for hallamos el nodo raíz y en el segundo organizamos el arreglo de acuerdo a la urgencia 
    De la línea 64 a la 66 - Seleccionamos el valor del arreglo a eliminar, lo "eliminamos"
    y lo sobreescribimos en pacientes ordenados """
def heapSort(pacientes):
    tamañoPacientes = len(pacientes)

    for i in range(tamañoPacientes // 2 -1, -1, -1):
        heapify(pacientes, i, tamañoPacientes)

    pacientesOrdenados = numpy.array([])
    for i in range(tamañoPacientes -1, 0, -1):
        [pacientes[0], pacientes[i]] = [pacientes[i], pacientes[0]]

        paciente = pacientes[len(pacientes) - 1]
        pacientes = numpy.delete(pacientes, len(pacientes) - 1)
        pacientesOrdenados = numpy.append(pacientesOrdenados, paciente)

        heapify(pacientes, 0 , i)
    

    paciente = pacientes[len(pacientes) - 1]
    pacientes = numpy.delete(pacientes, len(pacientes) - 1)
    pacientesOrdenados = numpy.append(pacientesOrdenados, paciente)

    return pacientesOrdenados

""" Imprimimos """
sortedPatients = heapSort(pacientes)
for i in range(len(sortedPatients)):
    print(sortedPatients[i])
