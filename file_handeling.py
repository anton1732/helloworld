#opening, reading and printing a file
"""
file handeling is where you interact with the file on the computer 
by defualt the read methed returnes the whole text but u can aslo spicify how many charecters u want to return 
"""



f = open("txt_file.txt", "r")
print(f.read())

print(f.read(5))
print(f.read(7))
print(f.read(10))
print(f.read(3))
