############# SMRITHI NADAMULURI GAMES ##############################
# creategame.py
#####################################################################

#-----import statements-----
import turtle as trtl


#-----game configuration----
screen_width = 765
screen_height = 785
background_image = "appletree.gif"
apple_image = "applesingle.gif"

#-----initialize turtle-----
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



#-----game functions--------


#-----events----------------
wn.mainloop()


#username entry
#create list of letters upper and lower (avoid.lower)
#initialize
#draw the letter on the apple
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
