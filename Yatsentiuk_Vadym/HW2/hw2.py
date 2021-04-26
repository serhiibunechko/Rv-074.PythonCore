# TASK 1

a = int(input("First number: "))
b = int(input("Second number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# TASK 2

name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")

print("Hello, " + name + ", Your age is " + age + ", You live in " + city)


# TASK 3 (з допомогою інтернету)

import turtle
lion=turtle.Turtle()
lion.up()
lion.goto(0, -100)  
lion.down()

lion.begin_fill()
lion.fillcolor("yellow")  
lion.circle(100)
lion.end_fill()

lion.up()
lion.goto(-67, -40)
lion.setheading(-60)
lion.width(5)
lion.down()
lion.circle(80, 120)    
lion.fillcolor("blue")

for i in range(-35, 105, 70):
    lion.up()
    lion.goto(i, 35)
    lion.setheading(0)
    lion.down()
    lion.begin_fill()
    lion.circle(10)   
    lion.end_fill()
    
lion.hideturtle()