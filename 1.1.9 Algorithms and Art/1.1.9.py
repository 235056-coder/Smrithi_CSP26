#119 Summative 
#start by creating a custon turtle shape
import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# define coordinates for a custom shape
custom_polygon = ((-6, 11), (6, 11), (6, -4), (0, -11), (-6, -4), (-6, 11))

# register the new custom shape and name it "pencil"
wn.register_shape("pencil", custom_polygon)

# create your turtle and apply the shape (named 'pencil' to match your drawing commands)
pencil = turtle.Turtle()
pencil.shape("pencil")
pencil.color("black")
pencil.fillcolor("khaki1")
pencil.speed(2)

# Welcome the user and ask them what they want to draw 
answer = turtle.textinput("Welcome to the digital coloring book, what would you like to color!", "mushroom(m) or flower(f) or tree(t)")

if answer == "m":
    # Add code for creating a mushroom and its user inputs
 
    pencil.penup()
    pencil.goto(-500, -200)
    pencil.setheading(0)
    pencil.pendown()  
    ground = turtle.textinput("Ground Color", "Choose the color of the ground (OliveDrab4, bisque4):")
    
    # draw the rectangle for the ground
    if ground: 
        pencil.fillcolor(ground)  
        pencil.begin_fill()
        pencil.forward(1000)   
        pencil.right(90)      
        pencil.forward(200)   
        pencil.right(90)      
        pencil.forward(1000)  
        pencil.right(90)      
        pencil.forward(200)   
        pencil.end_fill()

    # draw the sky for the backround
    sky_color = turtle.textinput("Sky Color", "Choose the sky color (LightBlue2, SteelBlue4):")
    if sky_color:
        pencil.penup()
        pencil.goto(-500, -200) 
        pencil.setheading(0)   
        pencil.pendown()
        pencil.fillcolor(sky_color)
        pencil.begin_fill()
        pencil.forward(1000)   
        pencil.left(90)        
        pencil.forward(600)     
        pencil.left(90)        
        pencil.forward(1000)   
        pencil.left(90)         
        pencil.forward(600)     
        pencil.end_fill()
    

    

    
wn.mainloop()


 

"""
if answer == "f":
  #add code for flower and its user input

if answer == "t":
  #add code for the tree and its user input
"""