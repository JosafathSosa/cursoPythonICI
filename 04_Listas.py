my_list = list()
my_other_list = []

my_list = [21, 20, 30, 35, 50, 3]
print(my_list[4]) #Buscar elemento dentro del array

my_other_list = ["Ramiro", "Sosa"]

print(my_other_list[-2]) #Busca elementos al reves
print(my_other_list.count("Ramiro")) #Cuenta los elementos dentro de la lista

#Asigna valores a variables seguna la posicion del array
fisrt_name, last_name = my_other_list
print(fisrt_name)

# Agrega elemnetos a la lista
my_other_list.append("Jimenez")
print(my_other_list)

# Agrega elemneto sin eleminar elemento en esa posicion
my_other_list.insert(0, "Peralta")
print(my_other_list)

# Elimnar elemento de la lista
my_other_list.remove("Peralta")
print(my_other_list)

#Elimina el ultmo elemento de la lista
my_other_list.pop()
print(my_other_list)

#Copia en una nueva lista los elementos de my_list
my_other_list = my_list.copy()
print(my_other_list)

#Voltea los elementos de la lista
my_other_list.reverse()
print(my_other_list)

#Ordena los elementos de la lista
my_list.sort()
print(my_list)


