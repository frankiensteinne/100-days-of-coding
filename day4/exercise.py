border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Driver Qualifier"
'''
Concepts: if Statements, Comparison Operators
Task: Write a program that checks if a driver’s lap time is under 80 seconds.
Expected Output:
Lap time: 78.2  
Output: Qualifies for the next round!  

'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_time = float(input("What is the driver's time in seconds?: "))

if driver_time < 80:
    print("Driver qualifies for the next round!")
else:
    print("Better luck next time.")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Fan Eligibility"
'''
Concepts: if-else Statements
Task: Ask the user for their age and check if they are eligible for discounted Barça tickets (under 18 or over 60).
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
age = int(input("How old are you?: "))
if age < 18 or age > 60:
    print("You are eligible for a discount.")
else:
    print("You pay full price")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Team Comparison"
'''
Concepts: Comparison Operators
Task: Compare two teams' points and print which one is leading. 
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team_one = input("Enter team one: ").upper()
team_one_pts = input(f"Enter {team_one}'s total points: ")
team_two = input("Enter team two: ").upper()
team_two_pts = input(f"Enter {team_two}'s total points: ")
message = ""

if team_one_pts == team_two_pts:
    message = "It's a tie."
elif team_one_pts > team_two_pts:
    message = f"{team_one} wins."
else:
    message = f"{team_two} wins."
    
print(f"{team_one} made {team_one_pts} points.\n{team_two} made {team_two_pts} points.\n{message}")
linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Race Winner Predictor"
'''
Concepts: Logical Operators (and, or)
Task: Write a program that predicts the race winner based on conditions like driver performance and car reliability.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
car_reliability = ["bad","mid","excellent"]
performance = ["weak", "regular", "strong"]
probability = [
    "unlikely to finish in the top 15.",
    "likely to finish in the top 10.",
    "likely to finish in the top 5.",
    "likely to finish on the podium.",
    "likely to win the race."
    ]

driver_name = "Carlos Sainz"
driver_car_reliability = car_reliability[2]
driver_performance = performance[2]

driver_car_reliability_points = car_reliability.index(driver_car_reliability)
driver_performance_points = performance.index(driver_performance)

driver_points = driver_performance_points + driver_car_reliability_points

print(f"{driver_name.title()} has a very {driver_car_reliability} car and had a {driver_performance} performance in the qualifying.\nHe is {probability[driver_points]}")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Barça Goal Tracker"
'''
Concepts: Nested if Statements
Task: Check if Barça scores 3 or more goals in a match. If yes, check if Lewandowski scored at least 2.
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
barca_goals = ["Lewandowski","Raphinha", "Ferran Torres", "Lewandowski", "Lewandowski"]
no_of_barca_goals = len(barca_goals)
lewy_goals = barca_goals.count("Lewandowski")

if no_of_barca_goals >= 3:
    if lewy_goals >= 2:
        print("Lewan-GOAL-ski for the win")
    print("Força Barça!")
else:
    print("Game well played.")
        
linebreak()
print_border(level,item, "End")
linebreak()

item = "Pit Stop Validator"
'''
Concepts: if-elif-else Statements
Task: Validate pit stop times. If below 2.5 seconds, print “Perfect Stop”; if between 2.5–3.5 seconds, print “Good Stop”; otherwise, print “Needs Improvement.”
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
pit_stop = 2.52

if pit_stop < 2.5:
    print("Perfect Stop.")
elif 2.5 <= pit_stop <= 3.5:
    print("Good Stop.")
else:
    print("Needs Improvement.")

linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "Team Loyalty Checker"
'''
Concepts: Logical and Comparison Operators
Task: Ask the user which team they support and whether they watch matches regularly. Print a message based on their loyalty.
Extra Challenge: Add a loyalty score system where regular viewers get a higher score.
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
base_loyalty_pts = 100
user_pts_adjustment = []

user_watch = input("Do you watch games regularly? (y/n): ").lower()
user_member = input("Are you a member of the fan club? (y/n): ").lower()
user_buy = input("Do you buy from the official store?: (y/n): ").lower()

user_pts_adjustment.append(user_watch)
user_pts_adjustment.append(user_member)
user_pts_adjustment.append(user_buy)

yes_count = user_pts_adjustment.count('y')
no_count = user_pts_adjustment.count('n')

user_loyalty_pts = ((yes_count*10) - (no_count*10)) + base_loyalty_pts

if 90 <= user_loyalty_pts <= 110:
    print(f"You have {user_loyalty_pts} Loyalty Points. You are a Fan!")

elif user_loyalty_pts > 110:
    print(f"You have {user_loyalty_pts} Loyalty Points. You are a Super Loyal Fan!")
    
else:
    print(f"You have {user_loyalty_pts} Loyalty Points. You are not a fan.")


linebreak()
print_border(level,item, "End")
linebreak()

item = "Dynamic Championship Standings"
'''
Concepts: Nested Conditionals
Task: Write a program that checks a driver’s points and determines their championship standing (e.g., Leader, Contender, Midfield).
Extra Challenge: Incorporate penalties or bonus points dynamically (e.g., add/subtract points based on conditions like infractions or wins).
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line


linebreak()
print_border(level,item, "End")
linebreak()

item = "FC Barcelona Score Validator"
'''
Concepts: Logical Operators, Nested Conditionals
Task: Ask for the match score and validate if it’s a win, draw, or loss. Also, check if Barça scored 3 or more goals.
Extra Challenge: Add support for a league points system
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
barca_goal_tally = int(input("How many goals did Barcelona scored in the game?: "))
opp_goal_tally = int(input("How many goals did the opponent scored in the game?: "))

if barca_goal_tally >= 3:
    print("Barcelona had a goal fest.")
if barca_goal_tally > opp_goal_tally:
    print("Barcelona wins and takes home the 3 points.")
elif barca_goal_tally == opp_goal_tally:
    print("It's a tie! Both teams finish the match day with one point.")
else:
    print("Barcelona losses and takes home zero points.")

linebreak()
print_border(level,item, "End")
linebreak()