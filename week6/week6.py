# import turtle
# #--setup--
# screen = turtle.Screen()
# tess = turtle.Turtle()
# screen.bgcolor("light green")
# #--functions--
# def drawPoly(someturtle,someside,somesize):
#     for i in range(someside):
#         someturtle.fd(somesize)
#         someturtle.left((360/someside))
# #--exercises--
# # Exercise 1
# drawPoly(tess,8,50)
# screen.exitonclick()
#execise 2
# import turtle
# turtle.bgcolor("lightgreen")
# screen = turtle.Screen()
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(2)
# def drawPoly(someturtle,someside,somesize):
#     for i in range(someside):
#         someturtle.fd(somesize)
#         someturtle.left((360/someside))
# for i in range(20):
#     drawPoly(tess,4,50)
#     tess.left(18)
# tess.speed(100)
# def drawSpiral(someturtle,angle):
#     size = 1
#     for i in range(100):
#         someturtle.forward(size)
#         someturtle.right(angle)
#         size +=2
# # Exercise 3
# tess.penup()
# tess.color("blue")
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess,90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)
# #exit
# screen.exitonclick()
# def drawEquiltriangle(someturtle,somesize):
#    drawPoly(someturtle,3,somesize)
#Exercise 4
# drawEquiltriangle(tess,100)
#exercise 5
# def drawstar (someturtle,somesize):
#     for i in range(5):
#         someturtle.fd(somesize)
#         someturtle.right(144)
# tess.color("pink")
# tess.pensize(3)
# tess.penup()
# tess.backward(250)
# tess.pendown()
# for i in range(5):
#     drawstar(tess,80)
#     tess.penup()
#     tess.fd(350)
#     tess.right(144)
#     tess.pendown()
# screen.exitonclick()
#exercise 6
# def drawSprite (someturtle,legs,length):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
# drawSprite(tess,15,120)
# screen.exitonclick()
