#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
CONTROLAR EL ERROR DESDE DENTRO
def pedirEdad(msj: str):

    error = True
    while error:
        try:
            edad = int(input(msj))
            error = False
        except:
            print("ERROR, Edad no válida")

    return edad

"""
"""
def pedirEdad(msj: str):

    entrada = input(msj)
    edad = int(entrada)
    return edad

--------CONTROLANDO EL ERROR DESDE FUERA--------
    def main():
    error = True
    while error:
        try:
            edad = pedirEdad("introduzca su edad: ")
            error = False
        except:
            print("ERROR, Edad no válida")

    print (mostrarSerie(edad))
"""
def pedirEdad(msj: str):

    entrada = input(msj)
    edad = int(entrada)
    
    if edad <= 0:
        raise Exception("No pongas edad negativa")
    
    return edad


def mostrarSerie(edad: int) -> str:
    serie = ""
    for i in range(1,  edad + 1):
        serie += str(i) + " "
    return  serie


def main():
    error = True
    while error:
        try:
            edad = None
    #si peta la edad de la funcion se queda sin valor por tanto salta el error controlado del None
            edad = pedirEdad("introduzca su edad: ")
            error = False
        except ValueError:
            print("ERROR, Edad no válida")
        except:
            print("ERROR no pongas edad negativa")

    print (mostrarSerie(edad))
    
    

if __name__=="__main__":
    main()