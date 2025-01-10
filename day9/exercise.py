border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Driver Statistics"
'''
Concepts: Creating and Accessing Dictionaries
Task: Create a dictionary driver_stats with keys "name", "team", and "points". Print each value individually.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_stats = {
    "name": "Carlos Sainz",
    "team": "Williams Racing",
    "points": 180
    }


linebreak()
print_border(level,item, "End")
linebreak()

item = "Team Goal Scorers"
'''
Concepts: Adding Key-Value Pairs
Task: Create a dictionary team_goals with initial scorers and their goal counts. Add a new player "Ferran Torres" with 3 goals and print the updated dictionary.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_goals = {"Lewandowski": 10, "Pedri": 5}


linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Profile Update"
'''
Concepts: Modifying Dictionary Values
Task: Update "points" in the driver_stats dictionary to reflect a new value of 200. Print the updated dictionary.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_stats = {
    "name": "Carlos Sainz",
    "team": "Williams Racing",
    "points": 180
    }

linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Lap Time Dictionary"
'''
Task: Write a function create_lap_times(drivers, times) that takes two lists (driver names and their lap times) and creates a dictionary with driver names as keys and lap times as values.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_names = ["Carlos Sainz", "Charles Leclerc", "Lewis Hamilton"]  
lap_times = [78.2, 79.5, 80.3]  


linebreak()
print_border(level,item, "End")
linebreak()

item = "Team Goal Leaderboard"
'''
Concepts: Sorting Dictionary Values
Task: Write a function sort_team_goals(team_goals) that returns the players sorted by their goal counts in descending order.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_goals = {
    "Lewandowski": 10,
    "Pedri": 5,
    "Ferran Torres": 3
    }


linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Points Checker"
'''
Concepts: Conditional Logic with Dictionaries
Task: Write a function check_driver_points(driver_stats) that:
- Checks if the driver has more than 200 points.
- Prints "Leader" if true, "Contender" for points between 150–200, and "Midfield" otherwise.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Goal Distribution Report"
'''
Concepts: Nested Dictionaries, Loops
Task: Write a function create_goal_report(players, goals) that:
- Creates a dictionary where each player is a key and their value is another dictionary containing "goals" and "assists".

'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
players = ["Lewandowski", "Pedri", "Ferran Torres"]  
goals = [10, 5, 3]  
assists = [7, 8, 4]  

linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Performance Analysis"
'''
Concepts: Dictionaries, Conditional Logic
Task: Write a function analyze_driver_performance(driver_stats) that:
- Checks if a driver’s points are above 250 and adds a "status" key with the value "Champion Contender".
- If points are between 150–250, sets "status" to "Contender".
Below 150, sets "status" to "Midfield".

'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()

item = "Match Result Summary"
'''
Concepts: Nested Dictionaries, Loops
Task: Write a function match_result_summary(teams, scores) that:
Takes two lists of teams and scores.
Returns a dictionary where each team is a key and their score is the value.
Adds a "result" key with "Win", "Loss", or "Draw" based on the score.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
teams = ["Barça", "Real Madrid", "Atletico Madrid"]  
scores = [3, 1, 1]  


linebreak()
print_border(level,item, "End")
linebreak()