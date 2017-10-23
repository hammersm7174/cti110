import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("M5LAB1 - Mark Hammers")

t = turtle.Turtle()

#graphics
t.pensize(6)
t.pencolor("orange")
t.shape("turtle")
t.color("orange")

# drawing the shapes
for i in (1,2,3,4):
    t.forward(100)
    t.left(90)

t.right(180)
t.forward(80)
t.right(180)

for j in (1,2,3):
    t.forward(50)
    t.left(135)


wn.mainloop()
