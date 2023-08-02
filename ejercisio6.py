def _calcular_suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
if __name__ == "__main__":
    lis_dada = [1,7,3,4,5] # puedes colocar la lista de numeros como desees
    sum_total = _calcular_suma_lista(lis_dada)
    print(f"la suma de la lista de los numeros es : {sum_total}")
