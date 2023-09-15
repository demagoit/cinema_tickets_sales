import turtle
import math

SCREEN_WIDH = 600
SCREEN_HEIGH = 600
CINEMA_HEADER = SCREEN_HEIGH * 0.1
FONT_SIZE = SCREEN_HEIGH // 50

SEAT_ROWS = 10
SEATS_IN_ROW = 8

cell_width = SCREEN_WIDH / SEATS_IN_ROW
cell_height = (SCREEN_HEIGH - CINEMA_HEADER) / SEAT_ROWS

if cell_height < cell_width:
    SEAT_SIZE = cell_height * 0.8 / 2
else:
    SEAT_SIZE = cell_width * 0.8 / 2
print(SEAT_SIZE)

main_screen = turtle.Screen()

# set size of screen
main_screen.setup(SCREEN_WIDH, SCREEN_HEIGH)
# set starting point at left bottom
main_screen.setworldcoordinates(0,0,SCREEN_WIDH, SCREEN_HEIGH)

t = turtle.Turtle()
# hide pen shape
t.hideturtle()
t.speed(0)

# free seats writer
free_writer = turtle.Turtle()
free_writer.hideturtle()
free_writer.speed(0)

# sold seats writer
sold_writer = turtle.Turtle()
sold_writer.hideturtle()
sold_writer.speed(0)

def cinema_screen():
    # switch off animation
    main_screen.tracer(False)
    t.fillcolor('blue')
    t.up()
    t.goto(FONT_SIZE * 10, SCREEN_HEIGH - FONT_SIZE * 2)
    t.down()
    t.begin_fill()
    t.left(90)
    t.forward(FONT_SIZE * 2)
    t.right(90)
    t.forward(SCREEN_WIDH - FONT_SIZE * 20)
    # t.forward(SCREEN_WIDH * 0.8)
    t.right(90)
    t.forward(FONT_SIZE * 2)
    # t.forward(SCREEN_HEIGH * 0.05)

    radius = FONT_SIZE * 1.8 / 2 + (SCREEN_WIDH - FONT_SIZE * 20)**2 / (8 * FONT_SIZE * 1.8)
    angle = math.asin((SCREEN_WIDH - FONT_SIZE * 20) / radius / 2) * 2 * 180 / math.pi
    # radius = SCREEN_HEIGH * 0.04 / 2 + (SCREEN_WIDH * 0.8)**2 / (8 * SCREEN_HEIGH * 0.04)
    # angle = math.asin(SCREEN_WIDH * 0.8 / radius / 2) * 2 * 180 / math.pi

    t.up()
    t.goto(SCREEN_WIDH / 2, SCREEN_HEIGH - FONT_SIZE * 0.2)
    t.right(90)
    t.circle(radius, -angle/2)

    t.down()
    t.circle(radius, angle)
    t.end_fill()

    t.setheading(0)
    main_screen.tracer(True)
    
def draw_seats():

    # switch off animation
    main_screen.tracer(False)

    # draw seats
    for row in range(SEAT_ROWS):
        for seat in range(SEATS_IN_ROW):
            x = cell_width * (1/2 + seat)
            y = cell_height * (0.1 + row)
            seat_sold[x,y] = False
            t.up()
            t.goto(x, y)
            t.down()
            t.fillcolor('green')
            t.begin_fill()
            t.circle(SEAT_SIZE)
            t.end_fill()
    main_screen.tracer(True)

def get_seat(x,y):
    for seat in seat_sold:
        distance = ((x - seat[0])**2 + (y - seat[1] - SEAT_SIZE)**2)**0.5
        if distance <= SEAT_SIZE:
            return seat
    return

def book_set(x, y):
    seat = get_seat(x,y)
    if seat:
        seat_sold[seat] = True
        # switch off animation
        main_screen.tracer(False)
        t.up()
        t.goto(seat)
        t.down()
        t.fillcolor('red')
        t.begin_fill()
        t.circle(SEAT_SIZE)
        t.end_fill()
        main_screen.tracer(True)
        write_available()

def unbook_set(x, y):
    seat = get_seat(x,y)
    if seat:
        seat_sold[seat] = False
        # switch off animation
        main_screen.tracer(False)
        t.up()
        t.goto(seat)
        t.down()
        t.fillcolor('green')
        t.begin_fill()
        t.circle(SEAT_SIZE)
        t.end_fill()
        main_screen.tracer(True)
        write_available()

def write_available():
    free_writer.clear()
    free_writer.penup()
    free_writer.goto(0, SCREEN_HEIGH - 2 * FONT_SIZE)
    free_writer.pendown()

    sold_writer.clear()
    sold_writer.penup()
    sold_writer.goto(0, SCREEN_HEIGH - 4 * FONT_SIZE)
    sold_writer.pendown()

    free_seats = 0
    for i in seat_sold.values():
        if not i:
            free_seats += 1
    free_writer.write(f"Free seats: {free_seats}", font = ("Arial", FONT_SIZE, "normal"))
    sold_writer.write(f"Sold seats: {len(seat_sold) - free_seats}", font = ("Arial", FONT_SIZE, "normal"))

cinema_screen()
seat_sold = {}
draw_seats()
write_available()
# print(seat_sold)
main_screen.onclick(book_set)
main_screen.onclick(unbook_set, btn=3)

# turtle.mainloop()
main_screen.mainloop()