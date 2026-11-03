############# SMRITHI NADAMULURI GAMES ##############################
# creategame.py
#####################################################################

#-----Import Statements-----
import turtle as trtl
import random as rand
from functools import partial

# --- Configuration & Setup ---
#size of the screen 
screen_width = 765
screen_height = 785
#importing the images for the game
background_image = "appletree.gif"
apple_image = "apple1.gif"

#import a new image just for the title screen 
startscreen_image = "titlescreen.gif"

#how far the apple can fall to get the the position I want it to
ground_height = -300
#where the letter will be drawn on the apple picture
apple_letter_x_offset = -13
apple_letter_y_offset = -40

#before they enter their name the title screen will be displayed for 3 seconds before the game starts and then the title screen will be cleared and the game will start
wn = trtl.Screen()
wn.title ("Drop'em Apples")
wn.setup(width=screen_width, height=screen_height)
wn.addshape(apple_image)
wn.bgpic(startscreen_image)
wn.update()

#user puts in their name
player_name = trtl.textinput("Name", "Enter your name")

while "," in player_name or len(player_name)==0 or len(player_name)>12:
 player_name = trtl.textinput ("Name", "Please do not use a comma, Enter your name")


#screen set up for the ACTUAL game
wn.reset()
wn = trtl.Screen()
wn.title ("Drop'em Apples")
wn.setup(width=screen_width, height=screen_height)
wn.addshape(apple_image)
wn.bgpic(background_image)
#add a timer here 30sec
score = 0
font_setup = ("Courier New", 30, "bold", )
timer = 30
counter_interval = 1000
timer_up = False
wn.tracer(False)

#list of letters
letter_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

#initialize the turtle
apple = trtl.Turtle()
apple.speed(8)
apple.penup()
current_letter = ""

#have a score writr with the same text setteings as teh apple
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-350, 330)

#counter goes here
counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(180, 330)

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
    x_pos = rand.randint(-270,80)
    y_pos = rand.randint(-140,350)
    apple.goto(x_pos, y_pos)
    draw_apple(apple, current_letter)

def drop_apple():
    """makes he apple fall and then resets to a new position with a new letter"""
    wn.tracer(True)#this is turning all the animation back on from the tracer(Flase) from earlier
    apple.goto(apple.xcor(), ground_height) #might need to play around with this a little more
    apple.clear()
    #add mmore code here to update the score when the apple is dropped

    apple.hideturtle()
    wn.tracer(False) #again just turns the animation off so that the apple can reset without the player seeing all the movements
    reset_apple(apple)
    
def check_letter(pressed_letter):
    if not timer_up and current_letter == pressed_letter:
        update_score() #this placement makes it so that the score updates when the right letter is pressed instead of when it drops because that might be more fair for time purpose
        drop_apple()

#def global update the scorehere
def update_score():
    global score
    score += 1 
    score_writer.clear()
    score_writer.write("score: " + str(score), font=font_setup) #maybe i shouldnt add this if it doesnt look good. try bth versions and see wat fits better

#def countdown timer here and when the times up, teh screen will clear and the final score will be dispayed with a messagesaying game over, and there should be a button that takes you to the leaderboar(more like a question maybe)
def countdown():
    global timer, timer_up

    counter.clear()

    if timer <= 0:
        counter.write("time's up!", font=font_setup)
        timer_up = True
        apple.hideturtle()

    else:
        counter.write("timer: " + str(timer), font=font_setup)
        timer -= 1
        wn.ontimer(countdown, counter_interval)
#def start game function here that will start the game when the player clicks a button on the title screen, and then the title screen will clear and the game will start
def start_game():
    wn.ontimer(countdown, counter_interval) #this hasnt really cleared the screen yet but that can worked on after the basic functionality

# --- Key Bindings & Initialization ---
for letter in letter_list:
    wn.onkeypress(partial(check_letter, letter), letter) #got rid of the .lower so its now case sensitive.

# Start the game
reset_apple(apple)
update_score()
start_game()
wn.listen()
trtl.mainloop()
