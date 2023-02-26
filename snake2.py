import turtle
import time
import random


#Configuración de la ventana
wn = turtle.Screen()
wn.title("Proyecto Karla Lerma")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Cabeza de la serpiente
cabeza_serpiente = turtle.Turtle()
cabeza_serpiente.speed(0)
cabeza_serpiente.shape("square")
cabeza_serpiente.color("white")
cabeza_serpiente.penup()
cabeza_serpiente.goto(0,0)
cabeza_serpiente.direction = "stop"

#Comida serpiente
comida_serpiente = turtle.Turtle()
comida_serpiente.speed(0)
comida_serpiente.shape("circle")
comida_serpiente.color("red")
comida_serpiente.penup()
comida_serpiente.goto(0,100)

#Cuerpo de serpiente
segmentos = []



#Funciones
def arriba():
    cabeza_serpiente.direction = "up"
def abajo():
    cabeza_serpiente.direction = "down"
def izquierda():
    cabeza_serpiente.direction = "left"
def derecha():
    cabeza_serpiente.direction = "right"

def mov():
    if cabeza_serpiente.direction == "up":
        y = cabeza_serpiente.ycor()
        cabeza_serpiente.sety(y + 20)

    if cabeza_serpiente.direction == "down":
        y = cabeza_serpiente.ycor()
        cabeza_serpiente.sety(y - 20)
    
    if cabeza_serpiente.direction == "left":
        x = cabeza_serpiente.xcor()
        cabeza_serpiente.setx(x - 20)

    if cabeza_serpiente.direction == "right":
        x = cabeza_serpiente.xcor()
        cabeza_serpiente.setx(x + 20)

#Codigo para conectar movimientos con el teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


#-------------------------------------------------
posponer = 0.1

while True:
    wn.update()

    #Colisiones comida
    if cabeza_serpiente.distance(comida_serpiente) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida_serpiente.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for segmento in range(totalSeg -1, 0, -1):
        x = segmentos[segmento - 1].xcor()
        y = segmentos[segmento - 1].ycor()
        segmentos[segmento].goto(x,y)

    if totalSeg > 0:
        x = cabeza_serpiente.xcor()
        y = cabeza_serpiente.ycor()
        segmentos[0].goto(x,y)


    mov()
    time.sleep(posponer)
