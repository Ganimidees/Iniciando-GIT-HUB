def fn_suma(a,b):
    total_suma = a + b
    return total_suma

if __name__ == "__main__":
    a = input("Ingrese el numero: ")
    b = input("Ingrese el otro  : ")
    resultado = fn_suma(int(a),int(b))
    print("La suma es: ", resultado)

def multidiv (a,b):
    total_mult = a * b
    total_div  = a / b
    return total_mult,total_div

if __name__ == "__main__":
    resultado = multidiv(int(a),int(b))
    print("La multiplicacion es: ", resultado[0])
    print("La multiplicacion es: ", resultado[1])