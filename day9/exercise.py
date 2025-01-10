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

for key, value in driver_stats.items():
    key = key.title()
    if type(value) == 'str':
        value = value.title()
    print(f"{key}: {value}")

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

team_goals["Ferran Torres"] = 3

print(team_goals)
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

driver_stats["points"] = 220

print(driver_stats)
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

def create_lap_times(drivers, times):
    driver_dict = {key: value for key, value in zip(drivers,times)}
    
    return driver_dict
    
new_dict = create_lap_times(driver_names, lap_times)
print(new_dict)


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

def sort_team_goals(dictionary_of_players):
    sorted_list = sorted(dictionary_of_players.items(), key=lambda x: x[1], reverse=True)
    return sorted_list


sorted_team_goals = sort_team_goals(team_goals)
print(sorted_team_goals)

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

def check_driver_pts(dictionary_of_driver_stats):
    status =""
    if 200 < dictionary_of_driver_stats["points"]:
        status = "Leader"
    elif 150 < dictionary_of_driver_stats["points"] <= 200:
        status = "Contender"
    else:
        status = "Midfield"
    
    return status

positions = check_driver_pts(driver_stats)
print(driver_stats["points"])
print(positions)        

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

def create_goal_report(players,goal_tally, assist_tally):
    goal_assist_dict = {a:{"goals":b, "assists":c} for (a,b,c) in zip(players, goal_tally, assist_tally)}
    return goal_assist_dict

GA_dict = create_goal_report(players, goals, assists)

print(GA_dict)

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
def analyze_driver_performance(driver_stats):
    if 250 < driver_stats["points"]:
        driver_stats["status"] = "Champion Contender"
    elif 150 < driver_stats["points"] <= 250:
        driver_stats["status"] = "Contender"
    else:
        driver_stats["status"] = "Midfield"
    return driver_stats
    
updated_driver_dict = analyze_driver_performance(driver_stats)
print(updated_driver_dict)
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
scores = [3, 0, 1]

def check_results(points):
    results = []
    for value in points:
        if value == 3:
           results.append('Win')
        elif value == 1:
            results.append('Draw')
        else:
            results.append('Lose')
    return results


def match_results_summary(team_list, points_list, results_list):
    match_summary = {a:{'points':b, 'results':c} for (a,b,c) in zip(team_list, points_list, results_list)}
    return match_summary
    
results = check_results(scores)
summary__dictionary = match_results_summary(teams,scores,results)
print(summary__dictionary)

linebreak()
print_border(level,item, "End")
linebreak()