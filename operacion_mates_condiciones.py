def edad(humano):
    # Esta función recoge la edad de un humano y devuelve esa edad más las
    #  edades equivalentes de un perro y un gato.
    # Devuelve una lista con [humnano, gato, perro]
    #
    # Se supone que los perros y gatos cumplen los siguiente:
    #  - Perros: Primer año humano, 14 años; segundo año humano, 9 años más; a partir del tercer año, 4 veces cada año humano.
    #  - Gatos: Primer año humano, 14 años; segundo año humano, 9 años más; a partir del tercer año, 5 veces cada año humano.
    #
    # Se puede hacer utilizando un condicional simple if-elif-else, pero esta manera es más ingeniosa,
    #  y sirve de ejemplo de uso de condiciones dentro de las propias operaciones matemáticas.
    return [humano, 14 + 9 * (humano > 1) + 4 * (humano - 2) * (humano > 2),  14 + 9 * (humano > 1) + 5 * (humano - 2) * (humano > 2)]

def main():
    print(edad(4))
    
main()
