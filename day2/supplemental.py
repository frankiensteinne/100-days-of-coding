border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)

level = "Base"

item = "Player Introduction"
'''
Task:  Write a program that takes a player's first and last name as input and prints a message like, "Welcome to the team, [first name] [last name]!". 
Expected Output: "Welcome to the team, [first name] [last name]!"
'''

print_border(level,item, "Start")
#Enter your code below this line
first_name = input("What is your first name?:\n\t").title()
last_name= input("What is your last name?:\n\t").title()

print(f"Welcome to the team, {first_name} {last_name}!")

print_border(level,item, "End")

item = "Race Position"
'''
Task: Write a program that takes a driver's name and their finishing position as input and prints a message like, "[Driver's name] finished the race in [position] place!". 
Expected Output: "[Driver's name] finished the race in [position] place!"
'''

print_border(level,item, "Start")
#Enter your code below this line
driver_name = input("What is the driver's name?: ").title()
ordinal_position = input("Where did he placed?: ")

print(f"{driver_name} finished the race in {ordinal_position} place!")
print_border(level,item, "End")


level = "Comfortable"

item = "Goal Celebration"
'''
Task: Write a program that takes a player's name and the number of goals they scored as input. Print a message like, "[Player's name] scored [number] goals! ¡Visca el Barça!". Use f-strings for formatting.

Expected Output: "[Player's name] scored [number] goals! ¡Visca el Barça!"
'''

print_border(level,item, "Start")
#Enter your code below this line
player_name = input("Input player's name: ").title()
goals = input("How many goals did they scored?: ")

print(f"{player_name} scored {goals} goals!\n¡Visca el Barça!")

print_border(level,item, "End")

item = "Fastest Lap"
'''
Task: Write a program that takes a driver's name and their fastest lap time as input. Print a message like, "[Driver's name] set the fastest lap with a time of [lap time]!". Use f-strings for formatting.

Expected Output: "[Driver's name] set the fastest lap with a time of [lap time]!"
'''

print_border(level,item, "Start")
#Enter your code below this line
driver_name = input("What is the driver's name?: ").title()
lap_time = input("Input lap time in seconds: ")

print(f"{driver_name} set the fastest lap with a time of {lap_time} seconds!")

print_border(level,item, "End")


level = "More Comfortable"

item = "Team Chant"
'''
Task: Write a program that takes a team name as input and creates a chant by repeating the team name three times, separated by commas and an exclamation mark at the end. Then, convert the chant to uppercase.

Expected Output: "[TEAM NAME], [TEAM NAME], [TEAM NAME]!" (all uppercase)
'''

print_border(level,item, "Start")
#Enter your code below this line
team_name = input("What is your team's name?: ").upper()

print(f'{team_name}, {team_name}, {team_name}!')
print_border(level,item, "End")

item = "Driver Lineup"
'''
Task: Write a program that takes the names of three drivers as input. Create a formatted string that lists the drivers separated by " | " and adds " - 2025 F1 Season" at the end.

Expected Output: "[Driver 1] | [Driver 2] | [Driver 3] - 2025 F1 Season"
'''

print_border(level,item, "Start")
#Enter your code below this line
driver1 = input("Input driver name: ").title()
driver2 = input("Input driver name: ").title()
driver3 = input("Input driver name: ").title()

print(f'{driver1} | {driver2} | {driver3} - 2025 F1 Season')
print_border(level,item, "End")