def gen_lista_pares ():
    lis_pares = [numero for numero in range(1,102) if numero % 2 == 0]
    return lis_pares
if __name__ == "__main__":
    lista_pares_gen = gen_lista_pares()
    print(lista_pares_gen)
