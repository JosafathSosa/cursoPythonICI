import turtle #importR WL MÒDULO PARA GRAFICOS SIMPLES
import time
import random 

wn = turtle.Screen()
wn.title("Snake by ICI")
wn.bgcolor("darkgreen")
wn.setup(width=600, height=600)
wn.tracer(
    0
)
delay = 0.1

score = 0
high_score = 0

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = (
    "stop" 
)

segments = []

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() 
food.goto(0,50)

sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0,250)
sc.write(
"Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal")
)
#Funciones para mover la serpiente
def Up():
    if(head.direction != "down"):
        head.direction = "up"
def Down():
    if(head.direction != "up"):
        head.direction = "down"
def Left():
    if(head.direction != "right"):
        head.direction = "left"
def Right():
    if(head.direction != "left"):
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y =  head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Controles de teclado
wn.listen()
wn.onkeypress(Up, "Up") # Cuando se presiona la tecla 'arriba', llama a la función 'Up'.
wn.onkeypress(Down, "Down")
wn.onkeypress(Right, "Right")
wn.onkeypress(Left, "Left")

while True:
    # Si la cabeza colisiona con los bordes:
    if(head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segment.clear()
    
    score = 0
    delay = 0.1
    sc.clear()
    sc.write("Score {} High Score: {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
wn.mainloop()