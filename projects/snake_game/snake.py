from turtle import Turtle



# colors = ["red", "blue", "green","pink","orange"]

{# My attempt of creating starting snake
# snake_list = []

# start_pos_x = -40
# for new_snake_part in range(0,3):
#     start_pos_x += 20
#     new_snake = Turtle(shape="square")
#     new_snake.color("white")
#     new_snake.penup()
#     new_snake.teleport(x=start_pos_x)
#     snake_list.append(new_snake)
}

{# Create snake with colors
# for i in range(len(STARTING_POSITION)):
#     new_segment = Turtle("square")
#     new_segment.penup()
#     new_segment.color(colors[i])  # Access color by index
#     new_segment.goto(STARTING_POSITION[i])  # Access position by index
#     segments.append(new_segment)
}
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0),(-60,0),(-80,0)]
MOVE_DISTANCE = 20

# Snake Class
class Snake:

    def __init__(self):
        self.segments = []
        self.adam()
        self.head = self.segments[0]
    
    
      
    def adam(self):
        """start of the game, creates 3 snakesegments according starting_position tuples"""
        for position in STARTING_POSITION: 
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())        
       
    def move(self):
        """Starts from the bottom of total number of snake segments(picks last - 1) and makes it go to the next one"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() 
            new_y = self.segments[seg_num - 1].ycor() 
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def getheadingreading(self):
        print(self.head.heading)


    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.segments[0].setheading(90)
                

    def down(self):
        if self.segments[0].heading() == 90:
            pass
        else:
           self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() == 0:
            pass
        else:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() == 180:
            pass
        else:
            self.segments[0].setheading(0)
        

    