def cal_media_arit(lista):
    if not lista:
        return 0
    suma = sum(lista)
    media = suma /  len(lista)
    return media
if __name__ == "__main__":
    lista_numeros = [10,20,30,40,60]
    med_arit =cal_media_arit(lista_numeros)
    print(f"la medida aritmetica de  la lista  es: {med_arit:.2f}")
