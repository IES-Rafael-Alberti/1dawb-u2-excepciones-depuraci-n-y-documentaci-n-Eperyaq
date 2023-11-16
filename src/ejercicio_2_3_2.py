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

    """
    error = True
    while error:
        try:
            
            numero = int(input(("Dime un numero entero positivo porfavor: ")))
            if numero <= 0:
                raise Exception("Error, no seas asi, pon el numero bien")
            #el raise es un error que nosotros queremos que pase si o si, normalmente que te den un numero negativo no pasa nada pero como nostros queremos que de el problema ponemos  el raise,para que salte si o si
        
            error = False
        
        except ValueError:
            print("Error, número no válido")
        except Exception as e:
            print(e)
    """

    error = True
    while error:
        try:
            
            numero = int(input(("Dime un numero entero positivo porfavor: ")))
            if numero <= 0:
                raise ValueError("no seas asi, pon el numero bien")
            
        
            error = False
        
        except ValueError as e:
            print("Error, " + str(e))

    
    return numero




def main():
    clean_terminal()
    print(pedir())
#me salen varios errores pero sin nombre, y despues sale el error forzado mio, esta bien?
#code is unreachable

if __name__=="__main__":
    main()
