# Escribe un programa que determine si un número es par o impar. 
# Crea una funcion, pasale un numero y determina si el numero es par o impar
# Un número se considera par cuando es divisible por 2, es decir, cuando al dividirlo entre 2 el resto es 0. 
# Recuerda el operador aritmetico que podria ayudar a saber el residuo

def par_o_impar(num):
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"{num} No es par")
par_o_impar(8)

# Escribe un programa que cuente cuántas vocales hay en una palabra. Declara una funcion y pasale un string
# Declara una variable string con las vocales en min y may
# Itera el string y pregunta si la posicion actual es vocal y suma 1 en un contado.
# Puedes usar la palabra reservada in para verificar si dicha posicion es una vocal
# Imprime al final la cantidad de vocales encontradas y la palabra 
def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    print(f"Hay {contador} vocales en : {palabra}")

contar_vocales("hola")


# La serie de Fibonacci es una secuencia de números donde cada número (a partir del tercero) es la suma de los dos números anteriores.
# Comienza con los números 0 y 1.
# Luego sigue: 0, 1, 1, 2, 3, 5, 8, 13...
# Ejemplo:

# Los primeros dos números de la serie son 0 y 1.
# El tercer número es la suma de 0 y 1, que es 1.
# El cuarto número es la suma de 1 y 1, que es 2.
# El quinto número es la suma de 1 y 2, que es 3.
# Así que la secuencia es: 0, 1, 1, 2, 3, 5, 8, 13, 21,...

def fibonacci(n):
    fib_sequence = [0, 1]  # Comenzamos con 0 y 1
    for i in range(2, n):
        siguiente = fib_sequence[i-1] + fib_sequence[i-2]  # Suma de los dos anteriores
        fib_sequence.append(siguiente)  # Lo agregamos a la lista
    return fib_sequence[:n]

# Prueba:
n = 15
print(fibonacci(n))
