from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align= ALIGNMENT , font= FONT)
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",  align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.highscore}")
            self.score = 0
            self.update_scoreboard()

    def increase_Score(self):
        self.score += 1
        self.update_scoreboard()
