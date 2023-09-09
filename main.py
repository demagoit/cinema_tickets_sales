import turtle
import math

SCREEN_WIDH = 600
SCREEN_HEIGH = 600

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
    t.up()
    t.goto(SCREEN_WIDH * 0.1, SCREEN_HEIGH * 0.94)
    t.down()
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

    # t.up()
    # t.goto(SCREEN_WIDH / 2, SCREEN_HEIGH * 0.98)
    # # t.right(90)
    # t.down()
    # t.circle(-radius, angle/2)

    print(radius, angle)

cinema_screen()

# for i in range(10):
#     t.circle(50)
#     t.up()
#     t.forward(60)
#     t.down()

main_screen.tracer(True)
# turtle.mainloop()
main_screen.mainloop()