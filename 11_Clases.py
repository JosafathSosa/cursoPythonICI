#PILARES POO

# 1 Herencia:  Es el mecanismo por el cual una clase (subclase) puede heredar atributos y métodos de otra clase (superclase). Facilita la reutilización del código y permite crear jerarquías de clases.
# 2 Polimorfismo:  Permite que los objetos de diferentes clases se comporten de manera distinta al compartir la misma interfaz. 
# 3 Abstraccion: Permite crear clases y objetos que representan entidades del mundo real o conceptos abstractos.
# 4 Encapsulamiento: Restringe el acceso directo a los atributos y métodos de un objeto, permitiendo su manipulación solo a través de métodos públicos (getters y setters). 

class Person:
    def __init__(self, name, lastName, peliculasFavoritas, alias="Pelon"):
        self.name = name
        self.lastName = lastName
        self.full_name = f"{name} {lastName} {alias}"
        self.peliculasFavoritas = peliculasFavoritas

    def walk(self):
        print(f"{self.full_name} esta caminando")
    
    def peliculas(self):
        for pelicula in self.peliculasFavoritas:
            print(pelicula)


peliculasFavoritas = ["Interestelar" , "Climax", "Saw"]

#Se crea un instancia u objeto de la clase Person
my_person = Person("Josafath", "Sosa", peliculasFavoritas)
print(f"Soy {my_person.full_name} y mis pelicuals favoritas son ", ", ".join(my_person.peliculasFavoritas))

my_person.walk()
print(my_person.name)


peliculasFavoritas2 = ["Harry potter" , "Hola", "Saw"]
mi_otra_persona = Person("Jose", "Juan", peliculasFavoritas2)
print(f"Soy {mi_otra_persona.full_name} y mis pelicuals favoritas son ", ", ".join(mi_otra_persona.peliculasFavoritas))
