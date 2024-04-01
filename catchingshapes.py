import turtle
import time
import random

class Shape:
    def __init__(self,shape,x,y,color):
        self.color = color
        self.shape = turtle.Turtle()
        self.shape.penup()
        self.shape.hideturtle()
        self.shape.speed(0)
        self.shape.goto(x,y)
        self.shape.color(color)
        self.shape.shape(shape)
        self.shape.shapesize(2, 2)

    def move(self):
        self.shape.sety(self.shape.ycor()-20)

    def hide(self):
        self.shape.hideturtle()

    def show(self):
        self.shape.showturtle()

class text:
    def __init__(self,x,y,text):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.goto(x,y)
        self.pen.color('black')
        self.write_text(text)

    def write_text(self,text):
        self.pen.clear()
        self.pen.write(text, align='center', font=('Arial',16,'normal'))

class game:
    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor('white')
        self.win.title('Catch the circles')
        self.win.tracer(0)

        self.shapes = []
        self.score = 0
        self.duration = 10
        self.start_time = time.time()

        self.score_text = text(-200, 250, f"Score: {self.score}")
        self.timer_text = text(200, 250, f"Timer: {self.duration}")

    def create(self):

        shapes = ['turtle','circle','square','triangle']
        color = ['red','blue','green','yellow','purple','orange']

        x = random.randint(-250,250)
        y = 250
        color = random.choice(color)
        shape = random.choice(shapes)

        new_shape = Shape(shape,x,y,color)
        new_shape.show()
        self.shapes.append(new_shape)

    def move(self):
        for shape in self.shapes:
            shape.move()
            if shape.shape.ycor() < -250:
                self.shapes.remove(shape)
                shape.hide()

    def onshapeclick(self, x, y):
        for shape in self.shapes:
            if shape.shape.distance(x,y) < 40 and shape.shape.shape() == "circle":
                self.shapes.remove(shape)
                shape.hide()
                self.score += 1
            elif shape.shape.distance(x,y) < 40 and shape.shape.shape() != "circle":
                self.shapes.remove(shape)
                shape.hide()
                self.score -= 1

            self.score_text.write_text(f"score: {self.score}")

    def update_timer(self):
       time_passed = int(time.time() - self.start_time)
       time_left = max(0, self.duration - time_passed)
       self.timer_text.write_text(f"{time_left} ")
       return time_left > 0

    def start(self):
        self.win.listen()
        self.win.onclick(self.onshapeclick)

        while self.update_timer():  # Call update_timer as a method
            self.win.update()
            self.create()
            self.move()
            time.sleep(0.1)
        else:
            self.win.textinput("Game Over", f"score: {self.score}")

if __name__ == "__main__":
    game = game()
    game.start()