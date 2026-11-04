############# SMRITHI NADAMULURI GAMES ##############################
# DROP'EM APPLES LEADERBOARD
#####################################################################

#----- leaderboard configuration -----

# set the maximum number of players on the leaderboard
max_players = 5

#----- get player names from leaderboard file -----

def get_names(file_name):

    # open the leaderboard file so we can read it
    leaderboard_file = open(file_name, "r")

    # create an empty list to store player names
    names = []

    # go through the file one line at a time
    for line in leaderboard_file:

        # create an empty string to store the player's name
        leader_name = ""
        index = 0

        # use a while loop to read the name until the comma
        while line[index] != ",":
            leader_name = leader_name + line[index]
            index = index + 1

        # add the player's name to the names list
        names.append(leader_name)

    # close the leaderboard file
    leaderboard_file.close()

    # return the completed names list
    return names
