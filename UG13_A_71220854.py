import turtle
s= turtle.Screen()
t= turtle.Turtle()

#D
t.penup()
t.goto(-300,60)
t.pendown()
t.goto(-300,238)
t.circle(-90,180)
t.penup()

#8
t.goto(-150,60)
t.pendown()
t.goto(-120,60)
t.circle(-25)
t.circle(30)
t.penup()

s.exitonclick()