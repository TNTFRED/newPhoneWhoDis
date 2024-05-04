
def answers():
  answer = ['i', 'n']
  return answer

def verification(user_input, answerKey):
  userAnswer = user_input.split(',')
  validAnswers = []

  for answers in userAnswer:
      answers = answers.strip()

      if answers in answerKey:
          validAnswers.append(answers)
  return validAnswers

def main():
    answerKey = answers()
    user_input = input("Spell IN separated by commas: ")
    validAnswers = verification(user_input, answerKey)

    if validAnswers:
        review = 1
    else:
        review = 0
    return review