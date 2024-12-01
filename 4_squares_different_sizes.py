#draw a line
#turn left 90 degrees
#draw a line
#turn left 90 degrees
#draw a line
#turn left 90 degrees
#draw a line
#turn left 90 degrees

#move to new square

#draw a line
#turn left 90 degrees
#draw a line
#turn left 90 degrees
#draw a line
#turn left 90 degrees
#draw a line
#turn left 90 degrees


#Draw a square

from turtle import*

for shape in range (4): #(1, 5)
#first square
    for sides in range(4): #(1, 5)
        forward(40+shape*20)
        left(90)

#move to new location
    penup()
    forward(100+shape*20)
    pendown()
