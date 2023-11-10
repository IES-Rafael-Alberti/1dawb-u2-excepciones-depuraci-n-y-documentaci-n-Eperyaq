"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
from ejercicio_2_3_4 import clean_terminal

def pedirAsignaturas():
    """Asks for the name of the subject.
    
    Args:
        asignaturas(str): an input to save the name of the subject
        
    returns:
        asignaturas(str): 
    
    """

    asignaturas = []
    while  len(asignaturas) == 0  or asignatura != "" :
        asignatura  = input("Dime que asignatura quieres meter y si no quieres meter nada introduce un espacio vacio: ")
        if asignatura != "":
            asignaturas.append(asignatura) 

    return asignaturas


def main():

    #clean_terminal()

    asignaturas = pedirAsignaturas()

    print(asignaturas)
    #hacer una funcion de mostrar lista 


if __name__ == "__main__":
    main()
#no comprendo porque al devolver asignaturas me las devuelve como literal ['']