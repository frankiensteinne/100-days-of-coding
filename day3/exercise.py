border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "F1 Driver Lineup"
'''
Concepts: List Creation and Accessing Elements
Task: Create a list of five F1 drivers. Print the second and last driver from the list.
Expected Output:

Second driver: Charles Leclerc  
Last driver: Carlos Sainz  
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
five_f1_drivers = [
    "Alex Albon",
    "Charles Leclerc",
    "Lewis Hamilton",
    "Yuki Tsunoda",
    "Carlos Sainz"
]

print(f"Second driver: {five_f1_drivers[1]}")
print(f"Last driver: {five_f1_drivers[-1]}")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Goal Scorers"
'''
Concepts: Modifying and Adding to Lists
Task: Create a list of top 3 goal scorers for FC Barcelona. Add a fourth player to the list and replace the second player with a new name. Print the updated list.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
fcb_goalscorers = [
    "Robert Leewandowski",
    "Ferran Torres",
    "Lamine Yamal"
]

fcb_goalscorers.append("Fermin Lopez")
fcb_goalscorers[1] = "Raphinha"

print(fcb_goalscorers)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Upcoming Fixtures"
'''
Concepts: Appending Items to a List
Task: Create an empty list fixtures. Append three upcoming matches to it (e.g., "vs Real Madrid"). Print the list.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
fixtures = []
fixtures.append("vs Real Sociedad")
fixtures.append("vs Sevilla")
fixtures.append("vs Las Palmas")

print(fixtures)
linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Sorted Driver Lineup"
'''
Concepts: Sorting Lists
Task: Sort the F1 driver lineup alphabetically. Print the original and sorted list.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
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

sorted_drivers = sorted(f1_drivers)

print(f1_drivers)
print(sorted_drivers)


linebreak()
print_border(level,item, "End")
linebreak()

item = "Top Scorers’ Rankings"
'''
Concepts: Removing and Inserting Elements
Task: Create a list of top 5 scorers. Remove the player ranked third, insert a new player at the same position, and print the updated rankings.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
top_scorers = [
    "Ronaldo",
    "Messi",
    "Bican",
    "Romario",
    "Pele"
]

top_scorers.pop(2)
top_scorers.insert(2, "Lewandowski")

print(top_scorers)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Favorite Teams"
'''
Concepts: List Iteration
Task: Create a list of 3 favorite teams. Print a message for each
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
fave_teams = [
    "FC Barcelona",
    "Scuderria Ferrari",
    "Williams Racing"
]

print(fave_teams[0])
print(fave_teams[1])
print(fave_teams[2])
linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Dynamic Fixture Manager"
'''
Concepts: Input and List Operations
Task: Allow the user to input three upcoming fixtures and store them in a list. Print the list.
Challenge: Ask the user if they want to update any fixture and modify it accordingly.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
new_fixtures = []

new_fixtures.append(input("Enter Fixture 1: "))
new_fixtures.append(input("Enter Fixture 2: "))
new_fixtures.append(input("Enter Fixture 3: "))

print(new_fixtures)
ans = input("Do you want to update fixtures? (yes/no): ").lower()
if ans == 'no':
    print("Bye")
else:
    fixture_number = int(input("Which fixture (1, 2, or 3)?: "))
    new_fixture = input("Enter new fixture: ")
    index = fixture_number -1
    new_fixtures[index] = new_fixture
    print(f"Updated Fixtures: {new_fixtures}")
linebreak()
print_border(level,item, "End")
linebreak()

item = "Top Drivers Manager"
'''
Concepts: List Operations, Input
Task: Prompt the user for a list of their top 5 drivers. Allow them to remove one driver and replace them with another. Print the updated list.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
top_drivers = []

top_drivers.append(input("Enter Driver 1: ").title())
top_drivers.append(input("Enter Driver 2: ").title())
top_drivers.append(input("Enter Driver 3: ").title())
top_drivers.append(input("Enter Driver 4: ").title())
top_drivers.append(input("Enter Driver 5: ").title())

print(top_drivers)

removed_driver = input("Remove one driver: ").title()
new_driver = input("Replace with: ").title()
top_drivers = [x.replace(removed_driver, new_driver) for x in top_drivers]

print(top_drivers)
linebreak()
print_border(level,item, "End")
linebreak()

item = "Barça Starting XI"
'''
Concepts: Complex List Operations
Task: Create a list of Barça’s starting XI players. Allow the user to:
- Add a substitute player.
- Replace one player in the starting XI.
- Print the updated lineup.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
starting_eleven = [
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
print(starting_eleven)
sub_player = input("Input your sub player: ").title()
subbed_off = input("Input who will be subbed off?: ").title()

fielded_players = [x.replace(subbed_off, sub_player) for x in starting_eleven]

print(fielded_players)
linebreak()
print_border(level,item, "End")
linebreak()