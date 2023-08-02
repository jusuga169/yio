def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return"impar"
if __name__ == "__main__":
    num_dado = int(input("ingrese un numero:"))
    resultado= es_par_o_impar(num_dado)
    print(f"el numero {num_dado} es {resultado}.")


