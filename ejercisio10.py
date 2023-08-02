def factorial (numero):
    if  numero < 0:
        raise ValueError("el factorial no esta definido para numeros negativos")
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1,numero+1):
            resultado *= i
            return resultado
if __name__ == "__main__":
    num_dado = int(input("ingrese un numero entero no negativo:"))
    try:
        resul_fact = factorial(num_dado)
        print(f"el factorial de {num_dado} es {resul_fact}. ")
    except ValueError as e:
        print(e)

