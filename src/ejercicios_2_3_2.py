"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def pedir ():
    numero = int(input(("Dime un numero entero positivo porfavor.")))

    if numero <= 0:
        raise Exception("no seas asi, pon el numero bien")
    
    return numero




def main():
    print(pedir())
#solo hecho para el commit

if __name__=="__main__":
    main()
