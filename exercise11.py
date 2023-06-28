print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print("Here is another way of doin it")
# This is a modification of the first expression
print(f"So you are {age} years old, {height}m tall, and {weight}kg heavy")
fname = input("Enter your first name? ")
lname = input("Enter your last name: ")
time = input("Enter your year of birth: ")
qualification = input("What is your highest qualification? ")
gender = input("Are you a male or a female? (male/female): ")
marital = input("Are you single or married? (single/married) ")
print(
    f"Your name is {fname} {lname}, and you were born in {time}. \nYour highest qualification is {qualification}. You are {gender} and you are {marital}"
)
