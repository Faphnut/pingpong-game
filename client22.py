import errno
import sys
import turtle
import socket
import random
ballAllowance = 0

t1 = turtle.Turtle()
t1.penup()
t1.goto(-350, 0)
t1.shape('square')
t1.color('blue')
t1.speed(0)
t1.shapesize(stretch_wid=4, stretch_len=1)

screen = turtle.Screen()
screen.setup(800, 800)
message = ""
screen.bgcolor('black')

my_username = screen.textinput('Name', 'Enter your name')

tt = turtle.Turtle()
tt.ht()
tt.color('brown')
tt.speed(0)
tt.goto(0, 400)
tt.goto(0, -400)

scoreA = turtle.Turtle()
scoreA.score = 5
scoreA.penup()
scoreA.ht()
scoreA.goto(-200, 350)
scoreA.color('blue')

scoreB = turtle.Turtle()
scoreB.score = 5
scoreB.penup()
scoreB.ht()
scoreB.goto(0, 350)
scoreB.color('red')

# star
scoreC = turtle.Turtle()
scoreC.score = 5
scoreC.penup()
scoreC.ht()
scoreC.goto(200, 350)
scoreC.color('green')

scoreA.write('5', font=("Arial", 18, "normal"))
scoreB.write('5', font=("Arial", 18, "normal"))
scoreC.write('5', font=("Arial", 18, "normal"))
scoreA.speed(0)
scoreB.speed(0)
scoreC.speed(0)

t2 = turtle.Turtle()
t2.penup()
t2.speed(0)
t2.goto(300, 0)
t2.shape('square')
t2.color('red')
t2.shapesize(stretch_wid=4, stretch_len=1)

# setareh added this code
t4 = turtle.Turtle()
t4.penup()
t4.goto(0, -350)
t4.shape('square')
t4.color('green')
t4.shapesize(stretch_wid=1, stretch_len=4)
t4.speed(0)

move_ball1 = False
move_ball2 = False
move_ball3 = False

ball_list = []
def initialize_ball():
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.color('white')
    ball.penup()
    ball.direction =1
    ball.isUp = 1
    ball.goto(0, 0)
    ball_list.append(ball)

def setBall():
    global move_ball2, message, ballAllowance
    if ballAllowance < 2:
        move_ball2 = True
        message = 'Enter'
        initialize_ball()
        ballAllowance += 1


def moveball():
    global message, move_ball1, move_ball2, ball_list, ballAllowance
    if not move_ball1 and not move_ball2:
        return

    for ball in ball_list:
        if ball.xcor() > 370 or ball.xcor() < -370 or ball.ycor() < -370:
            if ball.xcor() > 370:
                scoreB.score -= 1
                scoreB.clear()
                scoreB.write(str(scoreB.score), font=("Arial", 18, "normal"))

            if ball.xcor() < -370:
                scoreA.score -= 1
                scoreA.clear()
                scoreA.write(str(scoreA.score), font=("Arial", 18, "normal"))

            if ball.ycor() < -370:
                scoreC.score -= 1
                scoreC.clear()
                scoreC.write(str(scoreC.score), font=("Arial", 18, "normal"))

            if scoreA.score == 0:
                screen.clear()
                import lost

            if scoreB.score == 0 or scoreC.score == 0:
                screen.clear()
                import win

            ball.hideturtle()
            ball_list.remove(ball)
            ballAllowance = 0

        if ball.ycor() > 370:
            ball.isUp = -ball.isUp
        if t1.ycor() + 40 > ball.ycor() > t1.ycor() - 40 and -340 > ball.xcor() > -350:
            ball.direction = -ball.direction
        if t2.ycor() + 40 > ball.ycor() > t2.ycor() - 40 and 340 < ball.xcor() < 350:
            ball.direction = -ball.direction
        if t4.xcor() - 40 < ball.xcor() < t4.xcor() + 40 and -340 > ball.ycor() > -350:
            ball.isUp = -ball.isUp
        ball.goto(ball.xcor() + 2 * ball.direction, ball.ycor() + 1 * ball.isUp)


def handleUp():
    global message
    t1.goto(-350, t1.ycor() + 20)
    message = 'Up'


def handleUp2():
    global message
    t1.goto(-350, t1.ycor() - 20)
    message = 'Down'


def move_t2_up():
    t2.goto(350, t2.ycor() + 20)


def move_t2_down():
    t2.goto(350, t2.ycor() - 20)


def move_t4_right():
    t4.goto(t4.xcor() + 20, -350)


def move_t4_left():
    t4.goto(t4.xcor() - 20, -350)


turtle.listen()
turtle.onkey(handleUp, 'Up')
turtle.onkey(handleUp2, 'Down')
turtle.onkey(setBall, 'Return')

header_length = 20
ip = '192.168.78.164'
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{header_length}}".encode('utf-8')
client_socket.send(username_header + username)
while True:
    message = ""
    moveball()
    screen.update()
    if message:
        message = message.encode('utf-8')
        message_header = f'{len(message) :< {header_length}}'.encode('utf-8')
        client_socket.send(message_header + message)
    try:
        while True:
            username_header = client_socket.recv(header_length)
            if not len(username_header):
                print('Connection closed by server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(header_length)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            print(f'{username} > {message}')
            if message == 'Enter':
                if ballAllowance < 2:
                    ballAllowance += 1
                    move_ball1 = True
                    initialize_ball()

            if message == 'UpR':
                move_t2_up()
            if message == 'DownR':
                move_t2_down()
            if message == 'Left':
                move_t4_left()
            if message == 'Right':
                move_t4_right()
            screen.update()

    except IOError as ioe:
        if ioe.errno != errno.EAGAIN and ioe.errno != errno.EWOULDBLOCK:
            print('Reading error', str(ioe))
            sys.exit()
        continue

    except Exception as e:
        print(('General error', str(e)))
        pass
    screen.update()

