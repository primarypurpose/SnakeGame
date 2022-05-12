from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_over = False
while not game_over:
	screen.update()
	time.sleep(0.1)
	snake.move()
	# Detect collision with food.
	if snake.head.distance(food) < 12:
		food.refresh()
		scoreboard.increase_score()

screen.exitonclick()
