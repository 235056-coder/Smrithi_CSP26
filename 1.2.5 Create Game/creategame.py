############# SMRITHI NADAMULURI GAMES ##############################
# creategame.py
#####################################################################

#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
screen_width = 765
screen_height = 785
background_image = "appletree.gif"
apple_image = "applesingle.gif"


letter_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
current_letter = ""
letter_font = ("Courier New", 30, "bold")

wn = trtl.Screen()
wn.setup(width=screen_width, height=screen_height)
wn.bgpic(background_image)
wn.addshape(apple_image)

apple = trtl.Turtle()
apple.shape(apple_image)
apple.hideturtle()
apple.penup()
apple.goto (-300,100)
apple.pendown()
apple.showturtle()

letter_writer = trtl.Turtle()
letter_writer.hideturtle()
letter_writer.penup()
letter_writer.color("white")

#-----initialize turtle-----


#-----game functions--------
def draw_letter():
    global current_letter

    current_letter = rand.choice(letter_list)

    letter_writer.goto(apple.xcor() - 10, apple.ycor() - 10)
    letter_writer.write(current_letter, font=letter_font)

#-----events----------------
wn.listen()
trtl.mainloop()


#username entry

#check the letter to see if it matches
#the apple falls
#reset the apple to a new random spot with a new letter
#bind keys
#create timer
#create a score counter
#track the score in teh text file
#present leaderboard



#other things that are needed are:
#leaderboard text file
#the gif of the apple and scene and any character that I might add

