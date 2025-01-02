border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
from random import randint

random_number = randint(1,3)
print(random_number)

level = "Base"
item = "Penalty Kick"

print_border(level,item, "Start")
#Enter your code below this line"
'''
Task:  Write a program that simulates a penalty kick. Ask the user to input "left," "right," or "center." If the user guesses the direction the goalkeeper dives, print "Goal!". Otherwise, print "Saved!".

Expected Output: "Goal!" or "Saved!"
'''
random_number = randint(1,3)
goalie = ""

if random_number == 1:
    goalie = "left"
elif random_number == 2:
    goalie ="right"
else:
    goalie = "center"
    
guess = input("Where will you kick: left, right, or center?: ").lower()

if guess == goalie:
    print("Saved")
else:
    print("Goal!")

print_border(level,item, "End")

item = "Race Start"
'''
Task:  Write a program that simulates the start of an F1 race. Ask the user if the lights are "red," "yellow," or "green." If the lights are "green," print "Go!". Otherwise, print "Wait!".

Expected Output: "Go!" or "Wait!"   
'''

print_border(level,item, "Start")
#Enter your code below this line
light = input("What color are the lights?: red, yellow, or green? ").lower()

if light == 'green':
    print('Go!')
else:
    print('Wait!')

print_border(level,item, "End")

level = "Comfortable"
item = "Yellow Card"
'''
Task: Write a program that asks the user for a player's name and the type of foul they committed ("minor" or "major"). If the foul is "major," print "[Player name] gets a red card!". If the foul is "minor" and the player already has a yellow card, print "[Player name] gets a second yellow card and a red card!". Otherwise, print "[Player name] gets a yellow card.". Use if-elif-else and logical operators.

Expected Output:  "[Player name] gets a [card type] card!"
'''

print_border(level,item, "Start")
#Enter your code below this line
yellow_cards = 0
player_name = input("What is the player's name?: ").title()
offense = input("What type of foul did they committed, major or minor?").lower()


if offense == 'minor':
    yellow_cards += 1
    if yellow_cards == 2:
        print(f"{player_name} gets a second yellow card and a red card!")
    else:
        print(f"{player_name} gets a yellow card.")
else:
    print(f"{player_name} gets a red card!")
        
print_border(level,item, "End")

item = "Pit Stop Strategy"
'''
Task: Write a program that asks the user for the current lap number and the tire condition ("good" or "worn"). If the lap number is greater than 10 and the tire condition is "worn," print "Pit stop!". Otherwise, print "Stay out.". Use if-elif-else and logical operators.

Expected Output: "Pit stop!" or "Stay out."
'''

print_border(level,item, "Start")
#Enter your code below this line
tire_number = int(input("What is the current lap number?: "))
tire_condition = input("What is the tire condition: good or worn?: ").lower()

if tire_number > 10 and tire_condition == 'worn':
    print("Pit Stop!")
else:
    print("Stay out.")
    

print_border(level,item, "End")


level = "More Comfortable"
item = "League Position"
'''
Task: Write a program that takes a team's points as input. If the points are greater than or equal to 70, print "The team is in first place!". If the points are between 60 and 69 (inclusive), print "The team is in second place!". If the points are between 50 and 59 (inclusive), print "The team is in third place!". Otherwise, print "The team is not in the top 3.". Use if-elif-else.

Expected Output:  A message indicating the team's league position.
'''

print_border(level,item, "Start")
#Enter your code below this line
team_points = int(input("How many points did the team scored?: "))

if team_points >= 70:
    print("The team is in first place!")
    
elif team_points < 70 and 59 < team_points:
    print("The team is in second place!")
    
elif team_points < 60 and 49 < team_points:
    print("The team is in third place!")
    
else:
    print("The team is not in the top 3.")


print_border(level,item, "End")

item = "Championship Decider"

'''
Task: Write a program that asks for the points of two drivers. Determine who is the champion based on their points. If they have the same number of points, print "It's a tie!". Use if-elif-else and comparison operators.

Expected Output: A message declaring the champion or indicating a tie.
'''

print_border(level,item, "Start")
#Enter your code below this line

driver_one_pts = int(input("How many points did driver one earned? "))
driver_two_pts = int(input("How many points did driver two earned? "))

if driver_one_pts < driver_two_pts:
    print("Driver two wins!")
elif driver_two_pts < driver_one_pts:
    print("Driver one wins!")
else:
    print("It's a tie!")



print_border(level,item, "End")