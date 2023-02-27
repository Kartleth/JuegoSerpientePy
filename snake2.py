import turtle
import time
import random

#Marcador
score = 0
high_score = 0

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
cabeza_serpiente.color("#297E1C")
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

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))

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

    #Colisiones bordes
    if cabeza_serpiente.xcor() > 280 or cabeza_serpiente.xcor() < -280 or cabeza_serpiente.ycor() > 280 or cabeza_serpiente.ycor() < -280:
        time.sleep(1)
        cabeza_serpiente.goto(0,0)
        cabeza_serpiente.direction = "stop"

        #Escnder segmentos (vuerpo de serpiente)
        for segmento in segmentos:
            segmento.goto(1000,1000)
        #Limpiar codigo de segmentos
        segmentos.clear()

        #Limpiar marcador
        score = 0
        texto.clear()
        texto.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))


    #Colisiones comida
    if cabeza_serpiente.distance(comida_serpiente) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida_serpiente.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("#A4FF83")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 10
        if score > high_score:
            high_score = score
        
        texto.clear()
        texto.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

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

    #Colisiones con el cuerpo 
    for segmento in segmentos:
        if segmento.distance(cabeza_serpiente) < 20:
            time.sleep(1)
            cabeza_serpiente.goto(0,0)
            cabeza_serpiente.direction = "stop"
            #Esconde los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            #Limpiar los elementos de la lista
            segmentos.clear()

            #Limpiar marcador
            score = 0
            texto.clear()
            texto.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(posponer)
