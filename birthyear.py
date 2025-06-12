"""
Project
Goals:
conditional statements
user input - you may need to do int(input("prompt goes here")) if you're expecting numbers
one loop (for loop, while loop)
history
pretend we're comparing birth years
take birth years from two people
program will tell us who is older
#"""

print("Person A will tell us their birth year first")

print("Person B will tell us their birth year second")

print("I, the computer program, will tell you who is older! Hold your applause, please")

#username = input("Enter username:")

yearB = int(input("Birth year for person B: "))



if yearA > yearB:
    print("Person A is younger than person B")

elif yearB > yearA:
    print("Person A is older than person B")

else:
    print("They are both the same age")


