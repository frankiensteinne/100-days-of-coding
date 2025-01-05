border = "*" * 10

def print_border(level,item,status):
    print(border,level,item,status, border)
    
def linebreak():
    print("\n")

level = "Base"
item = "Hello, Python World (Football Edition)"
'''
Concepts: Printing, Strings
Task: Write a program that prints:

`Welcome to Python Programming!
Visca Barça!`
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
print("Welcome to Python Programming!\nVisca Barça!")

linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Introduction"
'''
Concepts: Variables
Task: Create a variable driver_name and assign it a value of your favorite F1 driver’s name. Print a message like:

`My favorite driver is Carlos Sainz!`

'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_name = "Carlos Sainz"
print(f"My favorite driver is {driver_name}")
linebreak()
print_border(level,item, "End")
linebreak()

item = "String Combination Practice"
'''
Concepts: String concatenation
Task: Combine variables team and motto into a single sentence.

Output: 
```
Team: FC Barcelona  
Motto: Més que un club  
Output: FC Barcelona's motto is "Més que un club."
```
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
football_team = "FC Barcelona"
motto = "Més que un club"

print(f'{football_team}\'s motto is "{motto}".')

linebreak()
print_border(level,item, "End")
linebreak()

level = "Comfortable"

item = "Dynamic Greetings"
'''
Concepts: Input, Variables, String Manipulation
Task: Ask for the user’s name and team, then print a message
Output: ```Hi [Name]! Welcome to the world of [Team].```
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
name_inp = input("What is your name?: ")
team_inp = input("Which team do you support?: ")

print(f"Hi {name_inp}! Welcome to the world of {team_inp}.")
linebreak()
print_border(level,item, "End")
linebreak()

item = "F1 Race Results"
'''
Concepts: Variables, f-strings
Task: Use variables position, driver, and team
Output: ```Carlos Sainz finished 2nd for Williams Racing.```
'''


print_border(level,item, "Start")
linebreak()
#Enter your code below this line
position = "3rd"
driver = "Lewis Hamilton"
team = "Ferrari"

print(f"{driver} finished {position} for {team}")
linebreak()
print_border(level,item, "End")
linebreak()

item = "Line Formatting Practice"
'''
Concepts: Special characters (newline, tabs)
Task: Print a race leaderboard
Output: 
```
1. Max Verstappen  
   2. Carlos Sainz  
   3. Charles Leclerc  
```
'''
print_border(level,item, "Start")
linebreak()
#Enter your code below this line
print("1. Max Verstappen\n\t2. Carlos Sainz\n\t3. Charles Leclerc")
linebreak()
print_border(level,item, "End")
linebreak()

level = "More Comfortable"

item = "FC Barcelona Chant Generator"
'''
Concepts: String Repetition
Task: Create a program that prints chant
Output: ```Barça! Barça! Barça!```
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
team = "Barça"
repeat = 3
chant = " ".join([team + "!" for _ in range(repeat)])


linebreak()
print_border(level,item, "End")
linebreak()

item = "Driver Fact File"
'''
Concepts: Variables, Multi-line Strings
Task: Use variables to create a bio for Carlos Sainz
'''



print_border(level,item, "Start")
linebreak()
#Enter your code below this line
driver_name= "Carlos Sainz"  
driver_team = "Williams Racing"
driver_wins= 2  
driver_fun_fact = 'Known as "Smooth Operator."'

linebreak()
print_border(level,item, "End")
linebreak()

item = "Custom Message Formatter"
'''
Concepts: Advanced String Manipulation
Task: Ask for user input (name, team, favorite driver)
Challenge: Capitalize inputs automatically.
Output: Hello [Name]! You’re a fan of [Team], and your favorite driver is [Driver].
'''

print_border(level,item, "Start")
linebreak()
#Enter your code below this line
inp_name = input("What is your name? :").title()
inp_team = input("Which team do you support?: ").title()
inp_driver = input("Who is your favorite driver?: ").title()

print(f"Hello {inp_name}! You’re a fan of {inp_team}, and your favorite driver is {inp_driver}.")
linebreak()
print_border(level,item, "End")
linebreak()