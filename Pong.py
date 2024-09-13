#!/usr/bin/env python3
import turtle  # Importa la librería turtle para crear gráficos
import random  # Importa la librería random para reiniciar la pelota

# Ventana
vn = turtle.Screen()  # Crea la ventana para el juego
vn.title("Pong ICI")  # Título de la ventana
vn.bgcolor("black")  # Color de fondo de la ventana
vn.setup(width=800, height=600)  # Tamaño de la ventana
vn.tracer(
    0
)  # Mejora la velocidad del juego al desactivar las actualizaciones automáticas

# Puntuaciones
puntuacion_jugador_A = 0  # Puntuación inicial del jugador A
puntuacion_jugador_B = 0  # Puntuación inicial del jugador B

# Estado del juego
juego_en_pausa = False  # Variable para pausar el juego cuando alguien gane

# Barra 1 (Jugador A)
barraA = turtle.Turtle()  # Crea la barra para el jugador A
barraA.speed(0)  # Velocidad de animación
barraA.shape("square")  # Forma de la barra
barraA.color("blue")  # Color de la barra
barraA.shapesize(stretch_wid=5, stretch_len=0.25)  # Tamaño de la barra
barraA.penup()  # Desactiva el rastro de la barra
barraA.goto(350, 0)  # Posición inicial de la barra

# Barra 2 (Jugador B)
barraB = turtle.Turtle()  # Crea la barra para el jugador B
barraB.speed(0)  # Velocidad de animación
barraB.shape("square")  # Forma de la barra
barraB.color("blue")  # Color de la barra
barraB.shapesize(stretch_wid=5, stretch_len=0.25)  # Tamaño de la barra
barraB.penup()  # Desactiva el rastro de la barra
barraB.goto(-350, 0)  # Posición inicial de la barra

# Pelota
pelota = turtle.Turtle()  # Crea la pelota
pelota.speed(0)  # Velocidad de movimiento de la pelota
pelota.shape("circle")  # Forma de la pelota
pelota.color("red")  # Color de la pelota
pelota.penup()  # Desactiva el rastro de la pelota
pelota.goto(0, 0)  # Posición inicial de la pelota
pelota.dx = 3  # Movimiento en el eje x
pelota.dy = 3  # Movimiento en el eje y


# Funciones para mover las barras
def barraAUp():
    if not juego_en_pausa:  # Solo permitir movimientos si el juego no está en pausa
        y = barraA.ycor()  # Obtiene la posición actual de la barra A en y
        y += 50  # Mueve la barra hacia arriba
        barraA.sety(y)  # Establece la nueva posición


def barraADown():
    if not juego_en_pausa:
        y = barraA.ycor()  # Obtiene la posición actual de la barra A en y
        y -= 50  # Mueve la barra hacia abajo
        barraA.sety(y)  # Establece la nueva posición


def barraBUp():
    if not juego_en_pausa:
        y = barraB.ycor()  # Obtiene la posición actual de la barra B en y
        y += 50  # Mueve la barra hacia arriba
        barraB.sety(y)  # Establece la nueva posición


def barraBDown():
    if not juego_en_pausa:
        y = barraB.ycor()  # Obtiene la posición actual de la barra B en y
        y -= 50  # Mueve la barra hacia abajo
        barraB.sety(y)  # Establece la nueva posición


# Control de teclado
vn.listen()  # Detecta la entrada de teclado
vn.onkeypress(barraAUp, "Up")  # Asigna la tecla 'Up' para mover la barra A hacia arriba
vn.onkeypress(
    barraADown, "Down"
)  # Asigna la tecla 'Down' para mover la barra A hacia abajo
vn.onkeypress(barraBUp, "w")  # Asigna la tecla 'w' para mover la barra B hacia arriba
vn.onkeypress(barraBDown, "s")  # Asigna la tecla 's' para mover la barra B hacia abajo

# Mostrar puntuación
puntuacion = turtle.Turtle()  # Crea el objeto de texto para la puntuación
puntuacion.speed(0)  # Velocidad de animación
puntuacion.color("white")  # Color del texto
puntuacion.penup()  # Desactiva el rastro del objeto de texto
puntuacion.hideturtle()  # Oculta la tortuga de dibujo
puntuacion.goto(0, 260)  # Posición del texto
puntuacion.write(
    "Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "normal")
)  # Texto inicial de puntuación


# Función para actualizar la puntuación en la pantalla
def actualizar_puntuacion():
    puntuacion.clear()  # Limpia el texto anterior
    puntuacion.write(
        f"Jugador A: {puntuacion_jugador_A}  Jugador B: {puntuacion_jugador_B}",
        align="center",
        font=("Courier", 24, "normal"),
    )  # Actualiza el texto con las puntuaciones actuales


# Función para reiniciar el juego
def reiniciar_juego():
    global puntuacion_jugador_A, puntuacion_jugador_B, juego_en_pausa  # Usar variables globales
    puntuacion_jugador_A = 0  # Reiniciar puntuación de A
    puntuacion_jugador_B = 0  # Reiniciar puntuación de B
    actualizar_puntuacion()  # Actualizar el texto de puntuación
    pelota.goto(0, 0)  # Posicionar la pelota en el centro
    pelota.dx *= random.choice([-1, 1])  # Cambiar dirección aleatoriamente
    pelota.dy *= random.choice([-1, 1])
    juego_en_pausa = False  # Quitar la pausa del juego


# Ciclo del juego
while True:
    vn.update()  # Actualiza la ventana en cada iteración del ciclo

    if not juego_en_pausa:  # Solo mover la pelota si el juego no está en pausa
        # Mover la pelota
        pelota.setx(pelota.xcor() + pelota.dx)  # Mueve la pelota en el eje x
        pelota.sety(pelota.ycor() + pelota.dy)  # Mueve la pelota en el eje y

        # Bordes superior e inferior
        if pelota.ycor() > 290:  # Colisión con el borde superior
            pelota.sety(290)
            pelota.dy *= -1  # Cambia la dirección en y
        if pelota.ycor() < -290:  # Colisión con el borde inferior
            pelota.sety(-290)
            pelota.dy *= -1  # Cambia la dirección en y

        # Bordes izquierdo y derecho (puntos)
        if pelota.xcor() > 390:  # Jugador B falla, punto para A
            pelota.goto(0, 0)  # Pelota regresa al centro
            pelota.dx *= -1  # Cambia la dirección en x
            puntuacion_jugador_A += 1  # Jugador A suma un punto
            actualizar_puntuacion()  # Actualizar el marcador
        if pelota.xcor() < -390:  # Jugador A falla, punto para B
            pelota.goto(0, 0)  # Pelota regresa al centro
            pelota.dx *= -1  # Cambia la dirección en x
            puntuacion_jugador_B += 1  # Jugador B suma un punto
            actualizar_puntuacion()  # Actualizar el marcador

        # Verificar si alguien ganó
        if puntuacion_jugador_A == 3:
            puntuacion.clear()  # Limpia el texto
            puntuacion.write(
                "¡Jugador A gana! Presiona 'r' para reiniciar",
                align="center",
                font=("Courier", 36, "normal"),
            )  # Muestra el mensaje de ganador
            juego_en_pausa = True  # Pausa el juego
            vn.onkeypress(reiniciar_juego, "r")  # Tecla 'r' para reiniciar
        if puntuacion_jugador_B == 3:
            puntuacion.clear()  # Limpia el texto
            puntuacion.write(
                "¡Jugador B gana! Presiona 'r' para reiniciar",
                align="center",
                font=("Courier", 24, "normal"),
            )  # Muestra el mensaje de ganador
            juego_en_pausa = True  # Pausa el juego
            vn.onkeypress(reiniciar_juego, "r")  # Tecla 'r' para reiniciar

        # Colisiones con las barras
        if (
            350 > pelota.xcor() > 340
            and barraA.ycor() + 50 > pelota.ycor() > barraA.ycor() - 50
        ):  # Colisión con barra A
            pelota.setx(340)  # Coloca la pelota justo en el borde
            pelota.dx *= -1  # Cambia la dirección en x
        if (
            -350 < pelota.xcor() < -340
            and barraB.ycor() + 50 > pelota.ycor() > barraB.ycor() - 50
        ):  # Colisión con barra B
            pelota.setx(-340)  # Coloca la pelota justo en el borde
            pelota.dx *= -1  # Cambia la dirección en x
