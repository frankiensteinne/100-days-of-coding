border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Driver Greeting"
'''
Concepts: Defining and Calling Functions
Task: Write a function greet_driver(driver_name) that takes a driver’s name
Expected Output: Hello, [Driver Name]! Best of luck for the race!  
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_name = input("What is your name?: ").title()
def greet_driver(driver_name):
    print(f"Hello, {driver_name}! Best of luck for the race!")

greet_driver(driver_name)
linebreak()
print_border(level,item, "End")
linebreak()

item = "Function Parameters"
'''
Concepts: Function Parameters
Task: Write a function celebrate_goals(player_name, goals)
Expected Output: [Player Name] scored [Goals] goals! ¡Visca el Barça!  
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

goals_scorer = input("Input goalscorer: ")
goals_scored = input("Input number of goals scored: ")

def celebrate_goals(player=goals_scorer, goals=goals_scored):
    print(f"{player} scored {goals}. ¡Visca el Barça!")

celebrate_goals()

linebreak()
print_border(level,item, "End")
linebreak()

item = "Return Statement"
'''
Concepts: Return Statement
Task: Write a function add_numbers(num1, num2) that returns the sum of two numbers.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(3,7))
linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Lap Time Calculator"
'''
Concepts: Functions with Multiple Parameters
Task: Write a function lap_time(driver, time) that takes a driver’s name and their lap time
Output : [Driver Name] completed a lap in [Time] seconds.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def lap_time(driver,time_in_secs):
    print(f"{driver.title()} completed lap in {time_in_secs} seconds.")
    
lap_time("carlos sainz", 77.3)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Team Ranking"
'''
Concepts: Function with Conditional Logic
Task: Write a function compare_teams(team1, team2, score1, score2) that prints the match result
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def compare_teams(team1, team2, score1, score2):
    if score1 < score2:
        print(f"{team2} beats {team1}")
    elif score2 < score1:
        print(f"{team1} beats {team2}.")
    else:
        print("It's a tie.")
linebreak()
print_border(level,item, "End")
linebreak()

item = "Goal Scorer Tracker"
'''
Concepts: Function with a List Parameter
Task: Write a function count_player_goals(goal_scorers, player_name) that takes a list of scorers and counts how many goals a specific player scored.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
goal_scorers = ['Lewandowski', 'Pedri', 'Lewandowski']

def count_player_goals(goal_scorers, player_name):
        goal_count = goal_scorers.count(player_name)
        print(f"{player_name.title()} scored {goal_count} goals!")

count_player_goals(goal_scorers, 'Lewandowski')

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = ""
'''
Concepts: Functions, Loops
Task: Write a function assess_driver(driver_name, lap_times) that:
- Takes a driver’s name and a list of lap times.
- Returns their fastest lap and average lap time.

Extra Challenge: If the average lap time is below 80 seconds, print: [Driver Name] had an excellent performance!  
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
from random import uniform

driver_lap_times = []
number_of_laps = 10
for _ in range(number_of_laps):
  lap_time = round(uniform(75, 90), 3)
  driver_lap_times.append(lap_time)

def assess_driver(driver,lap_times):
    total_time = sum(driver_lap_times)
    average_lap = total_time/len(lap_times)
    fastest_lap = min(driver_lap_times)
    print(f"Average lap: {average_lap} secs\nFastest lap: {fastest_lap} secs")
    if fastest_lap < 80:
        print(f"{driver} had an excellent performance!")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Match Simulation with Functions"
'''
Concepts: Functions, Nested Loops
Task: Write a function simulate_matches(match_count) that:
- Simulates match_count matches, randomly generating scores for Barça and their opponent.
- Returns a summary of results (wins, losses, draws).
Extra Challenge: Pass a team_name parameter and simulate matches for different teams.

'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
from random import randint

def simulate_matches(match_count, team_name="Barça"):
    wins = 0
    losses = 0
    draws = 0

    for match_number in range(match_count):  # Corrected loop range
        team_goals = 0
        opp_goals = 0
        for _ in range(5):  # Simulating 5 scoring events per match
            scorer = randint(1, 2)  # 1 = team_name, 2 = Opponent
            if scorer == 1:
                team_goals += 1
            else:
                opp_goals += 1
        result = "WIN" if team_goals > opp_goals else "LOSS" if team_goals < opp_goals else "DRAW"
        print(f"Match {match_number+1}: {team_name} {team_goals} - {opp_goals} Opponent | {result}")

        if result == "WIN":
            wins += 1
        elif result == "LOSS":
            losses += 1
        else:
            draws += 1

    return wins, losses, draws  # Return the summary

# Example usage
match_count = 5
team_name = "Real Madrid"  # Example with a different team name
wins, losses, draws = simulate_matches(match_count, team_name)

print("\nMatch Summary:")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Draws: {draws}")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Goal Distribution Report"
'''
Concepts: Functions, Lists
Task: Write a function goal_report(goals_list) that:
- Takes a list of goal scorers.
- Returns a dictionary of players and their total goals.
Extra Challenge: Print the player with the highest number of goals
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
list_goal_scorers = ["Lewandowski", "Fermin Lopez", "Lamine Yamal", "Lewandowski", "Lewandowski"]

def goal_report(goals_list):
    goal_scorers_dict = {}
    for player in goals_list:
        if player in goal_scorers_dict:
            goal_scorers_dict[player] += 1
        else:
            goal_scorers_dict[player] = 1
    
    return goal_scorers_dict

print(goal_report(list_goal_scorers))


linebreak()
print_border(level,item, "End")
linebreak()