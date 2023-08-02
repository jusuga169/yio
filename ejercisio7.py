def encontrar_max_o_min(lista):
    maximo = max(lista)
    minimo = min(lista)

if __name__ == "__main__":
    lis_dada = [10,5,15,7,14]

    max_numero,min_numero = encontrar_max_o_min(lis_dada)
    print(f"el numero mas grande en la lista es:{max_numero}")
    print(f"el numero mas grande en la lista es:{min_numero}")
