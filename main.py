import turtle
import math

SCREEN_WIDH = 600
SCREEN_HEIGH = 600
CINEMA_HEADER = SCREEN_HEIGH * 0.1

SEAT_ROWS = 10
SEATS_IN_ROW = 8

cell_width = SCREEN_WIDH / SEATS_IN_ROW
cell_height = (SCREEN_HEIGH - CINEMA_HEADER) / SEAT_ROWS

if cell_height < cell_width:
    SEAT_SIZE = cell_height * 0.8 / 2
else:
    SEAT_SIZE = cell_width * 0.8 / 2

main_screen = turtle.Screen()

# set size of screen
main_screen.setup(SCREEN_WIDH, SCREEN_HEIGH)
# set starting point at left bottom
main_screen.setworldcoordinates(0,0,SCREEN_WIDH, SCREEN_HEIGH)
# switch off animation
main_screen.tracer(False)

t = turtle.Turtle()
# hide pen shape
t.hideturtle()

def cinema_screen():
    t.fillcolor('blue')
    t.up()
    t.goto(SCREEN_WIDH * 0.1, SCREEN_HEIGH * 0.94)
    t.down()
    t.begin_fill()
    t.left(90)
    t.forward(SCREEN_HEIGH * 0.05)
    t.right(90)
    t.forward(SCREEN_WIDH * 0.8)
    t.right(90)
    t.forward(SCREEN_HEIGH * 0.05)

    radius = SCREEN_HEIGH * 0.04 / 2 + (SCREEN_WIDH * 0.8)**2 / (8 * SCREEN_HEIGH * 0.04)
    angle = math.asin(SCREEN_WIDH * 0.8 / radius / 2) * 2 * 180 / math.pi
    t.up()
    t.goto(SCREEN_WIDH / 2, SCREEN_HEIGH * 0.98)
    t.right(90)
    t.down()
    t.circle(radius, -angle/2)

    t.up()
    t.goto(SCREEN_WIDH / 2, SCREEN_HEIGH * 0.98)
    t.setheading(180)
    t.down()
    t.circle(radius, angle/2)
    t.end_fill()

    t.setheading(0)
    
    
cinema_screen()

# draw seats
for row in range(SEAT_ROWS):
    for seat in range(SEATS_IN_ROW):
        t.up()
        t.goto(cell_width * (1/2 + seat), cell_height * (0.1 + row))
        t.down()
        t.circle(SEAT_SIZE)


main_screen.tracer(True)
# turtle.mainloop()
main_screen.mainloop()