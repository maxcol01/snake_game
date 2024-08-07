from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

#  initialize the screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# initialize the snake
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
is_on = True
points = 0
snake.initialize()
food.initialize_food()
pts = Score()
pts.add_score(points)
# start the game
while is_on:
    screen.update()
    time.sleep(0.1)
    is_on = snake.move_snake()  # move the snake
    coord_leader = snake.leader()
    pos_food = food.coord_food_to_catch()
    if food.collision(coord_leader,pos_food):
        points += 1
        food.initialize_food()
        snake.add_turtl()
        pts.add_score(points)
        is_on = snake.move_snake()

screen.exitonclick()
