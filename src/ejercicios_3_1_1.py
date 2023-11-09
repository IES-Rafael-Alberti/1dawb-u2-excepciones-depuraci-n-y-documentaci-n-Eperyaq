"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
from ejercicio_2_3_4 import clean_terminal

def pedirAsignaturas():
    
    asignaturas = None
    while asignaturas != "":

        asignaturas = input("Dime que asignatura quieres meter y si no quieres meter nada introduce un espacio vacio: ")

    return asignaturas

def meterAsignaturas(asignaturas):
    
    listaAsignaturas = []
    listaAsignaturas.append(asignaturas)
    
    return listaAsignaturas

def main():

    clean_terminal

    asignaturas =pedirAsignaturas()

    print(meterAsignaturas(asignaturas))


if __name__ == "__main__":
    main()