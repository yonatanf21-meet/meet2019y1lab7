import turtle
turtle.goto(0,0)

def up():
    print("You pressed the up key.")

turtle.onkey(up, "up")
turtle.goto(0,0)
turtle.listen()
