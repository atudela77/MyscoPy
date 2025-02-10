def feast(beast, dish):
    # your code here
    pass
    # Devuelve true si las dos cadenas empieza por el mismo caracter y acaban por el mismo caracter
    # Se mete la evaluación de la expresión condicional directamente en el return de manera que
    #  devuelve true o false dependiendo de si se cumple la expresión o no.
    # Esto convierte la función feast en una función lógica que se puede utilizar en el main o 
    #  donde sea dentro de un if, match, ...
    return beast[0] == dish[0] and beast[-1] == dish[-1]

def main():
    bestia = "León"
    comida = "Lacón y jamón"
    
    if feast(bestia, comida):
        print("Correcto")
    else:
        print("Incorrecto")
        
main()