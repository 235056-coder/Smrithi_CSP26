############# SMRITHI NADAMULURI GAMES ##############################
# creategame.py
#####################################################################

#-----Import Statements-----
import turtle as trtl
import random as rand

# --- Configuration & Setup ---
#size of the screen 
screen_width = 765
screen_height = 785
#importing the images for the game
background_image = "appletree.gif"
apple_image = "apple1.gif"
#how far the apple can fall to get the the position I want it to
ground_height = -400
#where the letter will be drawn on the apple picture
apple_letter_x_offset = -15
apple_letter_y_offset = -10

#screen set up
wn = trtl.Screen()
wn.title ("Drop'em Apples")
wn.setup(width=screen_width, height=screen_height)
wn.addshape(apple_image)
wn.bgpic(background_image)
wn.tracer(False)


#list of letters
letter_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

#initialize the turtle
apple = trtl.Turtle()
apple.penup()
current_letter = ""

# --- Game Functions ---
def draw_letter(apple, letter):
    """Draws the letter text over the apple."""
    apple.color("white")
    remember_position = apple.position()
    apple.setpos(apple.xcor() + apple_letter_x_offset, 
    apple.ycor() + apple_letter_y_offset)

    
    apple.write(letter, font=("Courier New", 60, "bold"))
    apple.setpos(remember_position)

def draw_apple(apple, letter):
    """Displays the apple turtle and draws the current letter."""
    apple.shape(apple_image)
    apple.showturtle()
    draw_letter(apple, letter)
    wn.update()

def reset_apple(apple):
    """picks a new random letter from the list and moves the apple to a new spot thats also random"""
    global current_letter
    if letter_list:
        #picka. random letter
        index = rand.randrange(len(letter_list))
        #when a letter is picked, pop it so that a its not repeated (could maybe change this if players cycle through all teh letters fast enough)
        current_letter = letter_list.pop(index)

        #change the spot of the apple(somewhere random ON THE TREE)
    x_pos = rand.randint(-370,150)
    y_pos = rand.randint(-140,380)
    apple.goto(x_pos, y_pos)
    draw_apple(apple, current_letter)

# --- Key Bindings & Initialization ---

# Start the game
reset_apple(apple)
wn.listen()
trtl.mainloop()
