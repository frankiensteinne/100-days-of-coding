border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Goal Event"
'''
Task: Create a function goal_event() that takes two team names as arguments. Randomly select a team to score a goal and print a message like "[Team name] scores a goal!".

Expected Output: A message indicating which team scored.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

item = "Card Event"
'''
Task: Create a function card_event() that takes a player's name as an argument. Randomly select a card type ("yellow" or "red") and print a message like "[Player name] receives a [card type] card!".

Expected Output: A message indicating which player received a card and the card type.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

item = "Substitution Event"
'''
Task: Create a function substitution_event() that takes two player names as arguments (player out, player in). Print a message like "[Player out] is substituted by [Player in].".

Expected Output: A message indicating the substitution. 
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Match Commentary"
'''
Task: Create a function match_commentary() that simulates a short segment of a match. Use a loop to generate 3 random events (goal, card, or substitution) and print commentary for each event.

Expected Output: A sequence of 3 random match events with commentary.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

item = "Foul Generator"
'''
Task: Create a function foul_generator() that takes a list of players as an argument. Randomly select a player from the list and determine if a foul was committed (50% chance). If a foul is committed, use the card_event() function from the "Base" exercises to determine the card type.

Expected Output: A message indicating if a foul was committed and, if so, which player received a card and the card type.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

item = "Goal Probability"
'''
Task: Create a function goal_probability() that takes two team names and their respective attack ratings (numbers between 1 and 10) as arguments. Generate a random number between 1 and 100. If the random number is less than or equal to the team's attack rating, that team scores a goal. Print a message indicating the outcome.

Expected Output: A message indicating if a team scored based on their attack rating.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Full Match Simulation"
'''
Task: Combine the functions from the previous exercises to create a program that simulates a full football match. The program should generate random events (goals, cards, substitutions) throughout the match and keep track of the score.

Expected Output: A simulation of a football match with a final score.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

item = "Match Statistics"
'''
Task: Extend the "Full Match Simulation" to track and display match statistics, such as the number of goals, shots, cards, and possession percentage for each team.

Expected Output: A match simulation with detailed statistics.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

item = " League Simulation"
'''
Task: Create a program that simulates a league with 4 teams. Each team plays each other once. Use the Full Match Simulation function to simulate the matches and keep track of the league table. At the end, print the final league standings.

Expected Output: A simulation of a league with final standings.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()