# my_list = list()
my_other_list = []

my_list = [21, 20, 30, 35, 50, 3]
print(my_list[4])

my_other_list = ["Ramiro", "Sosa"]

print(my_other_list[-2])
print(my_other_list.count("Ramiro"))

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

my_other_list.pop()
print(my_other_list)

my_lista = []
my_other_list = my_lista.copy()
print(my_other_list)

my_other_list.reverse()
print(my_other_list)

my_list.sort()
print(my_list)
