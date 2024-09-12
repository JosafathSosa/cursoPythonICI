#While
#For
#Python no cuenta con do - while

#Git: https://github.com/JosafathSosa/cursoPythonICI

mi_condicion = 0
while mi_condicion <= 20:
    print(mi_condicion)
    #mi_condicion = mi_condicion + 1
    mi_condicion += 1
else:
    print("Ya no es mayor que 20")


numeros = [0, 5, 2, 7, "Hola", False]
for i in numeros:
    print(i)

my_dict = {
    "Nombre": "Josafath", 
    "Edad": 22, 
    "Lenguajes": {
        "Valor1": "Swift", 
        "Valor2": "JS",
    }
}

#Imprime el valor del valor1 del subdiccionario lenguajes
for key in my_dict["Lenguajes"]:
    print(my_dict["Lenguajes"]["Valor1"])
    break

# Imprimir todos los valores en el subdiccionario "Lenguajes"
for key, value in my_dict["Lenguajes"].items():
    print(f"{key}: {value}")





