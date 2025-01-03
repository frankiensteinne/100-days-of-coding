#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

names = ["Mika","Claudia","Dau"]

print(names[0])
print(names[1])
print(names[2])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
greeting = "Hello,"
for name in names:
    print(greeting, name)

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

sentence = "I would like to have my own"
cars = ["Ferrari LaFerrari", "Bentley Continental", "Rolls-Royce Phantom", "Toyota Land Cruiser Prado", "Nissan GT-R"]

for car in cars:
    print(sentence, car)

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

dinner_guests = [
    "Reese Witherspoon",
    "Anne Hathaway",
    "Michelle Obama",
    "Mayim Bialik",
    "Hidilyn Diaz"
]

for guests in dinner_guests:
    print(f"Please join us for dinner, {guests.title()}.")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. 
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it. 
print(dinner_guests[-1])
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting. 
dinner_guests[-1] = "Simone Biles"
# • Print a second set of invitation messages, one for each person who is still in your list.
for guests in dinner_guests:
    print(f"You are invited to the dinner, {guests.title()}.")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. 
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table. 
print("We got a larger table!")
# • Use insert() to add one new guest to the beginning of your list. 
dinner_guests.insert(0,"Selena Gomez")
# • Use insert() to add one new guest to the middle of your list.
dinner_guests.insert(3, "Ellie Goulding")
# • Use append() to add one new guest to the end of your list.
dinner_guests.append("Aitana Bonmati")
# • Print a new set of invitation messages, one for each person in your list.
for guests in dinner_guests:
    print(f"You have a plate in our dinner, {guests.title()}.")

 
# #3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print("Oh shoot, we only have two spots left.")
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner. 
not_invited = []
not_invited.append(dinner_guests.pop())
not_invited.append(dinner_guests.pop())
not_invited.append(dinner_guests.pop())
not_invited.append(dinner_guests.pop())
not_invited.append(dinner_guests.pop())
not_invited.append(dinner_guests.pop())

for guest in not_invited:
    print(f"Maybe dinner next time, {guest}")
# • Print a message to each of the two people still on your list, letting them know they’re still invited. 
for guest in dinner_guests:
    print(f"Dinner is still on, {guest}")
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)