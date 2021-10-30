size =(input("Enter the size of balloon(large/small):\n")
if size == "large":
       import turlte
       window = turtle.Screen()
       turtle.bgcolor("yellow")
       turtle.color("magenta","cyan")
       turtle.pensize(5)
       turtle.begin_fill()
       turtle.circle(100)
       turtle.end_fill()

elif size =="small":
       import turtle
       window = turtle.Screen()
       turtle.bgcolor("yellow")
       turtle.color("magenta","cyan")
       turtle.pensize(5)
       turtle.begin_fill()
       turtle.circle(100)
       turtle.end_fill()
else:
       print("ERROR!!!!!")
