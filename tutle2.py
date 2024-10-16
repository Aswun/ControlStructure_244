import turtle

turtle.speed(100)
nbrSides = 5
for steps in range(nbrSides):
    turtle.forward(100)
    turtle.left(360/nbrSides)
    for moresteps in range(nbrSides):
        turtle.forward(50)
        turtle.left(360/nbrSides)