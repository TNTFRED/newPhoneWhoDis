firstNumber = ""
secondNumber = ""
operation = ""

def main():

    firstNumber = firstNumberFunction()
    secondNumber = secondNumberFunction()
    operation = opertationFunction()

    simpleCalculator(firstNumber, secondNumber, operation)

    return

def simpleCalculator(x,y,z):
    if z == "+":
        total = x + y
    if z == "-":
        total = x - y
    if z == "*":
        total = x * y
    if z == "/":
        total = x / y
    if z == "^":
        total = x ** y
    return total
    
def firstNumberFunction():
    try:
            userInput = float(input("first number "))
    except ValueError:
            print("Not a Valid Number")
    return userInput

def secondNumberFunction():
     try:
          userInput = float(input("Second number "))
     except ValueError:
          print("Not a Valid Number")
     return userInput

def opertationFunction():
     userInput = input("Choose Operation ")

     if userInput != "+" or "-" or "*" or "/" or "^":
          print("Not a Valid Opertaion")
     else: 
          return userInput


print(main())