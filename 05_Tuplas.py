#Los elementos de la tupla NO se pueden modificar, ni agregar ni quitar
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (21, 1.70, "Jose", "peralta")

print(my_tuple)
print(my_tuple[1])

print(my_tuple.count("Jose"))
print(my_tuple.index("Jose"))