import random

def lista_aleatoria(longitud,rango_mi,rango_ma):
    lista_ale =[random.randint(rango_mi,rango_ma) for _ in range(longitud)]
    return lista_aleatoria
def impri_lista(lista):
    for elemento in lista:
        print(elemento)

if __name__ == "__main__":
    longitud_lista = 10
    valor_min = 1
    valor_ma = 100

    lista_aleatoria =  lista_aleatoria(longitud_lista,valor_min,valor_ma)
    impri_lista(lista_aleatoria())




