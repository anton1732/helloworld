#f is the connection to the answers text file
with open("historyAnswers.txt") as f:
    #x is the entire question and answer,the entire row
    for x in f:
        #i is each character in each row
        for i in x:
            #print(i)
            if i == ";":
                break
            else:
                print(i,end="")


"""
realDate = 1945
guess = ""

while guess != realDate:
    guess = int(input("what year did WW2 end? >"))
    if guess < realDate:
        print("this guess is too old, the end of WWII happened more recently than that!")
    if guess > realDate:
        print("this guess is too recent, the end of WWII happened longer ago than that!")
    if guess == realDate:
        print("This guess is correct!")
"""

"""

# REMEMBER, YOU WILL HAVE TO USE int(input....)
# don't forget the int(...)

# after checking to see which birth year makes the older person older, print:
#"Person A is older! You're welcome"
#"Person B is older! You're welcome"
firstGuess = 1500
secondGuess= 2000
thirdGuess = 1945
realDate  = 1945
if firstGuess < realDate:
    print("this game is to old, the end of WWII happend more recently than that!")


guess = int(input("What year did WWII end? >"))

if guess < realDate:
    print("this guess is too old, the end of WWII happened more recently than that!")
if guess > realDate:
    print("this guess is too recent, the end of WWII happened longer ago than that!")
if guess == realDate:
    print("This guess is correct!")



   """
