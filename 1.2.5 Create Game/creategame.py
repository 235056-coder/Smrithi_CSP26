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
apple_image = "apple100.gif"
#how far the apple can fall to get the the position I want it to
ground_height = -400
#where the letter will be drawn on the apple picture
apple_letter_x_offset = -15
apple_letter_y_offset = -10

#screen set up
wn = trtl.Screen()
wn.setup(width=screen_width, height=screen_height)
wn.addshape(apple_image)
wn.bgpic(background_image)



# --- Game Functions ---

# --- Key Bindings & Initialization ---

# Start the game

trtl.mainloop()
