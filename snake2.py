import turtle
import time



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
cabeza_serpiente.direction = "up"

#Funciones
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


posponer = 0.1

while True:
    wn.update()

    mov()
    time.sleep(posponer)
