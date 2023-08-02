def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32)* 5/9
    return celsius

if  __name__ == "__main__":
    fahrenheit = float (input("ingrese la temperatura en grados  fahrenheit:"))

    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados  fahrenheit son{celsius:.2f} grados celsius")


