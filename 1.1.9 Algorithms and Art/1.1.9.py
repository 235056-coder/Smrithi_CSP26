#119 Summative 
#start by creating a custon turtle shape
import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Define coordinates for a custom shape (e.g., a diamond/star-like polygon)
# (0, 0) is the center point of your turtle

#Input your own coordinates here
custom_polygon = (((-6, 11), (6, 11), (6, -4), (0, -11), 
                  (-6, -4), (-6, 11)))

# Register the new custom shape and name it "mystar"
wn.register_shape("pencil", custom_polygon)

# Create your turtle and apply the shape
my_turtle = turtle.Turtle()
my_turtle.shape("pencil")
my_turtle.color("black")
my_turtle.fillcolor("khaki1")