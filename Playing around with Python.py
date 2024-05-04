import math

x = 1 # First number input
y = 2  # Second number input
z = 3 # Third number input

def addNum(x,y):        # add the numbers
    sum = x + y

    return sum

def subNum(x,y):        # subtract the numbers
    sum = x - y

    return sum

def multNum(x,y):       # multiply the numbers
    sum = x * y

    return sum

def divNum(x,y):        # divide the numbers
    sum = x / y

    return sum

def modNum(x,y):        # find the remainder
    sum = x % y

    return sum

def highOrLow(x,y):     # check if x higher than y
    temp = True
    if x > y:           # if x is greater than y then set temp to true
        temp = True
    else:               # else set temp to false
        temp = False

    return temp

def countTheDif(x,y):   # count the numbers between x and y
    for i in range(x,(y + 1)):  # print every number from x to y
        print (i)

    return

def testFunction():     # test function to play around with
    array = [x,y,z]
    for i in range(x,y):    # add i to every index of the array
        array = [x*i,y*(2*i), z*(3*i)]

    return array
"""
print (addNum(x,y))
print (subNum(x,y))
print (multNum(x,y))
print (divNum(x,y))
print (modNum(x,y))
print (highOrLow(x,y))
print (countTheDif(x,y))
"""
print (testFunction())