border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)

level = "Base"
item = "Favorite Player."
'''
Task: Write a program that stores your favorite FC Barcelona player's name in a variable and prints a message like, "My favorite player is [player's name]."

Expected Output: "My favorite player is [player's name]." (e.g., "My favorite player is Pedri.")
'''

print_border(level,item, "Start")
#Enter your code below this line
player = input("Who is your favorite football player?\n").title()
print(f"My favorite player is {player}.")

print_border(level,item, "End")

item = "Favorite Driver. "
'''
Task: Write a program that stores your favorite F1 driver's name in a variable and prints a message like, "My favorite driver is [driver's name]."

Expected Output: "My favorite driver is [driver's name]." (e.g., "My favorite driver is Carlos Sainz.")
'''
print_border(level,item, "Start")
#Enter your code below this line

driver = input("Who is your favorite F1 driver?\n").title()
print(f"My favorite driver is {driver}.")

print_border(level,item, "End")

item = "Favorite F1 team."
'''
Task: Write a program that stores your favorite F1 team's name in a variable and prints a message like "I support [team's name] in F1." [cite: 502]

Expected Output: "I support [team's name] in F1." (e.g., "I support Ferrari in F1.")
'''

print_border(level,item, "Start")
#Enter your code below this line
team = input("Which team in F1 do you support?\n").title()
print(f"I support {team} in F1.")

print_border(level,item, "End")

level = "Comfortable"
item = "El Clasico"
'''
Task: Write a program that stores "FC Barcelona" in a variable and prints a message about the team. Then, change the variable's value to "Real Madrid" and print a message about the updated team.`

Expected Output:

"[First team name] is the best team in La Liga!"
"[Second team name] is also a good team."
'''

print_border(level,item, "Start")
#Enter your code below this line
first_team = input("Input team in La Liga:\n")
second_team = input("Input another team in La Liga:\n")

print(f"{first_team} is the best team in La Liga!")
print(f"{second_team} is also a good team.")

print_border(level,item, "End")

item = "Switching Teams"
'''
Task: Write a program that stores "Ferrari" in a variable and prints a message about the team. Then, change the variable's value to "Williams" and print a message about the updated team.

Expected Output:

"[First team name] is a legendary F1 team."
"Carlos Sainz will be driving for [second team name] in 2025."
'''

print_border(level,item, "Start")
#Enter your code below this line
carlos_team =  "Ferrari"
print(f"{carlos_team} is a legendary F1 team.")

carlos_team = "Williams"
print(f"Carlos Sainz will be driving for {carlos_team} in 2025.")

print_border(level,item, "End")


level = "More Comfortable"
item = "Driver Name Error"
'''
Task: Write a program that tries to print a message about Carlos Sainz but has a name error (e.g., misspelling the variable name). Then, fix the error and print the correct message.

Expected Output: (After fixing the error) "Carlos Sainz is a skilled F1 driver."
'''

print_border(level,item, "Start")
#Enter your code below this line

fave_driver = "Carlos Sainz"
# print(f"{favedriver} is a skilled F1 Driver.") # error
print(f"{fave_driver} is a skilled F1 Driver.") # corrected

print_border(level,item, "End")

item = "Team Name Error"

'''
Task: Write a program that tries to print a message about FC Barcelona but has a name error (e.g., misspelling the variable name). Then, fix the error and print the correct message.

Expected Output: (After fixing the error) "FC Barcelona won La Liga in the 2023-2024 season."
'''

print_border(level,item, "Start")
#Enter your code below this line

fave_team = "FC Barcelona"
# print(f"{fav_team}  won La Liga in the 2023-2024 season.") # error
print(f"{fave_team}  won La Liga in the 2023-2024 season.") # corrected

print_border(level,item, "End")
