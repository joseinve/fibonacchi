import fibonacchi_digitos
import fibonacchi_secuencia
while True:
    operacion = input("""1-mostrar solo un digito un digito
2-mostrar toda la secuencia
0-Finalizar la ejecucion\n""")
    match operacion:
        case "1":
            digito = input("Ingrese el numero de digito a buscar \n")
            digito = int(digito)
            print(fibonacchi_digitos.fibonacci_d(digito))
            terminar = input("Presione cualquier tecla para continuar")
        case "2":
            digitos = input("Ingrese la cantidad de digitos deseada \n")
            digitos = int(digitos)
            fibonacchi_secuencia.fibonacci_s(digitos)
            terminar = input("Presione cualquier tecla para continuar")
        case "0":
            break
