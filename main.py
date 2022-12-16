from turtle import Screen
from user import User
from cars import Cars
from scoreboard import Scoreboard
import time

#constans
cars = []
GAME_ON = True
delay = 0.1

#making the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

#making the player
user = User()

#making the cars
for i in range(0, 20):
    cars.append(Cars())

while GAME_ON:

    #move the cars
    for car in cars:
        car.cars_move()

        #Detec collision with car
        if car.distance(user) < 21:
            GAME_ON = False
            scoreboard.game_over()

    # update the screen
    time.sleep(delay)
    screen.update()


    #move the turtle
    screen.listen()
    screen.onkey(fun=user.move_up, key="w")


    #update scoreboard and speed
    if user.ycor() > 280:
        user.reset_position()
        scoreboard.leve_up()
        scoreboard.scoreboard_update()
        delay *= 0.5

screen.exitonclick()
