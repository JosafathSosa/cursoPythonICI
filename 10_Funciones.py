#En c++
#int suma(int x, int y)

def my_function():
    print("hola")

my_function()

def suma_valores(x, y):
    print("el resultado es",  x + y)

suma_valores(10, 5)

def funcion_funcion():
    def hola ():
        return "hola"
    return hola()

print(funcion_funcion())

def div_values(x , y):
    div = x/ y
    return div
print(div_values(20, 2))

def nombre(x, y, Z="Jimenez"):
    print(f"El nombre completo es: {x}{y}{Z}")

x = input("Dame el valor x")
y = input("Dame el valor y")

nombre(x,y)