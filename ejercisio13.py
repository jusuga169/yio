if __name__ == "__main__":
    try:
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))

        suma = num1 + num2
        resta = num1 - num2
        multiplicion = num1 * num2

        if num2 == 0:
            division = " no se puede dividir entre cero."
        else:
            division = num1 / num2

        print(f"suma: {suma}")
        print(f"resta: {resta}")
        print(f"multiplicacion: {multiplicion} ")
        print(f"division: {division}")
    except ValueError:
        print("error: ingrese dos numeros validos.")


