"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
from ejercicio_2_3_4 import  clean_terminal


def lista():
    tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return tuple



def main():

    clean_terminal()
    print(lista()[::-1])


if __name__ == "__main__":
    main()