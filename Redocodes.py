import random as chidera
print("Welcome to Odera Redo Python!")
'''This program is to generate radom numbers that changes on refresh'''
a = 2024;b=2025;c=2030
'''for 2024'''
print("You Chose 2024")
first = (a+chidera.randint(2,5))
print("you have till ",(first), "to be rich")
print("Guess the random number and arithemetic")

def my_function():
    choose = input("Choose a number: ")
    if choose == first:
        print("Correct!")
    if choose != first:
        print("Incorrect!")
    return choose

while True:
    mf = my_function()
    tp = ''
    try:
        tp = type(int(mf)).__name__
    except: 
        tp = tt = type(mf).__name__
    if tp == 'int':
        break
    else:
        print("numbers only")

second = first+chidera.randint(10,15)
family = " to make your first family"
print("it will take you "+format(second)+ (family))
