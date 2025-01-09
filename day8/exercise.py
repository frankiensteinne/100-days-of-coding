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


linebreak()
print_border(level,item, "End")
linebreak()

item = "Goal Celebration Validator"
'''
Concepts: Input Validation, String Methods
Task: Write a function validate_goal_celebration(player_name) that:
- Takes a player’s name.
- Validates if it contains only alphabetic characters.
- Returns the name in title case or prints an error message if invalid.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
player_name = "Lewandowski2"


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
driver_name = "Carlos Sainz"  
position = 2  
team = "Ferrari"  


linebreak()
print_border(level,item, "End")
linebreak()