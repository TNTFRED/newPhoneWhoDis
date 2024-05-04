import random

MAX_NUMBER_OF_QUESTIONS = 50



def arrayGenerator():
  numberOfQuestions = []

  for i in range(1,MAX_NUMBER_OF_QUESTIONS - 1):
    numberOfQuestions.append(i)
  return numberOfQuestions



def randomGenerator(x):

  numberOfQuestions = x
  number = random.choice(numberOfQuestions)
  numberOfQuestions.remove(number)
  print(f"{numberOfQuestions} the number removed is: {number}")
  if not number:
    print(f"error at number {number}")
  return number


numbersInList = arrayGenerator()

for i in range(1,MAX_NUMBER_OF_QUESTIONS-1):
  randomGenerator(numbersInList)

print(randomGenerator(numbersInList))
