import turtle  # Importa el módulo 'turtle' para crear gráficos simples.
import time  # Importa el módulo 'time' para manejar retrasos.
import random  # Importa el módulo 'random' para generar posiciones aleatorias.

wn = turtle.Screen()  # Crea la pantalla del juego.
wn.title("Snake Game by ICI")  # Establece el título de la ventana.
wn.bgcolor("darkgreen")  # Cambia el color de fondo de la ventana a verde oscuro.
wn.setup(width=600, height=600)  # Establece el tamaño de la ventana del juego.
wn.tracer(
    0
)  # Desactiva la actualización automática de la ventana (se hará manualmente para mejorar el rendimiento).

delay = 0.1  # Define el tiempo de espera entre actualizaciones (velocidad del juego).

# Variables de puntuación
score = 0  # Puntuación inicial.
high_score = 0  # Puntuación más alta.

# Creación de la cabeza de la serpiente
head = turtle.Turtle()  # Crea el objeto para la cabeza de la serpiente.
head.speed(0)  # Establece la velocidad de animación de la cabeza.
head.shape("square")  # Establece la forma de la cabeza como un cuadrado.
head.color("red")  # Cambia el color de la cabeza a amarillo.
head.penup()  # Desactiva el dibujo de líneas al moverse.
head.goto(0, 0)  # Coloca la cabeza en el centro de la pantalla.
head.direction = (
    "stop"  # Establece la dirección inicial de la serpiente como 'detenida'.
)

segments = []  # Lista vacía para almacenar los segmentos del cuerpo de la serpiente.


# Creación de la comida
food = turtle.Turtle()  # Crea el objeto para la comida.
food.speed(0)  # Establece la velocidad de la animación de la comida.
food.shape("circle")  # Establece la forma de la comida como un círculo.
food.color("red")  # Cambia el color de la comida a rojo.
food.penup()  # Desactiva el dibujo de líneas al moverse.
food.goto(0, 100)  # Coloca la comida en una posición inicial en la pantalla.


# Creación del marcador de puntuación
sc = turtle.Turtle()  # Crea el objeto para mostrar la puntuación.
sc.speed(0)  # Establece la velocidad del marcador.
sc.shape("square")  # Forma del marcador.
sc.color("white")  # Color del texto del marcador.
sc.penup()  # Desactiva el dibujo de líneas.
sc.hideturtle()  # Oculta el marcador (para mostrar solo el texto).
sc.goto(0, 260)  # Coloca el marcador en la parte superior de la pantalla.
sc.write(
    "Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal")
)  # Muestra la puntuación inicial.


# Funciones para mover la serpiente en diferentes direcciones
def Up():
    if (
        head.direction != "down"
    ):  # La serpiente no puede moverse hacia arriba si ya se está moviendo hacia abajo.
        head.direction = "up"  # Cambia la dirección de la cabeza a 'arriba'.


def Down():
    if (
        head.direction != "up"
    ):  # La serpiente no puede moverse hacia abajo si ya se está moviendo hacia arriba.
        head.direction = "down"  # Cambia la dirección de la cabeza a 'abajo'.


def Right():
    if (
        head.direction != "left"
    ):  # La serpiente no puede moverse a la derecha si ya se está moviendo a la izquierda.
        head.direction = "right"  # Cambia la dirección de la cabeza a 'derecha'.


def Left():
    if (
        head.direction != "right"
    ):  # La serpiente no puede moverse a la izquierda si ya se está moviendo a la derecha.
        head.direction = "left"  # Cambia la dirección de la cabeza a 'izquierda'.


# Función para mover la serpiente en la dirección actual
def move():
    if head.direction == "up":  # Si la dirección es 'arriba':
        y = head.ycor()  # Obtiene la coordenada Y actual de la cabeza.
        head.sety(y + 25)  # Mueve la cabeza 20 píxeles hacia arriba.
    if head.direction == "down":  # Si la dirección es 'abajo':
        y = head.ycor()  # Obtiene la coordenada Y actual.
        head.sety(y - 25)  # Mueve la cabeza 20 píxeles hacia abajo.
    if head.direction == "right":  # Si la dirección es 'derecha':
        x = head.xcor()  # Obtiene la coordenada X actual.
        head.setx(x + 25)  # Mueve la cabeza 20 píxeles hacia la derecha.
    if head.direction == "left":  # Si la dirección es 'izquierda':
        x = head.xcor()  # Obtiene la coordenada X actual.
        head.setx(x - 25)  # Mueve la cabeza 20 píxeles hacia la izquierda.


# Controles de teclado
wn.listen()  # Escucha las entradas del teclado.
wn.onkeypress(
    Up, "Up"
)  # Cuando se presiona la tecla 'arriba', llama a la función 'Up'.
wn.onkeypress(
    Down, "Down"
)  # Cuando se presiona la tecla 'abajo', llama a la función 'Down'.
wn.onkeypress(
    Right, "Right"
)  # Cuando se presiona la tecla 'derecha', llama a la función 'Right'.
wn.onkeypress(
    Left, "Left"
)  # Cuando se presiona la tecla 'izquierda', llama a la función 'Left'.

# Bucle principal del juego
while True:
    wn.update()  # Actualiza la pantalla en cada iteración del bucle.

    # Verificación de colisiones con el borde
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):  # Si la cabeza colisiona con los bordes:
        time.sleep(1)  # Pausa el juego por 1 segundo.
        head.goto(0, 0)  # Restaura la cabeza al centro de la pantalla.
        head.direction = "stop"  # Detiene el movimiento de la serpiente.

        for segment in segments:  # Mueve todos los segmentos fuera de la pantalla.
            segment.goto(1000, 1000)
        segments.clear()  # Limpia la lista de segmentos.

        # Restablece la puntuación y la velocidad del juego
        score = 0
        delay = 0.1
        sc.clear()  # Limpia el marcador.
        sc.write(
            "Score: {}  High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Verificación de colisión con la comida
    if head.distance(food) < 20:  # Si la cabeza está cerca de la comida:
        # Mueve la comida a una nueva posición aleatoria
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Agrega un nuevo segmento al cuerpo de la serpiente
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)  # Añade el nuevo segmento a la lista de segmentos.

        # Reduce el retraso para aumentar la velocidad del juego
        if delay > 0.05:
            delay += 0.001

        # Aumenta la puntuación
        score += 10
        if score > high_score:  # Si la nueva puntuación es mayor que la más alta:
            high_score = score  # Actualiza la puntuación más alta.

        # Actualiza el marcador de puntuación
        sc.clear()
        sc.write(
            "Score: {}  High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
    # Mover los segmentos del cuerpo
    for i in range(
        len(segments) - 1, 0, -1
    ):  # Desde el último segmento hasta el primero:
        x = segments[i - 1].xcor()  # Obtiene la posición del segmento anterior.
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)  # Mueve el segmento actual a la posición del anterior.

    # Mueve el primer segmento al lugar de la cabeza
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()  # Llama a la función para mover la cabeza.

    for segment in segments:
        if(segment.distance(head) < 20):
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Muve los segmentos fuera de la pantalla
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            #Restable la puntuacion y la velocidad del juego
            score = 0
            delay = 0.1
            sc.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)  # Pausa el juego por el tiempo de retraso definido.


wn.mainloop()