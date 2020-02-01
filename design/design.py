from turtle import Turtle, Screen

def dragging(x, y):
    yertle.ondrag(None)
    yertle.setheading(yertle.towards(x, y))
    yertle.goto(x, y)
    yertle.ondrag(dragging)

screen = Screen()

yertle = Turtle('turtle')
yertle.speed('fastest')

yertle.ondrag(dragging)

screen.mainloop()
