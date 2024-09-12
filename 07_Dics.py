#El dict nos sirve para acceder mas facil a datos mediante el par clave-valor
my_dict = dict()
my_other_dict = {}

my_other_dict = {
    "Nombre": "Jose",
    "Edad": 23
}

my_dict = {
    "Nombre": "Jose",
    "Edad": 23,
    "Lenguajes": {
        "Python",
        "Golang"
    },
    "Edad2": 22
}


for i in my_dict:
    if my_dict["Lenguajes"]:
        for n in my_dict["Lenguajes"]:
            print(n)
    break


print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
