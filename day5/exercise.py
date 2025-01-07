border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Driver List Printer"
'''
Concepts: `for` Loops, List Iteration
Task: Print each driver’s name from a list of 5 drivers.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
five_drivers = [
    "Carlos Sainz",
    "Charles Leclerc",
    "Lewis Hamilton",
    "Alex Albon",
    "Yuki Tsunoda"
]

for driver in five_drivers:
    print(driver)
    
linebreak()
print_border(level,item, "End")
linebreak()

item = "Barça Goal Count"
'''
Concepts: for Loops, Conditional Statements
Task: Count the number of goals scored by Lewandowski from a list of Barça goalscorers.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
barca_goal_count = ['Lewandowski', 'Pedri', 'Lewandowski', 'Ferran Torres', 'Lewandowski']
lewy_goals = 0

for scorers in barca_goal_count:
    if scorers == 'Lewandowski':
        lewy_goals += 1
print(f"Lewandowski scored {lewy_goals} goals.")
linebreak()
print_border(level,item, "End")
linebreak()

item = "Count to Ten"
'''
Concepts: while Loops
Task: Write a while loop that prints numbers from 1 to 10.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
count = 0
while count < 10:
    count += 1
    print(count)
linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Lap Time Filter"
'''
Concepts: for Loops, Conditional Logic
Task: Given a list of lap times, print only the times below 1 minute and 20 seconds.
'''        
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
lap_times = [80.2, 78.5, 90.3, 85.0, 76.8]
base = 80

for laps in lap_times:
    if laps < base:
        print(laps)
        
linebreak()
print_border(level,item, "End")
linebreak()

item = "Goal Streak Calculator"
'''
Concepts: while Loops, Break Statement
Task: Ask the user to input Barça scorers one by one. Stop when the user types “stop.” Print the number of goals entered.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
scorers = []
while True:
    inp_player = input("Enter Scorer\nor type stop to quit\n").lower()
    
    if inp_player == 'stop':
        print(f"Team scored {len(scorers)} goals.")
        break
    else:
        scorers.append(inp_player)
        print(scorers)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Leaderboard"
'''
Concepts: for Loops, Enumerate
Task: Print a leaderboard from a list of drivers using their position and name.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line

podium = [
    "Charles Leclerc",
    "Lewis Hamilton",
    "Carlos Sainz"
]
for idx, driver in enumerate(podium, start=1):
    print(f"{idx}. {driver}")

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Dynamic Lap Time Analysis"
'''
Concepts: while Loops, Input Validation
Task: Allow the user to input lap times one by one. Stop when the user types “done.” Print the fastest and slowest lap times.
Extra Challenge: Handle invalid inputs (e.g., non-numeric values).
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
slowest_lap = float('-inf')  # Initialize with negative infinity
fastest_lap = float('inf')  # Initialize with infinity
inp_laps_time = []

while True:
    inp_lap_time = input("Enter Lap Time in seconds.\nEnter `done` to quit.\n")
    
    if inp_lap_time == 'done':
        print(f"Slowest lap: {slowest_lap} secs")
        print(f"Fastest lap: {fastest_lap} secs")
        break

    try:
        inp_lap_time = float(inp_lap_time)  # Convert input to float
        if inp_lap_time < 0:
            print("ERROR! Please input valid lap time in seconds.")
        else:
            inp_laps_time.append(inp_lap_time)
            if inp_lap_time > slowest_lap:
                slowest_lap = inp_lap_time
            if inp_lap_time < fastest_lap:
                fastest_lap = inp_lap_time
            print(inp_laps_time)

    except ValueError:
        print("ERROR! Please input a valid number.")
    
linebreak()
print_border(level,item, "End")
linebreak()

item = "Lap Count Tracker"
'''
Concepts: for Loops, Conditional Logic
Task: Simulate a 10-lap race. Print a message for each lap where the driver sets a time under 80 seconds.
Extra Challenge: Count how many laps meet the condition.

'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
lap_no = 0
ten_lap_times = []
laps_under_eighty = []

while len(ten_lap_times) < 10:
    lap_no += 1
    ten_lap_time = float(input(f"Input lap {lap_no} time in secs: " ))
    ten_lap_times.append(ten_lap_time)
    if ten_lap_time < 80:
        laps_under_eighty.append(ten_lap_time)
        print(f"Lap {lap_no}: Fast lap at {ten_lap_time} seconds")

print(f"Total Fast Laps: {len(laps_under_eighty)}")
    
linebreak()
print_border(level,item, "End")
linebreak()

item = "Flexible Match Simulation"
'''
Concepts: for Loops, Nested Loops
Task: Simulate match scores for 3 matches using two nested loops. Randomly generate scores for Barça and the opponent.
Extra Challenge: Print whether Barça won, lost, or drew each match.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
from random import randint
match_number = 0
message = ""

while match_number < 3:
    match_number += 1
    barca_goals = randint(0,5)
    opp_goals = randint(0,5)
    if barca_goals > opp_goals:
        message ="WIN"
    elif opp_goals > barca_goals:
        message = "LOSS"
    else:
        message = "DRAW"
    
    print(f"Match {match_number}: Barça {barca_goals} - {opp_goals} Opponent  | {message}")
linebreak()
print_border(level,item, "End")
linebreak()