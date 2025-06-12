name = input("Enter your name: ")

if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")


name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")


age = int(name = input("Enter your age: "))

while age < 0:
    print("Age cant be negative")
    age = int('imput'("Enter your age: "))

print(f"You are {age} years old")


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")


