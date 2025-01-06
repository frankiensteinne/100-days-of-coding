border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Player Introduction"
'''
Concepts: Variables, String Concatenation
Task: Write a program that takes a player's first and last name as input and prints a message
Output: Welcome to the team, [First Name] [Last Name]!
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
player_fname = input("What is your first name?: ").title()
player_lname = input("What is your last name?: ").title()

print(f"Welcome to the team, {player_fname} {player_lname}!")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Statistics"
'''
Concepts: Variables, Numbers
Task: Create variables for a driver's name, their current wins, and the number of races they've participated in. 
Output: Carlos Sainz has won 2 races out of 10 total races.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_name = "Carlos Sainz"
races_win = 2
total_race = 10

print(f"{driver_name} has won {races_win} out of {total_race}.")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Whitespace Formatter"
'''
Whitespace Formatter

Concepts: String Manipulation (Tabs/Newlines)
Task: Write a program that prints the output below.
Output: 
   Himne del Barça  
   Més que un club  
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
print("\tHimne del Barça\n\tMés que un club")

linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Case Changes Practice"
'''
Concepts: String Case Changes
Task: Take input for a team name and print it in uppercase, lowercase, and title case.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_name = input("Input team name: ")
print(team_name.upper())
print(team_name.lower())
print(team_name.title())

linebreak()
print_border(level,item, "End")
linebreak()

item = "F1 Championship Points Calculator"
'''
Concepts: Variables, Basic Arithmetic
Task: Prompt the user for a driver’s points and calculate their championship standing-
Points Required for 1st: 500  
Example: Input = 420
Output: Carlos Sainz is 80 points away from 1st place!
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
pts_rqrd = 500
driver_inp = input("What is the name of the driver?: ").title()
driver_pts = int(input("How many points does the driver have?: "))
pts_needed = pts_rqrd - driver_pts

print(f"{driver_inp} is {pts_needed} away from 1st place!")

linebreak()
print_border(level,item, "End")
linebreak()

item = "F1 Pit Stop Analysis"
'''
Concepts: Float Numbers, f-strings
Task: Ask for three pit stop times (in seconds) and calculate the total and average pit stop time.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
pit_one = float(input("What is the first pit stop time?: "))
pit_two = float(input("What is the second pit stop time?: "))
pit_three = float(input("What is the third pit stop time?: "))

pit_total = pit_one + pit_two + pit_three
pit_average = pit_total/3

print(f"Total Pit Time: {pit_total}\n Average Pit Time: {pit_average}")

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Custom Team Greeting Formatter"
'''
Concepts: String Manipulation, Input Validation
Task: Prompt for a user’s name, team, and a custom message.
Challenge: Ensure proper capitalization of inputs.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
user_name = input("What is your name?: ").title()
user_team = input("Which team do you support?: ").title()
custom_message = f", vamos {user_team}!"

print(f"Welcome to {user_team}, {user_name}{custom_message}")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Goal Tracker"
'''
Concepts: Arithmetic, Variables
Task: Write a program that calculates how many more goals a player needs to reach 50 career goals.
Output: Robert Lewandowski has scored 35 goals. He needs 15 more goals to reach 50!
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
target_goal = 50
player_goals = 35
goal_difference =  target_goal-player_goals
goals_player = "Robert Lewandowski"

print(f"{goals_player} has scored {player_goals}. He needs {goal_difference} more goals to reach {target_goal}")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Lap Time Formatter"
'''
Concepts: String and Number Formatting
Task: Take input for a driver’s best lap time in seconds (e.g., 72.345) and print it as:
Best Lap Time: 1 minute, 12.345 seconds.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

lap_in_secs = float(input("Input driver lap in seconds: "))
num_of_mins = int(lap_in_secs // 60)  # Use floor division to get integer minutes
num_of_secs = lap_in_secs % 60  # Use modulo operator to get remaining seconds

# Format the output with correct singular/plural forms
minutes_str = "minute" if num_of_mins == 1 else "minutes"
seconds_str = "second" if num_of_secs == 1 else "seconds"

print(f"Best Lap Time: {num_of_mins} {minutes_str}, {num_of_secs:.3f} {seconds_str}")

linebreak()
print_border(level,item, "End")
linebreak()