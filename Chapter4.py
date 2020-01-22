#Exercise 4.1.1
print('\n ***Exercise 4.1.1**')
import math
import turtle


def square(t):
    bob=turtle.Turtle()
    for i in range(4):
        bob.fd(100)
        bob.lt(90)
square('bob')

#Exercise 4.1.2
print('\n ***Exercise 4.1.2**')

def square(t,length):
    bob=turtle.Turtle()
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
square('bob',100)

#Exercise 4.1.3
print('\n ***Exercise 4.1.3**')

def polygon(t,length,n):
    bob=turtle.Turtle()
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)
polygon('bob',100,5)

#Exercise 4.1.4
print('\n ***Exercise 4.1.4**')
def circle(t, r):
    circumference = 2 * math.pi * r
    t = 100
    length = circumference / t
    polygon('bob', 5, 100)
circle(100,10)

#Exercise 4.1.5
print('\n ***Exercise 4.1.5**')















