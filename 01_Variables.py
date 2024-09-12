my_name = "Josafath"
print(my_name)

# Integer to string
my_int = 2002
myInt_to_String = str(my_int)
print(type(myInt_to_String))

# Concatenar
print("Hola soy", my_name)
print("Soy ", my_name, " y naci en el {}".format(my_int))
print("Su nombre es %s y nació en el %s" %(my_name, my_int))
print(f"Hola soy {my_name} y naci en el {my_int}")

#Declarar variables en una sola linea
name, lastName, age = "Josafath", "Sosa", 22
print(name, lastName, age)

#No se puede forzar el tipado, solo se sugiere
address: str = "Andalucia"
print(type(address))

#Algunas funciones del sistema para strings
print(len("Josafath")) #Devuelve el tamaño de la cadena

#Convirte la cadena a mayusculas
cadena = "hola"
print(cadena.upper())

#Convirte la cadena a minusculas
cadena2 = "HOLA"
print(cadena2.lower())

#Permite cambiar una cadena por otra
cadena3 = "Hola, mundo"
print(cadena3.replace("mundo", "Pyhton"))

#Permite unir los elementos de un arrat convirtiendolo en string
lista = ["Hola", "Jose juan"]
print(" ".join(lista))