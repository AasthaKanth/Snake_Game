from turtle import Turtle 

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt",mode="r") as data:
            last_high_score=data.read()
            self.high_score=int(last_high_score)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Arial",20,"bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))
        self.score=0
        self.update_score()
    
    def score_tracker(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(self.write("GAME OVER",align="center",font=("Arial",24,"bold")))


