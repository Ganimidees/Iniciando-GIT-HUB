def fn_suma(a,b):
    total_suma = a + b
    return total_suma

if __name__ == "__main__":
    a = input("Ingrese el numero: ")
    b = input("Ingrese el otro  : ")
    resultado = fn_suma(int(a),int(b))
    print("La suma es: ", resultado)


def multiplicar (a,b):
    total_mult = a * b
    return total_mult

if __name__ == "__main__":
    resultado = multiplicar(int(a),int(b))
    print("La suma es: ", resultado)