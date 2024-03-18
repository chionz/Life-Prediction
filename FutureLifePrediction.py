#This Project is to calculate your age and tell you when to:
#make your first family
#become a millioniare
#your first child, boy or girl
#estimated date of death
print("This Year is 2024")
import random
year = 2024
#____Family
print("let's Find Year for Your First Family")
def my_function():
    global choose
    choose = int(input("Your Age? "))
    global birth
    birth = year - choose
    print("You are born in", birth)
    global family
    family = year + random.randint(27,45)
    print("You will make your first family in", family, "Age", family - birth, "years")
    if choose != "int":
        return choose

while True:
    mf = my_function()
    tp = 'str'
    try:
        tp = type(int(mf)).__name__
    except: 
        print('')
    if tp == 'int':
        break
    else:
        print("numbers only")

#____Millionaire
print("Lets Find What Year You Will Make Your First Million")
million = choose + random.randint(22,63)
print("You become a Millionaire in ", million)

#____First Child
child = family + random.randint(2,5)
male = 1
female = 2
gender = random.randint(0,3)
if gender > 1:
    print("Your First Child is in: ", child, "(Female)")
if gender <= 1:
    print("Your First Child is in: ", child, "(Male)")
#____Date of Death
death = birth + random.randint(70,120)
print("You will die in ", death, " Age", death-birth)
