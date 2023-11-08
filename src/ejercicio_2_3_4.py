"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""
import os

def clean_terminal():
    """cleans terminal

    """
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def pedirNumero ():
    """Ask for a number
    
    args:
        n1 = number
        
    returns:
        int : a number
    
    """
    n1 = None
    while n1 == None:
        try:
            n1 = int(input("Dame un numero entero: "))
        except ValueError:
            print("La entrada no es correcta, prueba de nuevo: ")
        
    return n1

def main():
    
    clean_terminal()
    print(pedirNumero())


if __name__ == "__main__":
    main()
#FUNCIONA