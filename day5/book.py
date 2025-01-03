# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = [
    "Four Cheese",
    "Pepperoni",
    "Creamy Spinach Dip",
    "High Protein",
    "Chicago Deep Dish",
]
# •Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# •Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
print("I really love pizza!")


#4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
animals = [
    "dog","seal","penguin", "otter", "capybara"
]
for animal in animals:
    print(animal)
# •Modify your program to print a statement about each animal, such as A dog would make a great pet.
for animal in animals:
    print(f"The {animal} is such a cinnamon roll.")
# •Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
print("Any of these animals are cinnamon rolls and are cute!")


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for number in range(1,21):
    print(number)


# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
for number in range(1,1000001):
    print(number)


# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
numbers = []
for number in range(1,1000001):
    numbers.append(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))
    
# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
for number in range(1,21,2):
    print(number)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
multiples_of_three = [number for number in range(3, 31, 3)]
print(multiples_of_three)


print(multiples_of_three)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
for number in range(1,11):
    print(number**3)


#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes = [number**3 for number in range(1,11)]


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# •Print the message "The first three items in the list are:." Then use a slice to print the first three items from that program’s list.
print("The first three animals in the list are:")
for animal in animals[:3]:
    print(animal)
# •Print the message "Three items from the middle of the list are: ." Then use a slice to print three items from the middle of the list.
print("The three animals in the middle of the list are:")
for animal in animals[1:4]:
    print(animal)
# •Print the message "The last three items in the list are:." Then use a slice to print the last three items in the list.
print("The last three animals in the list are:")
for animal in animals[-3:]:
    print(animal)

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
friend_pizzas =  pizzas[:]

# •Add a new pizza to the original list.
pizzas.append("Truffle")
# •Add a different pizza to the list friend_pizzas.
friend_pizzas.append("Funghi")
# •Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are:")
number = 0
for pizza in pizzas:
    number += 1
    print(f"{number}. {pizza}")
    
print("My  friend's favorite pizzas are:")
number = 0
for pizza in friend_pizzas:
    number += 1
    print(f"{number}. {pizza}")


# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

pizza_topping = []

while True:
    mode = input("Add pizza topping? Y/N: ").upper()
    if mode == 'N':
        break
    elif mode == 'Y':
        topping = input("Input topping: ")
        pizza_topping.append(topping)
        print(f"Added {topping.title()} to your pizza!")
    else:
        print("Please enter a valid response (Y/N).")

print("Your toppings are:")
for topping in pizza_topping:
    print(topping.title())


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
mode = input("Would you like to buy a ticket? Y/N : ").upper()
ticket_prices = [0,10,15]
while mode == 'Y':
    age = int(input("How old are you?: "))
    if age < 3:
        print(f"You pay ${ticket_prices[0]}.")
    elif 3 <= age <= 12:
         print(f"You pay ${ticket_prices[1]}.")
    else:
         print(f"You pay ${ticket_prices[2]}.")
         
    mode = input("Would you like to buy another ticket? Y/N : ").upper()
    
    if mode == 'N':
        print("Thanks!")


# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
# •Use a conditional test in the while statement to stop the loop.
mode = input("Add pizza topping? Y/N: ").upper()

# Validate the initial input
while mode not in ['Y', 'N']:
    print("Please enter a valid response (Y/N).")
    mode = input("Add pizza topping? Y/N: ").upper()

pizza_topping = []

# Loop to collect toppings
while mode == 'Y':
    topping = input("Input topping: ")
    pizza_topping.append(topping)
    mode = input("Add another topping? Y/N: ").upper()

# Display the toppings when done
if mode == 'N':
    print("Your toppings are:")
    for topping in pizza_topping:
        print(topping.title())

# •Use an active variable to control how long the loop runs.
active = True
pizza_topping = []

while active:
    topping = input("Input topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        active = False
    else:
        pizza_topping.append(topping)
        print(f"Added {topping.title()} to your pizza!")

print("Your toppings are:")
for topping in pizza_topping:
    print(topping.title())


# •Use a break statement to exit the loop when the user enters a 'quit' value.
pizza_topping = []

while True:
    topping = input("Input topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    pizza_topping.append(topping)
    print(f"Added {topping.title()} to your pizza!")

print("Your toppings are:")
for topping in pizza_topping:
    print(topping.title())


# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.)

x = 0
while x < 1:
    print("Hi")
