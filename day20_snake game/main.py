import turtle as t
from snake_body import Snake
from food import Food
from scoreboard import Score
import time

#screen appearance
screen=t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

#snake movement
game_is_on=True

score=Score()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        score.score_tracker()
        snake.extend()
    
    # detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-300 or snake.head.ycor()>290 or snake.head.ycor()<-300:
        game_is_on=False
        score.game_over()

    # detect colliosion with tail and increment of tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()

screen.exitonclick()