#notes on while loops
# while loop = loop some code while some condition remains true
# name = input("Enter your name?")
# while name== "":
#     print("You did not enter your name")
# print(f"Hello {name}")

# age = int(input("Enter your age"))

# while age<0:
#     print("Age cannot be negative")
#     age = int(input("What is your age???"))

# print(f"You are {age} years old")
# # #  Given:
# colors = ["red", "blue", "green", "yellow", "purple"]

# food = input("What is your favorite food? q to quit")
# foodlist= []
# while not food =="q":
#     print(f"You like {food}")
#     foodlist.append(food)
#     food = input("what is your favorite food?")

# print(foodlist)
# print("Bye")

# num = int(input("Enter a number"))
# while num<1 or num>10:
#     print(f"{num}is not valid")
#     num = int(input("Enter a different number "))

# print(f"your number is {num}")

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

colors = ["red, , blue, orange, yellow, purple"]

i= 0

while i <len(colors):
    if colors[i] == "yellow":
        break
    print(colors{i})
    i+=1