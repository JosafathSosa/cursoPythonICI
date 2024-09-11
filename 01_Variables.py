my_name = "Josafath"
print(my_name)

# Integer to string
my_int = 2002
myInt_to_String = str(my_int)
print(type(myInt_to_String))

# Concatenar
print("Hola soy", my_name)
print("Soy ", my_name, " y naci en el {}".format(my_int))
print(f"Hola soy {my_name} y naci en el {my_int}")

name, lastName, age = "Josafath", "Sosa", 22
print(name, lastName, age)

address: str = "Andalucia"
print(type(address))

#Funciones
print(len("Josafath"))

cadena = "hola"
print(cadena.upper())
cadena2 = "HOLA"
print(cadena2.lower())

cadena3 = "Hola, mundo"
print(cadena3.replace("mundo", "Pyhton"))

lista = ["Hola", "Jose juan"]
print(" ".join(lista))