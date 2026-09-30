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
pencil.speed(0)
answer = "m"

# Welcome the user and ask them what they want to draw 
while (answer != "q"):
  answer = turtle.textinput("Welcome to the digital coloring book, what would you like to color!", "mushroom(m) or flower(f) or tree(t)")
  """
  ###########MUSHROOM####################
  if answer == "m":
    # Add code for creating a mushroom and its user inputs
    ground_colors=["OliveDrab4", "bisque4"]
    pencil.penup()
    pencil.goto(-500, -200)
    pencil.setheading(0)
    pencil.pendown()
    ground = "a"
    while(ground != "g" and ground != "b"):  
        ground = turtle.textinput("Ground Color", "Choose the color of the ground (Green(g), Brown(b):").lower()
      
      # draw the rectangle for the ground
    if ground=="g":
        ground_color = ground_colors[0]
    else:  
        ground_color = ground_colors[1]

    pencil.fillcolor(ground_color)  
    pencil.begin_fill()
    pencil.forward(1000)   
    pencil.right(90)      
    pencil.forward(200)   
    pencil.right(90)      
    pencil.forward(1000)  
    pencil.right(90)      
    pencil.forward(200)   
    pencil.end_fill()

      # draw the sky for the background
    sky_colors = ["LightBlue2", "SteelBlue4"]
    sky = "a"
    while sky != "l" and sky != "s":
        sky = turtle.textinput("Sky Color", "Choose the sky color (Light Blue(l), Steel Blue(s)):").lower()
      # draw the big rectangle for the sky 
    if sky == "l":
          sky_color = sky_colors[0]
    else:
          sky_color = sky_colors[1]

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
      
    # draw the mushroom stem
    pencil.penup()
    pencil.goto(-30, -200)      
    pencil.setheading(0)        
    pencil.pendown()
    pencil.fillcolor("darksalmon")
    pencil.begin_fill()
    pencil.forward(70)         
    pencil.left(90)
    pencil.forward(130)         
    pencil.left(90)
    pencil.forward(70)
    pencil.left(90)
    pencil.forward(130)
    pencil.end_fill()
      # draw the mushroom top
    top_color_options = ["brown3", "darkorchid4"]
    top = "a"
    while top != "b" and top != "d":
      top = turtle.textinput("Top Color", "Choose the color of the cap (Brown(b), Dark Orchid(d)):").lower()
    #draw teh semi circle at the top of the stem
    if top == "b":
      top_color = top_color_options[0]
    else:
      top_color = top_color_options[1]
    pencil.penup()
    pencil.goto(117, -80)        
    pencil.setheading(90)      
    pencil.pendown()
    pencil.fillcolor(top_color) 
    pencil.begin_fill()
    pencil.circle(120, 180)   
    pencil.goto(117, -80)           
    pencil.end_fill()
      #add teh white dots in the mushroom
      #use a circle turtle and stamp it
    pencil.penup()
    pencil.shape("circle")     
    pencil.color("white")       
    pencil.shapesize(1.5)       
    pencil.goto(-60,-20)
    pencil.stamp()
    pencil.goto(90,-60)
    pencil.stamp()
    pencil.goto(40,-15)
    pencil.stamp()
    pencil.goto(5,2)
    pencil.stamp()
    pencil.goto(-80,-55)
    pencil.stamp()
    pencil.goto(-15,-55)
    pencil.stamp()
  ########## END MUSHROOM #######################

  
  
  ############FLOWER######################################
  if answer == "f":
    #add code for flower and its user input
    #color options for the ground 
     ground_colors=["OliveDrab4", "bisque4"]
     pencil.penup()
     pencil.goto(-500, -200)
     pencil.setheading(0)
     pencil.pendown()
     ground = "a"
     while(ground != "g" and ground != "b"):  
        ground = turtle.textinput("Ground Color", "Choose the color of the ground (Green(g), Brown(b):").lower()
      
      # draw the rectangle for the ground
     if ground=="g":
        ground_color = ground_colors[0]
     else:  
        ground_color = ground_colors[1]

     pencil.fillcolor(ground_color)  
     pencil.begin_fill()
     pencil.forward(1000)   
     pencil.right(90)      
     pencil.forward(200)   
     pencil.right(90)      
     pencil.forward(1000)  
     pencil.right(90)      
     pencil.forward(200)   
     pencil.end_fill()

      # draw the sky for the background
     sky_colors = ["LightBlue2", "SteelBlue4"]
     sky = "a"
     while sky != "l" and sky != "s":
        sky = turtle.textinput("Sky Color", "Choose the sky color (Light Blue(l), Steel Blue(s)):").lower()
      # draw the big rectangle for the sky 
     if sky == "l":
          sky_color = sky_colors[0]
     else:
          sky_color = sky_colors[1]

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

     #actually creating the parts of the flower
     # stem
     pencil.color("chartreuse4")
     pencil.pensize(30)
     pencil.penup()
     pencil.goto(0, -230)
     pencil.pendown()
     pencil.setheading(90)
     pencil.forward(200)
     #  leaf
     pencil.setheading(270)
     pencil.circle(20, 120, 20)
     pencil.setheading(90)
     pencil.goto(0, -60)
     #draw the petals and this part requires user input
     # change pen
     petal_colors=["plum1", "MediumPurple1"]
     petal = "a"   
     while(petal != "p" and petal != "m"):
           petal = turtle.textinput("Ground Color", "Choose the color of the petal (pink(p), purple(m):").lower()
     if petal=="p":
             petal_color = petal_colors[0]
     else:  
             petal_color = petal_colors[1]
     pencil.penup()
     pencil.shape("circle")
     pencil.turtlesize(3.5)  
     pencil.color(petal_color)
     pencil.goto(-70,40)
     for petal in range(13):
      pencil.right(30)
      pencil.forward(40)
      pencil.stamp()
      pencil.penup()

  #the yellow part in the middle

  pencil.goto(1,20)
  pencil.pendown()
  pencil.color("khaki1")
  pencil.turtlesize(4.7)
  pencil.stamp()

###########ENDFLOWER#####################################################
"""

###########TREE###########################################
  if answer == "t":
      #add code for the tree and its user input
          #color options for the ground 
      ground_colors=["OliveDrab4", "bisque4"]
      pencil.penup()
      pencil.goto(-500, -200)
      pencil.setheading(0)
      pencil.pendown()
      ground = "a"
      while(ground != "g" and ground != "b"):  
        ground = turtle.textinput("Ground Color", "Choose the color of the ground (Green(g), Brown(b):").lower()
      
      # draw the rectangle for the ground
      if ground=="g":
        ground_color = ground_colors[0]
      else:  
        ground_color = ground_colors[1]

      pencil.fillcolor(ground_color)  
      pencil.begin_fill()
      pencil.forward(1000)   
      pencil.right(90)      
      pencil.forward(200)   
      pencil.right(90)      
      pencil.forward(1000)  
      pencil.right(90)      
      pencil.forward(200)   
      pencil.end_fill()

      # draw the sky for the background
      sky_colors = ["LightBlue2", "SteelBlue4"]
      sky = "a"
      while sky != "l" and sky != "s":
        sky = turtle.textinput("Sky Color", "Choose the sky color (Light Blue(l), Steel Blue(s)):").lower()
      # draw the big rectangle for the sky 
      if sky == "l":
          sky_color = sky_colors[0]
      else:
          sky_color = sky_colors[1]

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
  
else:
  answer = turtle.textinput("Do you want to color again?","Quit(q) or Continue(c)")
  answer = turtle.textinput("Do you want to color again?","Quit(q) or Continue(c)")  
wn.bye()

wn.mainloop()



