border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Nested Lap Times"
'''
Concepts: Nested Lists, Accessing Elements
Task: Create a nested list of lap times for three drivers. Print the lap times for each driver.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
lap_times = [
    [78.5, 79.2, 80.3],  # Carlos Sainz
    [81.1, 80.0, 79.5],  # Charles Leclerc
    [82.0, 81.2, 80.7]   # Lewis Hamilton
]
drivers = ["Carlos Sainz", "Charles Leclerc", "Lewis Hamilton"]


linebreak()
print_border(level,item, "End")
linebreak()

item = "Team Goal Details"
'''
Concepts: Nested Dictionaries, Accessing Values
Task: Create a nested dictionary with players as keys and another dictionary containing "goals" and "assists" as values. Print each player’s details.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_goals = {
    "Lewandowski": {"goals": 10, "assists": 7},
    "Pedri": {"goals": 5, "assists": 8},
    "Ferran Torres": {"goals": 3, "assists": 4}
}


linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Performance Summary"
'''
Concepts: Nested Lists, Loops
Task: Write a function driver_summary(drivers, lap_times) that takes a list of drivers and their nested lap times and prints a summary for each dr
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
drivers = ["Carlos Sainz", "Charles Leclerc", "Lewis Hamilton"]  
lap_times = [
    [78.5, 79.2, 80.3],  
    [81.1, 80.0, 79.5],  
    [82.0, 81.2, 80.7]  
]

linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Fixture Results Analysis"
'''
Concepts: Nested Dictionaries, Loops
Task: Write a function analyze_fixtures(fixtures) that:
- Takes a nested dictionary where the key is the match (e.g., "Match 1") and the value is a dictionary containing teams and their scores.
- Prints the match result for each.

'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
fixtures = {
    "Match 1": {"Barça": 3, "Real Madrid": 1},
    "Match 2": {"Barça": 2, "Atletico Madrid": 2},
    "Match 3": {"Barça": 0, "Sevilla": 1}
}


linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Stats Comparison"
'''
Concepts: Nested Dictionaries, Loops
Task: Write a function compare_driver_stats(driver_stats) that:
- Takes a dictionary where each key is a driver and its value is another dictionary with stats like "team", "points", and "laps".
- Compares and prints the driver with the most points.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_stats = {
    "Carlos Sainz": {"team": "Williams", "points": 220, "laps": 30},
    "Charles Leclerc": {"team": "Ferrari", "points": 240, "laps": 32},
    "Lewis Hamilton": {"team": "Ferrari", "points": 200, "laps": 28}
}

linebreak()
print_border(level,item, "End")
linebreak()

item = "Top Scorer Analysis"
'''
Concepts: Nested Dictionaries, Loops
Task: Write a function find_top_scorer(team_goals) that identifies the top scorer based on the "goals" key.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_goals = {
    "Lewandowski": {"goals": 10, "assists": 7},
    "Pedri": {"goals": 5, "assists": 8},
    "Ferran Torres": {"goals": 3, "assists": 4}
}


linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Championship Standing Tracker"
'''
Task: Write a function track_championship_standings(teams, points) that:
- Creates a nested dictionary with teams as keys and their "points" and "rank" as values.
- Assigns ranks dynamically based on the points.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
teams = ["Barça", "Real Madrid", "Atletico Madrid", "Sevilla"]  
points = [12, 15, 9, 10]  


linebreak()
print_border(level,item, "End")
linebreak()

item = "Match-by-Match Performance Summary"
'''
Concepts: Nested Dictionaries, Loops
Task: Write a function match_performance_summary(fixtures) that summarizes match results and team performances.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
fixtures = {
    "Match 1": {"Barça": 3, "Real Madrid": 1},
    "Match 2": {"Barça": 2, "Atletico Madrid": 2},
    "Match 3": {"Barça": 0, "Sevilla": 1}
}


linebreak()
print_border(level,item, "End")
linebreak()

item = "Detailed Goal Analysis"
'''
Concepts: Nested Dictionaries, Loops
Task: Write a function detailed_goal_analysis(team_goals) that:
- Identifies the player with the most assists.
- Returns both the top scorer and top assist provider.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_goals = {
    "Lewandowski": {"goals": 10, "assists": 7},
    "Pedri": {"goals": 5, "assists": 8},
    "Ferran Torres": {"goals": 3, "assists": 4}
}

linebreak()
print_border(level,item, "End")
linebreak()