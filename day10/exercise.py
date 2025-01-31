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
drivers = ["Carlos Sainz", "Charles Leclerc", "Lewis Hamilton"]

lap_times = [
    [78.5, 79.2, 80.3],  # Carlos Sainz
    [81.1, 80.0, 79.5],  # Charles Leclerc
    [82.0, 81.2, 80.7]   # Lewis Hamilton
]
for driver in drivers:
    index =  drivers.index(driver)
    print(f"{driver}: {lap_times[index]}")

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

for player, stats in team_goals.items():
    print(f"{player}: {stats['goals']} goals, {stats['assists']} assists")


linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Performance Summary"
'''
Concepts: Nested Lists, Loops
Task: Write a function driver_summary(drivers, lap_times) that takes a list of drivers and their nested lap times and prints a summary for each driver
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def driver_summary(drivers_list, lap_times_list):
    for driver in drivers_list:
        idx =  drivers_list.index(driver)
        avg_lap = sum(lap_times_list[idx])/len(lap_times_list[idx])
        fastest_lap = min(lap_times_list[idx])
        print(f"{driver}: Average Lap Time: {avg_lap:.3f}, Fastest Lap: {fastest_lap}")

driver_summary(drivers, lap_times)
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

def analyze_fixtures(fixtures):
    for match, result in fixtures.items():
        values = list(result.values())
        keys = list(result.keys())
        message = match
        if values[0] >  values[1]:
            message += f": {keys[0]} wins!"
        elif values[0] < values[1]:
            message += f": {keys[1]} wins!"
        else:
            message += f": Draw!"
        print(message)
    
analyze_fixtures(fixtures)


linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Stats Comparison"
'''
Concepts: Nested Dictionaries, Loops
Task: Write a function compare_driver_stats(driver_stats) that:
- Takes a dictionary where each key is a driver and its value is another dictionary with stats like "team", "points", and "penalties".
- Compares and prints the driver with the most points.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_stats = {
    "Carlos Sainz": {"team": "Williams", "points": 210, "penalties": 0},
    "Charles Leclerc": {"team": "Ferrari", "points": 240, "penalties": 5},
    "Lewis Hamilton": {"team": "Ferrari", "points": 210, "penalties": 10}
}
def compare_driver_stats(driver_stats):
    top_driver = ""
    top_points = 0
    for driver, info in driver_stats.items():  # Use .items() to get key-value pairs
        final_points = info["points"] - info["penalties"]
        if final_points > top_points:
            top_driver = driver
            top_points = final_points

    print(f"{top_driver} from {driver_stats[top_driver]['team']} has the most points: {top_points}")

compare_driver_stats(driver_stats)
        
        

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

def find_top_scorer(team_goals):
    top_scorer = ""
    top_goals = 0
    for player, stats in team_goals.items():
        if stats["goals"] > top_goals:
            top_scorer = player
            top_goals = stats["goals"]
    print(f"Top Scorer: {top_scorer} with {top_goals} goals.")
    
find_top_scorer(team_goals)


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
points = [15, 13, 9, 10]
def rank_teams(teams, points):
    # 1. Combine and sort
    team_points = list(zip(teams, points))  # Combine teams and points
    team_points.sort(key=lambda item: item[1], reverse=True)  # Sort by points

    # 2. Assign ranks
    ranks = {}
    rank = 1
    for team, _ in team_points:
        ranks[team] = {'points': points[teams.index(team)], 'rank': rank}  # Include original points
        rank += 1

    return ranks

ranked_teams = rank_teams(teams, points)
print(ranked_teams)

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

def analyze_fixtures(fixtures):
    for match, result in fixtures.items():
        team1, team2 = list(result.keys())  # Get team names
        score1, score2 = list(result.values())  # Get scores

        if score1 > score2:
            winner = team1
            points_earned = 3
        elif score1 < score2:
            winner = team2
            points_earned = 0  # 0 points for a loss
        else:
            winner = "Draw"
            points_earned = 1  # 1 point for a draw

        print(f"{match}: {winner} wins! (Points Earned: {points_earned})")

analyze_fixtures(fixtures)
    


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

def find_top_scorer(team_goals):
    top_scorer = ""
    top_goals = 0
    top_assister =""
    top_assists = 0
    for player, stats in team_goals.items():
        if stats["goals"] > top_goals:
            top_scorer = player
            top_goals = stats["goals"]
        
        if stats["assists"] > top_assists:
            top_assister = player
            top_assists = stats["assists"]

    print(f"Top Scorer: {top_scorer} with {top_goals} goals.")
    print(f"Top Playmaker: {top_assister} with {top_assists} assists.")
        
    
find_top_scorer(team_goals)


linebreak()
print_border(level,item, "End")
linebreak()