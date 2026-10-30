# import math
import turtle
# fonctions
# def SumTo(n):
#     n = int(input("what's your namber:"))
#     n=(n*(n+1))/2
#     return n
# def drawstar(t,n,size):
#     angle=180 -180/n
#     for i in range(n):
#         t.fd(size)
#         t.right(angle)
# def SumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
# def mySqrt(x):
#     guess = x/2
#     for i in range(20):
#         guess = (1/2)* (guess + x/ guess)
#     return guess
# def sprits(t,legs,leght):
#     angle=360/ legs
#     for i in range(legs):
#         t.fd(leght)
#         t.backward(leght)
#         t.left(angle)
# def fancySquare(t,size):
#     for corner in range(4):
#         spritetip(t,8,20)
#         t.fd(size)
#         t.left(90)
# def tip(t,size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size/2)
#     t.right(120)
#     t.fd(size)
#     t.right(120)
#     t.fd(size)
#     t.right(120)
#     t.fd(size/2)
#     t.right(90)
#     t.end_fill()
# def spritetip(t,legs,leghth):
#     angle =360/ legs
#     for i in range(legs):
#         t.fd(leghth)
#         tip(t,10)
#         t.backward(leghth)
#         t.left(angle)
# def checknumber(n):
#     if n>0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return "zero"
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.fd(height +gap)
#     t.write(" "+ str(height))
#     t.backward(height +gap)
#     t.right(90)
#     t.pendown()
#     t.begin_fill()
#     t.left(90)
#     t.fd(height)
#     t.right(90)
#     t.fd(40)
#     t.right(90)
#     t.fd(height)
#     t.left(90)
#     t.end_fill()
# def BarChart():
#     maxheight = max(data)
#     num_bars = len(data)
#     border =10
#     gap =(maxheight - border)/25
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right =40 *num_bars+ border
#     top = maxheight + 4 * border
#     wn.setworldcoordinates(-border,-border,right,top)
#     t = turtle.Turtle()
#     t.color("blue")
#     t.fillcolor("red")
#     t.pensize(3)
#     for height in data:
#         drawBar(t, height,gap)
#     wn.exitonclick()
# exercise1
# result=SumTo(10)
# print(result)
#exercise2
# tess=turtle.Turtle()
# screen=turtle.Screen()
# tess.pensize(3)
# drawstar(tess,7,100)
# screen.exitonclick()
#exercise3
# n = int(input("Enter a number: "))
# print(SumTo(10))
# print("sum is", SumTo(n))
#exercise4
# n = int(input("enter a positive integer: "))
# print(mySqrt(n))
# print (math.sqrt(n))
#exercise5
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.pensize(2)
# fancySquare(tess,100)
# screen.exitonclick()
#exercise6
# n = [-7,5,0]
# for number in n:
#     print(number, "is",checknumber(number))
#exercise7
# data =[48,117,200,240,160,260,220]
# BarChart()




