def gen_matriz(filas,columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(i * columnas + j +1)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print("".join(str(elemento) for elemento in fila))

if __name__ == "__main__":
    filas_matriz = 3
    columnas_matriz = 4

    matriz_gen = gen_matriz(filas_matriz,columnas_matriz)
    imprimir_matriz(matriz_gen)
