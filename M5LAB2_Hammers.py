import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("M5LAB2 - Mark Hammers")

t = turtle.Turtle()

#graphics
t.pensize(5)
t.pencolor("yellow")
t.shape("turtle")
t.color("orange")

# drawing the initials

t.left(90)
t.forward(80)
t.right(135)
t.forward(40)
t.left(135)
t.forward(40)
t.right(135)
t.forward(80)
t.penup()
t.left(90)
t.forward(40)
t.left(90)
t.pendown()
t.forward(80)
t.penup()
t.right(180)
t.forward(40)
t.left(90)
t.pendown()
t.forward(40)
t.penup()
t.left(90)
t.forward(40)
t.left(180)
t.pendown()
t.forward(80)



wn.mainloop()
