from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
my_screen = Screen()

my_screen.setup(width= 600, height= 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
my_screen.listen()
food = Food()
scoreboard = Scoreboard()

my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_Score()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

my_screen.exitonclick()
