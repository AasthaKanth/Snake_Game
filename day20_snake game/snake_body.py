import turtle as t
position=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments=[]
        self.creat_snake()
        self.head=self.segments[0]

    def add_seg(self,i):
        snake=t.Turtle()
        snake.penup()
        snake.color("white")
        snake.shape("square")
        snake.goto(i)
        self.segments.append(snake)
    
    def creat_snake(self):
        for i in position:
            self.add_seg(i)
        
        t.Screen().update()
    
    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)   
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    
