border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Driver Name Formatter"
'''
Concepts: String Methods
Task: Write a function format_driver_name(name) that converts a driver’s name to title case.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
name = "cArLoS sAinZ"
def format_driver_name(name):
    name = name.title()
    return name

name = format_driver_name(name)
print(name)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Team Chant Generator"
'''
Concepts: String Repetition
Task: Write a function generate_chant(team_name) that prints the team name repeated three times, separated by commas, with "!" at the end.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_name = "Barça"

def generate_chant(team_name):
    chant = f"{team_name}, {team_name}, {team_name}!"
    return chant

chant = generate_chant(team_name)
print(chant)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Match Score Formatter"
'''
Concepts: String Concatenation
Task: Write a function format_match_score(team1, team2, score1, score2) that formats a match result into a readable string.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team1 = "Barça"
team2 = "Real Madrid"
score1 = 3
score2 = 1

def format_match_score(team1,team2,score1,score2):
    message = f"{team1} {score1} - {score2} {team2}"
    return message

match_score = format_match_score(team1,team2,score1,score2)

print(match_score)

linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Dynamic Driver Introduction"
'''
Concepts: String Formatting
Task: Write a function introduce_driver(driver_name, team) that returns a formatted string introducing the driver and their team.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_name = "Lewis Hamilton"
team = "Ferrari"

def introduce_driver(driver_name, team):
    return f"{driver_name} drives for {team}."

message = introduce_driver(driver_name, team)

print(message)


linebreak()
print_border(level,item, "End")
linebreak()

item = "Name Validator"
'''
Concepts: Input Validation, String Methods
Task: Write a function validate_name(player_name) that:
- Takes a player’s name.
- Validates if it contains only alphabetic characters.
- Returns the name in title case or prints an error message if invalid.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def validate_name(name):
    if name.isalpha():
        return name.title()  # Use title case
    else:
        print("Please input letters only")
        return None  # Return None for invalid input

while True:
    name = input("Input your name: ")
    validated_name = validate_name(name)  # Pass name to the function
    if validated_name:  # Check if validation was successful
        print(validated_name)
        break

linebreak()
print_border(level,item, "End")
linebreak()

item = "Match Summary Formatter"
'''
Concepts: String Methods, Formatting
Task: Write a function format_match_summary(team1, team2, goals_team1, goals_team2) that:
- Formats the match result into a multi-line string using f-strings.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team1 = "Barça"
team2 = "Sevilla"
goals_team1 = 3
goals_team2 = 0

def format_match_summary(team1, team2, goals_team1, goals_team2):
    winner = ""
    if goals_team1 < goals_team2:
        winner = team2
    else:
        winner = team1
    message = f"""
    Match Summary:
    {team1}: {goals_team1}
    {team2}: {goals_team2}
    Result: {winner} wins!
    """
    return message

message = format_match_summary(team1, team2, goals_team1, goals_team2)
print(message)

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Dynamic Fixture Generator"
'''
Concepts: String Formatting, Loops
Task: Write a function generate_fixtures(team_name, opponents) that takes a team name and a list of opponents and generates a formatted fixture list.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_name = "Barça"
opponents = ["Real Sociedad", "Sevilla", "Las Palmas"]

def generate_fixtures(team_name, opponents):
    fixtures = f"Upcoming fixtures for {team_name}:"
    for idx, fixture in enumerate(opponents, start=1):
        fixtures +=  f"{idx}. {team_name} vs {fixture}\n"
    
    return fixtures
print(generate_fixtures(team_name, opponents))

linebreak()
print_border(level,item, "End")
linebreak()

item = "Scoreboard Formatter"
'''
Concepts: String Manipulation, Loops
Task: Write a function format_scoreboard(scores) that takes a dictionary of teams and their scores and returns a formatted scoreboard.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
scores = {"Barça": 3, "Real Madrid": 1, "Atletico Madrid": 0}
def format_scoreboard(scores):
    for team, score in scores.items():
        print(f"{team}: {score} points")
        
format_scoreboard(scores)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Post-Match Interview Formatter"
'''
Concepts: String Formatting, Input Validation
Task: Write a function post_match_interview(driver_name, position, team) that:
Returns a formatted post-match statement based on the driver’s position.
Positions:
1: "Amazing race! [Driver Name] wins for [Team]!"
Top 3: "Great effort! [Driver Name] finishes on the podium for [Team]."
Other: "Keep pushing! [Driver Name] finishes [Position] for [Team]."
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_name = "Carlos Sainz jr"  
position = 2  
team = "williams racing"  

def validate_name(name):
    if all(x.isalpha() or x.isspace() for x in name):
        name = name
    else:
        name = input("Please input valid name using only alphabets or spaces.")
    return name.title()

def validate_position(position):
    if type(position) == int:
        position = position
    else:
        position = input("Please input valid position using only integers")
    return position

def validate_team(team):
    if all(x.isalpha() or x.isspace() for x in team):
        team = team
    else:
        team = input("Please input valid name using only alphabets or spaces.")
    return team.title()
        
def post_match_interview(name,position,team):
    validate_name(name)
    validate_position(position)
    validate_team(team)
    
    if position == 1:
        return f"Amazing race! {name} wins for {team}!"
    
    if 1 < position <= 3:
        return f"Great effort! {name} finishes on the podium for {team}."
    else:
        return f"Keep pushing! {name} finishes {position} for {team}."

outcome = post_match_interview(driver_name, position, team)

print(outcome)

linebreak()
print_border(level,item, "End")
linebreak()