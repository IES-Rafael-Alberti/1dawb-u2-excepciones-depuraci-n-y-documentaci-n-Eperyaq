"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""
from ejercicio_2_3_4 import clean_terminal

def definePassword():
    """Defines the password
    args:
        password: str with the password
    ---
    return:
        password: str
    
    """
    password = "contraseña"
    return password


def askPassword(password: str):
    """asks for a password
    args: 
        ask: str asking for the password
    ---
    return:
        ask: str
    """
    
    try:
        ask = input("Dime cual crees que es la contraseña: ")
    except:
        print("Incorrect Password!!")
        
    return ask



def main():
    clean_terminal()
    definePassword()
    askPassword()
    
        


if __name__ == "__main__":
    main()