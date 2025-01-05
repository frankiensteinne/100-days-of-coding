'''
Exercise 1: Set Up Race Information
Difficulty: Base
Goal: Set up the track and race details.
Concepts: String manipulation, Lists and indexing, Input

Steps:
- User Input: Ask for the track name (e.g., "Monza") and number of laps (e.g., 50).
- Define a list of drivers for the race (e.g., "Charles Leclerc", "Lewis Hamilton", etc.).
- Display the track name and race details.
'''
from random import shuffle 
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

track_name = input("Enter the track name: ").title()
no_laps = int(input(f"Enter the number of laps in {track_name}: "))
starting_grid = f1_drivers[:]
shuffle(starting_grid)

print(f"Track Name: {track_name}")
print(f"Number of laps: {no_laps}")
print(f"Starting Grid:")

for idx, driver in enumerate(starting_grid, start=1):
    print(f"P{idx} - {driver}")

