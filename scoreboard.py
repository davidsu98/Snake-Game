from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Ariel', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0,270)
        self.color('white')
        self.write(f'Scoreboard = {self.score}', False, align= ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'Scoreboard = {self.score}', False, align= ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font = FONT)
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    