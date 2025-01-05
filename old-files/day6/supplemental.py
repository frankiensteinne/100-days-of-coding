border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Calculate Points with Bonus"
'''
Task: Define a function called calculate_points() that takes the number of wins, draws, and losses as arguments. Calculate the total points (3 points for a win, 1 for a draw, 0 for a loss). If the total points are above 10, add a bonus of 2 points. Return the result. Call the function with some sample data.

Expected Output: The total number of points, potentially with a bonus.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def calculate_points(wins,draws,losses):
    points = (wins*3) + (draws*1) + (losses*0)
    
    if points > 10:
        points += 2
        
    print(points)

calculate_points(1,2,5)
calculate_points(3,2,3)

linebreak()
print_border(level,item, "End")
linebreak()

item = "Format Driver Name with Nationality"
'''
Task: Define a function called format_driver_name() that takes a driver's first name, last name, and nationality as arguments. Return a formatted string like "[Last Name], [First Initial.] ([Nationality])".  (e.g., "Sainz, C. (Spanish)"). Call the function with a driver's information.

Expected Output: The formatted driver name with nationality.

'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def format_driver_name(fname, lname, nationality):
    fname = fname[0].upper()
    lname = lname.title()
    nationality = nationality.title()
    
    return f"{lname}, {fname}. ({nationality})"

print(format_driver_name("Carlos", "Sainz JR.", "spanish"))
print(format_driver_name("alex", "albon", "thai"))

linebreak()
print_border(level,item, "End")
linebreak()


level = "Comfortable"

item = "Goal Difference with Message"
'''
Task: Define a function called goal_difference() that takes two arguments: goals scored and goals conceded. Calculate the goal difference. If the goal difference is positive, return a string like "The team won by [goal difference] goals!". If it's negative, return "The team lost by [goal difference] goals!". If it's zero, return "It's a draw!". Call the function with different values.

Expected Output: A message indicating the goal difference and result.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def goal_difference(scored, conceded):
    message = ""
    difference = scored-conceded
    if difference > 0:
        message = f"The team won by {difference} goals!"
        return message
    elif difference == 0:
        message = f"It's a draw!"
        return message
    elif difference < 0:
        message = f"Oh, no! The team lost by {difference} goals."
        return message
    
    
print(goal_difference(5,2))
print(goal_difference(3,3))
print(goal_difference(0,2))
    
linebreak()
print_border(level,item, "End")
linebreak()

item = "Lap Time Analysis"
'''
Task: Define a function called lap_time_analysis() that takes two lap times in seconds as arguments. Return a string indicating which lap time was faster (e.g., "Lap 1 was faster."). If the lap times are the same, return "Both laps have the same time.". Call the function with different lap times.

Expected Output: A message comparing the two lap times.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def lap_time_analysis(lap_time_one,lap_time_two):
    difference = round(abs(lap_time_one-lap_time_two),3)
    if lap_time_one > lap_time_two:
        return f"Lap 2 was faster by {difference} seconds"
    elif lap_time_two > lap_time_one:
        return f"Lap 1 was faster by {difference} seconds"
    else:
        return f"Both laps have the same time."
    
print(lap_time_analysis(74.352,74.570))
print(lap_time_analysis(75.352,74.570))
print(lap_time_analysis(73.001,73.001))

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = " Points Per Game with Ranking"
'''
Task: Define a function called points_per_game() that takes the number of games played and the total points as arguments. Calculate the points per game. If the points per game are above 2, return "Excellent performance!". If between 1 and 2 (inclusive), return "Good performance.". Otherwise, return "Needs improvement.". Call the function with different values.

Expected Output: A message evaluating the performance based on points per game.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def points_per_game(games,points):
    average = points/games
    
    if average > 2:
        return f"Excellent Performance"
    elif 1 <= average <= 2:
        return f"Good Performance"
    else:
        return f"Needs Improvement"

print(points_per_game(10,30))
print(points_per_game(18,30))
print(points_per_game(19,12))

linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Position Change with Overtakes"
'''
Task: Define a function called driver_position_change() that takes a driver's starting position and finishing position as arguments. Calculate the change in position. If the change is positive, return a string like "The driver gained [number] positions!". If negative, return "The driver lost [number] positions!". If zero, return "The driver maintained their position.". Call the function with different positions.

Expected Output: A message describing the driver's position change.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
def driver_position_change(starting, final):
    change = starting - final
    if 0 < change:
        return f"The driver gained {change} positions!"
    elif change == 0:
        return "The driver maintained their position."
    else:
        return f"The driver lost {abs(change)} positions!"
    
print(driver_position_change(19,3))
print(driver_position_change(1,5))
print(driver_position_change(3,3))
    
linebreak()
print_border(level,item, "End")
linebreak()