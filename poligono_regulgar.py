import turtle

tata = turtle.Turtle()

nlados = 13
angulo = 360/nlados
for _ in range(nlados):
    tata.forward(50)
    tata.right(angulo)
    