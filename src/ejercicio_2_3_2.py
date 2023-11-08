"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
from ejercicio_2_3_4 import clean_terminal

def pedir ():
    """ask for a number
    
    args: 
        numero= just a number
    ------
    returns:
        int: a number
    """
    numero = int(input(("Dime un numero entero positivo porfavor: ")))

    while numero <= 0:
        raise Exception("no seas asi, pon el numero bien")
        num = int(input("prueba de nuevo"))
        
    
    return numero




def main():
    clean_terminal()
    print(pedir())
#me salen varios errores pero sin nombre, y despues sale el error forzado mio, esta bien?
#code is unreachable

if __name__=="__main__":
    main()
