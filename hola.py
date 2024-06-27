def fn_suma(a,b):
    total_suma = a + b
    return total_suma

if __name__ == "__main__":
    a = input("Ingrese el numero: ")
    b = input("Ingrese el numero: ")
    resultado = fn_suma(int(a),int(b))
    print("La suma es: ", resultado)