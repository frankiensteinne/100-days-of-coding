border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Countdown"
'''
Task: Write a program that uses a for loop to print a countdown from 10 to 1, then prints "Liftoff!".

Expected Output:

10
9
8
...
2
1
Liftoff!
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
for number in reversed(range(0,11)):
    if number != 0:
        print(number)
    else:
        print("Liftoff!")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Team Chant Loop"
'''
Task: Write a program that takes a team name as input and uses a for loop to print the team chant 3 times.

Expected Output:

[Team Name]!
[Team Name]!
[Team Name]!
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_name = input("Input team name for chant: ").title()

for _ in range(3):
    print(f"{team_name}!") 

linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Lap Counter with a Twist"
'''
Task: Write a program that simulates laps in an F1 race. Use a while loop to print "Lap [number]" for 20 laps. On laps 5, 10, and 15, print "Pit stop!".

Expected Output: "Lap [number]" for 20 laps, with "Pit stop!" on laps 5, 10, and 15.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

laps = 0
while laps < 20:
    laps += 1
    if laps%5 == 0:
        print(f"Lap {laps} - Pit Stop!")
    else:
        print(f"Lap {laps}")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Goal Scorers with Details"
'''
Task: Create a list of 4 football players. Use a for loop and an if-else statement to print details about each player. If the player is named "Pedri", print "[Player's name] scored a goal! He's a rising star!". For other players, print "[Player's name] scored a goal!". (pp. 38-40)

Expected Output:

"[Player's name] scored a goal!" for most players.
"Pedri scored a goal! He's a rising star!" if the player is "Pedri"."
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
footballers = [
    "Marc Casado",
    "Pedri",
    "Raphina",
    "Gavi",
    "Fermin Lopez",
    "Robert Lewandowski"
    ]
for player in footballers:
    if player != 'Pedri':
        print(f"{player} scored a goal!")
    else:
        print(f"{player} scored a goal! He's a rising star!")

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Interactive Chant"
'''
Task: Write a program that takes a team name as input and uses a while loop to repeatedly ask the user if they want to "chant" or "quit." If they choose "chant," print the team chant. If they choose "quit," exit the loop.

Expected Output: The program repeatedly asks the user to "chant" or "quit" and responds accordingly.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
while True:
    mode = input("Chant or Quit? ").title()
    if mode == 'Quit':
        break
    elif mode == 'Chant':
        print("Vamos Barca, vamos!")
    else:
        print("Please enter a valid response (Chant/ Quit). ")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Position Tracker"
'''
Task: Create a list of 5 F1 drivers. Use a while loop and input() to ask the user to enter the current lap number and the position changes for each driver. Update the driver positions accordingly and print the current standings after each lap.

Expected Output: The program asks for lap number and position changes, then prints the updated driver standings after each lap.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
from random import shuffle

five_drivers = [
    "Charles Leclerc",
    "Lewis Hamilton",
    "Alex Albon",
    "Carlos Sainz",
    "Oliver Bearman"
]

while True:
    try:
        lap_number = int(input("Input current lap number (1-30): "))
        
        if lap_number < 1 or lap_number > 30:
            print("Please input a value between 1 and 30.")
            continue

        shuffle(five_drivers)

        if lap_number < 30:
            print(f"Lap {lap_number}:")
            for idx, driver in enumerate(five_drivers, start=1):
                print(f"{idx}. {driver}")
        else:  # Lap 30
            print(f"Lap {lap_number} - Final Standings:")
            for idx, driver in enumerate(five_drivers, start=1):
                print(f"{idx}. {driver}")
            print("Race complete!")
            break

    except ValueError:
        print("Please enter a valid number.")

    
linebreak()
print_border(level,item, "End")
linebreak()