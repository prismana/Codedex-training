"""
As a data analyst for the Kansas City Chiefs you have been given a dataset containing information about the players, their positions, and some game statistics.

Let's start analyzing!

-> Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name,' 'position,' and 'jersey number.'
-> Print out a list of all player positions in the dataset.
-> Choose a player and update their game statistics in the dataset.
-> Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.
"""
# Make a dict of player
player1 = {'name': 'Alonso',
           'position': 'Kipper',
           'jersey_number': '9'}
player2 = {'name': 'Qabi',
           'position': 'Back',
           'jersey_number': '5'}

# Make list of dictonary
my_team = [player1, player2]

# Updating player1
my_team[0]['name'] = 'Samuel'
print(my_team[0]['name'])


