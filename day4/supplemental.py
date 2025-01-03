border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status)

    
from random import choice, randint, shuffle

level = "Base"
item = "Coin Toss"
'''
Task: Write a program that simulates a coin toss. Use the random.choice() function to randomly choose between "Heads" and "Tails." Print the result.

Expected Output: "Heads" or "Tails"
'''
print_border(level,item, "Start\n")
#Enter your code below this line
coin_toss = choice([True, False])
print(coin_toss)
print_border(level,item, "End")

item = "Penalty Shootout"
'''
Task: Write a program that simulates a penalty shootout. Randomly select a player from a list of 3 FC Barcelona players. Print the message, "[Player's name] steps up to take the penalty!".

Expected Output: "[Player's name] steps up to take the penalty!" (e.g., "Pedri steps up to take the penalty!")
'''

print_border(level,item, "Start")
#Enter your code below this line
penalty_takers = [
    "Raphina",
    "Fermin Lopez",
    "Robert Lewandowski"
]

penalty_taker = penalty_takers[randint(0,2)]

print(f"{penalty_taker} steps up to take the penalty")


print_border(level,item, "End")


level = "Comfortable"
item = "Starting Lineup"

'''
Task: Create an empty list called starting_lineup. Write a program that randomly selects 5 players from a list of 11 football players and adds them to the starting_lineup. Print the starting_lineup.

Expected Output: A list of 5 player names.
'''

print_border(level,item, "Start")
#Enter your code below this line

starting_lineup = []
eleven = [
    "Inaki Pena",
    "Kounde",
    "Pau Cubarsi",
    "Inigo Martinez",
    "Balde",
    "Marc Casado",
    "Pedri",
    "Raphina",
    "Gavi",
    "Fermin Lopez",
    "Robert Lewandowski"
]

shuffle(eleven)
starting_lineup = eleven[0:5]

print(starting_lineup)

print_border(level,item, "End")

item = "Race Finishers"
'''
Task: Create an empty list called top_3. Write a program that randomly selects 3 drivers from a list of 20 F1 drivers and adds them to the top_3 list. Print the message "The top 3 finishers are: [driver 1], [driver 2], and [driver 3]".

Expected Output: "The top 3 finishers are: [driver 1], [driver 2], and [driver 3]"
'''

print_border(level,item, "Start")
#Enter your code below this line
top_3 = []
f1_drivers = [
    "Max Verstappen",
    "Liam Lawson",
    "Charles Leclerc",
    "Lewis Hamilton",
    "Lando Norris",
    "Oscar Piastri",
    "George Russell",
    "Kimi Antonelli",
    "Fernando Alonso",
    "Lance Stroll",
    "Yuki Tsunoda",
    "Isack Hadjar",
    "Oliver Bearman",
    "Esteban Ocon",
    "Pierre Gasly",
    "Jack Doohan",
    "Alex Albon",
    "Carlos Sainz",
    "Nico Hulkenberg",
    "Gabriel Bortoleto"
]

shuffle(f1_drivers)
top_3 = f1_drivers[0:3]

print(f"The top 3 finishers are: {top_3[0]}, {top_3[1]}, and {top_3[2]}")

print_border(level,item, "End")

level = "More Comfortable"
item = "Guess the Number"

'''
Task: Write a program that generates a random number between 1 and 20. Ask the user to guess the number. If the guess is correct, print "Correct!". If the guess is too high, print "Too high!". If the guess is too low, print "Too low!".

Expected Output: "Correct!", "Too high!", or "Too low!"
'''

print_border(level,item, "Start")
#Enter your code below this line
winning_number =  randint(1,20)
# print(winning_number)
user_guess = int(input("Guess a number between 1 and 20: "))

if winning_number < user_guess:
    print("Too high!")
elif winning_number == user_guess:
    print("Congrats!")
else:
    print("Too low!")

print_border(level,item, "End")

item = "Team Selection"
'''
Task: Write a program that randomly selects 4 teams from a list of 8 football teams. Create a new list called selected_teams and add the selected teams to it. Print the selected_teams.

Expected Output: A list of 4 team names.
'''

print_border(level,item, "Start")
#Enter your code below this line
football_teams = [
    "FC Barcelona",
    "Atletico Bilbao",
    "Cadiz FC",
    "Las Palmas",
    "Deportivo Coruna",
    "Girona",
    "Espanyol",
    "Real Sociedad"
]

shuffle(football_teams)
selected_teams = football_teams[1:5]
print(selected_teams)
print_border(level,item, "End")