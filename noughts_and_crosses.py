grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]
players = ['O', 'X']
next_player = 0



def get_next_character():
    """Returns the character for the next player"""
    global players
    global next_player
    #Get the next character
    next_character = players[next_player]
    #Update next_player
    if next_player == 1:
        next_player = 0
    elif next_player == 0:
        next_player = 1
    else:
        print("Prob in get_next_character")
    return players[next_player]


'''
#test get_next_character
for i in range(9):
    print(get_next_character())'''

print(grid)
