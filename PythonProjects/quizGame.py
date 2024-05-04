# This is a simple quiz game
# there are currently 0 questions

import random

MAX_NUMBER_OF_QUESTIONS = 0 #should be set to the max questions input or anything less as there are not enough questions made (there is room for 40 questions)
def arrayGenerator():
  numberOfQuestions = []
  for i in range(0,MAX_NUMBER_OF_QUESTIONS):
    numberOfQuestions.append(i)
  return numberOfQuestions

def randomGenerator(x):
  numberOfQuestions = x
  number = random.choice(numberOfQuestions)
  numberOfQuestions.remove(number)

  # number = 0 # For testing a question
  return number

def questions():
  question = ""
  if  randomNumber == 0:
    question = "? "
  elif randomNumber == 1:
    question = "? "
  elif randomNumber == 2:  
    question = "? "
  elif randomNumber == 3:  
    question = "? "
  elif randomNumber == 4:
    question = "? "
  elif randomNumber == 5:  
    question = "? "
  elif randomNumber == 6:  
    question = "? "
  elif randomNumber == 7:
    question = "? "
  elif randomNumber == 8:  
    question = "? "
  elif randomNumber == 9:  
    question = "? "
  elif randomNumber == 10:
    question = "? "
  elif randomNumber == 12:  
    question = "? "
  elif randomNumber == 13:  
    question = "? "
  elif randomNumber == 14:
    question = "? "
  elif randomNumber == 15:  
    question = "? "
  elif randomNumber == 16:  
    question = "? "
  elif randomNumber == 17:
    question = "? "
  elif randomNumber == 18:  
    question = "? "
  elif randomNumber == 19:  
    question = "? "
  elif randomNumber == 20:
    question = "? "
  elif randomNumber == 21:  
    question = "? "
  elif randomNumber == 22:  
    question = "? "
  elif randomNumber == 23:
    question = "? "
  elif randomNumber == 24:  
    question = "? "
  elif randomNumber == 25:  
    question = "? "
  elif randomNumber == 26:
    question = "? "
  elif randomNumber == 27:  
    question = "? "
  elif randomNumber == 28:  
    question = "? "
  elif randomNumber == 29:
    question = "? "
  elif randomNumber == 30:  
    question = "? "
  elif randomNumber == 31:  
    question = "? "
  elif randomNumber == 32:
    question = "? "
  elif randomNumber == 33:  
    question = "? "
  elif randomNumber == 34:  
    question = "? "
  elif randomNumber == 35:
    question = "? "
  elif randomNumber == 36:  
    question = "? "
  elif randomNumber == 37:  
    question = "? "    
  elif randomNumber == 38:  
    question = "? "
  elif randomNumber == 39:  
    question = "? " 
  elif randomNumber == 40:  
    question = "? "
  elif randomNumber == 41:  
    question = "? "
  elif randomNumber == 42:
    question = "? "
  elif randomNumber == 43:  
    question = "? "
  elif randomNumber == 44:  
    question = "? "
  elif randomNumber == 45:
    question = "? "
  elif randomNumber == 46:  
    question = "? "
  elif randomNumber == 47:  
    question = "? "    
  elif randomNumber == 48:  
    question = "? "
  elif randomNumber == 49:  
    question = "? " 


  elif randomNumber != range(0,MAX_NUMBER_OF_QUESTIONS):
    print("Random Number Error")
  return question

def answers():
  answer = ""
  if  randomNumber == 0:
    answer = ""
  elif randomNumber == 1:
    answer = ""
  elif randomNumber == 2:  
    answer = ""
  elif randomNumber == 3:  
    answer = ""
  elif randomNumber == 4:
    answer = ""
  elif randomNumber == 5:  
    answer = ""
  elif randomNumber == 6:  
    answer = ""
  elif randomNumber == 7:
    answer = ""
  elif randomNumber == 8:  
    answer = ""
  elif randomNumber == 9:  
    answer = ""
  elif randomNumber == 10:
    answer = ""
  elif randomNumber == 12:  
    answer = ""
  elif randomNumber == 13:  
    answer = ""
  elif randomNumber == 14:
    answer = ""
  elif randomNumber == 15:  
    answer = ""
  elif randomNumber == 16:  
    answer = ""
  elif randomNumber == 17:
    answer = ""
  elif randomNumber == 18:  
    answer = ""
  elif randomNumber == 19:  
    answer = ""
  elif randomNumber == 20:
    answer = ""
  elif randomNumber == 21:  
    answer = ""
  elif randomNumber == 22:  
    answer = ""
  elif randomNumber == 23:
    answer = ""
  elif randomNumber == 24:  
    answer = ""
  elif randomNumber == 25:  
    answer = ""
  elif randomNumber == 26:
    answer = ""
  elif randomNumber == 27:  
    answer = ""
  elif randomNumber == 28:  
    answer = ""
  elif randomNumber == 29:
    answer = ""
  elif randomNumber == 30:  
    answer = ""
  elif randomNumber == 31:  
    answer = ""
  elif randomNumber == 32:
    answer = ""
  elif randomNumber == 33:  
    answer = ""
  elif randomNumber == 34:  
    answer = ""
  elif randomNumber == 35:
    answer = ""
  elif randomNumber == 36:  
    answer = ""
  elif randomNumber == 37:  
    answer = ""
  elif randomNumber == 38:  
    answer = ""
  elif randomNumber == 39:  
    answer = "" 
  elif randomNumber == 40:  
    answer = ""
  elif randomNumber == 41:  
    answer = ""
  elif randomNumber == 42:
    answer = ""
  elif randomNumber == 43:  
    answer = ""
  elif randomNumber == 44:  
    answer = ""
  elif randomNumber == 45:
    answer = ""
  elif randomNumber == 46:  
    answer = ""
  elif randomNumber == 47:  
    answer = ""
  elif randomNumber == 48:  
    answer = ""
  elif randomNumber == 49:  
    answer = ""     


  elif randomNumber != range(0,MAX_NUMBER_OF_QUESTIONS):
    print("Random Number Error")
  return answer

def verification():
  UserAnswer = input(questions()).lower()
  if UserAnswer == answers():
    review = 1
  else:
    review = 0
  return review

while True:
  print("Let's play a game")
  numbersInList = arrayGenerator()
  playing = (input(f"Are you in? There will be {MAX_NUMBER_OF_QUESTIONS} different questions: ")).lower()
  if playing == "yes":
    score = 0
    for i in range(0,MAX_NUMBER_OF_QUESTIONS):
      randomNumber = randomGenerator(numbersInList)
      questions()
      answers()
      value = verification()
      if value == 1:
        score += 1
        print("Correct!")
      elif value == 0:
        print("Incorrect")
    print(f"Your score is: {score}/{MAX_NUMBER_OF_QUESTIONS}")
    quit()
  elif playing == "no":
    print("Quitting Game")
    quit()