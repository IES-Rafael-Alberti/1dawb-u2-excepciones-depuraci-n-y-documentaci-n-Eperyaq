"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
"""
from ejercicio_2_3_4 import clean_terminal

def pedirNumero():
    numero = None
    while numero == None:
        try:
            numero = int(input("Dime un numero entero positivo: "))
        except ValueError: 
            print("**ERROR** dame el numero bien: ")
        except:
            print("en serio? prueba de nuevo: ")
    return numero

def hacerSerie(num : int):
    
    contador= 0
    while contador <= num:
        print (num, end="")
        num = num -1
        if num != contador -1:
            print(",", end="")
        
    return num



def main():
    
    clean_terminal()
    numerito = pedirNumero()
    hacerSerie(numerito)
    


if __name__ == "__main__":
    main()
#me falla el final, el main