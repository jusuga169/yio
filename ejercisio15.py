def es_palin(cadena):
  cadena = cadena.lower()
  cadena = cadena.replace ("  ","")
  return cadena == cadena [::-1]
if __name__ == "__main__":
    texto = input("ingrese  una cadena de texto:")
    if es_palin(texto):
        print("es un palindromo.")
    else:
        print("no es palindromo")

