# playlist - https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2

import turtle

window = turtle.Screen()
window.title("pong by tokyoedtdch zrobione przez grubasa")
window.bgcolor("black")  # gbcolor - background color / kolor tła
window.setup(width=800, height=600)  # ustala wielkosc ekranu na 800x600
window.tracer(0)  # stop automaticly update window, przyspiesza nasza gierke

# Paddle A
paddle_a = turtle.Turtle()  # object of class Turtle
paddle_a.speed(0)  # najwieksza mozliwa szybkosc
paddle_a.shape("square")  # ustalasz rodzaj blocku, bedzie kwadrat. Base shape is (20x20)pixels
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # zwieksza wysokosc 5krotnie, zwieksza szerokosc 1 krotnie czyli zostawia takie samo
paddle_a.penup()  # turtles by definiots draw the line then they move. WE dont want it. .penup() disables them
paddle_a.goto(-350, 0)  # miejsce gdzie sie zaczyna, leci 350 w lewo i 0 w góre, bo zaczyna centrum to (400,300)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # 0,0 to centrum wiec ball nie poruszamy od centum nawet o 1 pixel
ball.delta_x = 0.25  # o ile zmienia sie x piłki co kazda iteracje
ball.delta_y = 0.25  # o ile zmienia sie y piłki co kazda iteracje

# Counting points
score_A = 0
score_B = 0


# Pen - printing result
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("red")
pen.hideturtle()  # nie widzimy tego, chcemy zobaczyc napis a nie co tworzy ten napis
pen.goto(0, 260)
pen.write(f"Player A: {score_A} Player B: {score_B}", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()  # pobieranie wspolrzedna y naszego padla
    y += 20  # kiedy idzie do gory to dodajemy 20 pixeli
    paddle_a.sety(y)  # sety = set y, ustawianie nowej wspolrzednej dla y


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

window.onkeypress(paddle_b_up, "Up")  # Up - upper arrow
window.onkeypress(paddle_b_down, "Down")  # Down - down arrow


# main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.delta_x)  # gets X coordinate and adds delta_x
    ball.sety(ball.ycor() + ball.delta_y)  # gets X coordinate and adds delta_y

    # Border checking
    if ball.ycor() > 290:  # 290 is maximum height
        ball.sety(290)
        ball.delta_y *= -1  # start going opposite direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.delta_y *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)  # moves ball to the center of screen
        ball.delta_x *= -1
        score_A += 1
        pen.clear()
        pen.write(f"Player A: {score_A} Player B: {score_B}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.delta_x *= -1
        score_B += 1
        pen.clear()
        pen.write(f"Player A: {score_A} Player B: {score_B}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if ball.xcor() > 340  and ball.xcor() < 360 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.delta_x *= -1

    if ball.xcor() < -340  and ball.xcor() > -360 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.delta_x *= -1
