def inver_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida
if __name__ == "__main__":
    lista_dada = [1,2,3,5,6]

lista_invertida  =inver_lista(lista_dada)
print(f"lista original: {lista_dada}")
print(f"lista invertida:{lista_invertida}")
