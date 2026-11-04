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

#----- get player scores from leaderboard file -----

def get_scores(file_name):

    # open the leaderboard file so we can read it
    leaderboard_file = open(file_name, "r")

    # create an empty list to store player scores
    scores = []

    # go through the file one line at a time
    for line in leaderboard_file:

        # create an empty string to store the player's score
        leader_score = ""
        index = 0

        # use a while loop to skip the player's name
        while line[index] != ",":
            index = index + 1

        # move past the comma to get to the score
        index = index + 1

        # use a while loop to read the score
        while index < len(line) and line[index] != "\n":
            leader_score = leader_score + line[index]
            index = index + 1

        # add the player's score to the scores list
        scores.append(int(leader_score))

    # close the leaderboard file
    leaderboard_file.close()

    # return the completed scores list
    return scores

#----- update leaderboard with new player -----

def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):

    # start at the end of the leaderboard
    index = len(leader_scores)

    # go through the existing scores to find where the new score belongs
    for i in range(len(leader_scores)):

        # check if the new score is higher than or equal to an existing score
        if player_score >= leader_scores[i]:

            # save the position where the new score belongs
            index = i
            break

    # insert the new player's name and score at the correct position
    leader_names.insert(index, player_name)
    leader_scores.insert(index, player_score)

    # checks if there are more than 5 players
    if len(leader_names) > max_players:

        # remove the last player from both lists so that only the top 5 remain
        leader_names.pop()
        leader_scores.pop()

    # opens the leaderboard file in write mode
    # "w" will update the file with the new leaderboard information because of the previous steps
    leaderboard_file = open(file_name, "w")

    # go through each player in the leaderboard
    for i in range(len(leader_names)):

        # write the player's name and score into the file
        # separate the name and score with a comma
        leaderboard_file.write(leader_names[i] + "," + str(leader_scores[i]) + "\n")

    # close the leaderboard file
    leaderboard_file.close()
