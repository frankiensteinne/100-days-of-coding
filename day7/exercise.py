border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Driver Lap List"
'''
Concepts: Passing Lists to Functions
Task: Write a function display_lap_times(lap_times) that takes a list of lap times and prints each time on a new line.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
lap_times = [80.2, 78.5, 76.8]

def display_lap_times(lap_times =  lap_times):
    for lap in lap_times:
        print(lap)

display_lap_times()
linebreak()
print_border(level,item, "End")
linebreak()

item = "Top Scorer List"
'''
Concepts: Modifying Lists in Functions
Task: Write a function add_goal_scorer(scorers, scorer) that appends a new scorer to the list and prints the updated list.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
scorers = ['Lewandowski', 'Pedri']
new_scorer = 'Ferran Torres'

def add_goal_scorer(scorer, list_of_scorers = scorers):
    list_of_scorers.append(scorer)
    print(list_of_scorers)
    
add_goal_scorer(new_scorer)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Total Lap Time"
'''
Concepts: Functions with List Operations
Task: Write a function calculate_total_time(lap_times) that returns the total time from a list of lap times.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
lap_times = [80.2, 78.5, 76.8]

def calculate_total_time(lap_times):
    total_time = 0
    for lap in lap_times:
        total_time += lap
    return total_time

calculate_total_time(lap_times)
linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Lap Time Average"
'''
Concepts: Functions with List Calculations
Task: Write a function calculate_average_time(lap_times) that returns the average lap time.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
lap_times = [80.2, 78.5, 76.8]

def calculate_average_lap_time(lap_times):
    total_time = sum(lap_times)
    return total_time/len(lap_times)

calculate_average_lap_time(lap_times)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Dynamic Scorer List"
'''
Concepts: Modifying Lists in Functions
Task: Write a function update_scorers(scorers, new_scorers) that takes two lists (existing scorers and new scorers) and extends the original list.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
scorers = ['Lewandowski', 'Pedri']  
new_scorers = ['Ferran Torres', 'Ansu Fati']

def update_scorers(scorers, new_scorers):
    scorers.extend(new_scorers)
    return scorers

update_scorers(scorers,new_scorers)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Race Position Tracker"
'''
Concepts: Functions with Conditional Logic and Lists
Task: Write a function track_positions(positions) that takes a list of driver positions and prints a message for each based on their placement.
'''
positions = [1, 2, 4, 6]
messages = [
    "Winner!",
    "Podium Finish!",
    "Keep Pushing!",
    "Keep Pushing!"
]

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def track_positions(positions,messages):
    index = 0
    for position in positions:
        print(f"Position {position}: {messages[index]}")
        index += 1
        
track_positions(positions, messages)

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Dynamic Lap Time Analysis 2.0"
'''
Concepts: Functions, Lists
Task: Write a function analyze_lap_times(lap_times) that:
- Takes a list of lap times.
- Returns the fastest lap, slowest lap, and average time.
Extra Challenge: Add a feature to count laps below 80 seconds.

'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
lap_times = [80.2, 78.5, 76.8, 90.3]

linebreak()
print_border(level,item, "End")
linebreak()

item = "Dynamic Scorer Analysis"
'''
Concepts: Functions, Lists, Dictionaries
Task: Write a function scorer_analysis(scorers) that:
Takes a list of scorers.
Returns a dictionary with each player’s goal count and the total goals.
Extra Challenge: Print the top scorer and their goals.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
scorers = ['Lewandowski', 'Pedri', 'Lewandowski', 'Ansu Fati', 'Lewandowski']

linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Performance Tracker"
'''
Concepts: Functions, Lists
Task: Write a function performance_tracker(driver_name, positions) that:
-Takes a driver’s name and a list of positions from multiple races.
-Returns their average position and the number of podium finishes (positions 1–3).

Extra Challenge: Add message if they have more than 50% podium finishes,
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line

linebreak()
print_border(level,item, "End")
linebreak()