from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600,height=500)
user_input = screen.textinput(title="Make you bet",prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
# sido = Turtle(shape="turtle")
# sido.penup()
# sido.teleport(x=-280,y=0)
y0=0

turtles = {}
for color in colors:
     t = Turtle()
     t.color(color)
     t.shape('turtle')
     t.teleport(x=-280,y=-150+y0)
     y0 +=60
     turtles[color] = t

if user_input:
     is_race_on = True

while is_race_on:
     
     for color in colors:
          if turtles[color].xcor()> 260:
               is_race_on = False
               winning_turtle = color
               if winning_turtle == user_input:
                    print(f"You've won! the {winning_turtle} is the winner")
               else:
                    print(f"You've Lost! the {winning_turtle} is the winner")
          random_distance = random.randint(0,15)
          turtles[color].fd(random_distance)


print(5)
screen.exitonclick()