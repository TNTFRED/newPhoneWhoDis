# This is a simple quiz program
# there are currently 50 questions (numbers 11, 49, 51 still need questions and answers)
# Currently set up for PSYCH 1200 Test #3

import random

MAX_NUMBER_OF_QUESTIONS = 50 #should be set to the max questions input or anything less as there are not enough questions made (there is room for 40 questions)


def arrayGenerator():
  numberOfQuestions = []

  for i in range(1,MAX_NUMBER_OF_QUESTIONS + 1):
    numberOfQuestions.append(i)
  return numberOfQuestions



def randomGenerator(x):
  numberOfQuestions = x
  number = random.choice(numberOfQuestions)
  numberOfQuestions.remove(number)

  #number = 22 # For testing a question (total questions - 1)
  if not number:
    print("problem")
    return
  return number



def questions(randomNumber, y):
  
  if randomNumber == 1:
    question = "Binet and Simon developed a method where a child performed various cognitive tasks relative to other children of his/her age. What are the two key elements of the method? "
  elif randomNumber == 2:  
    question = "What are the five abilities tested for in intelligence? (Make a list spaced out by commas EX: one, two, three, four, five) "
  elif randomNumber == 3:  
    question = "Who was the first to measure intelligence through Anthropometrics? "
  elif randomNumber == 4:
    question = "Who modified Binet's test to asses high achieving adults? (Standfor-Binet scale) "
  elif randomNumber == 5:  
    question = "Who developed intelligence quotient? (IQ) "
  elif randomNumber == 6:  
    question = "What is the term used for the average intellectual ability score for children of specific age? "
  elif randomNumber == 7:
    question = "What is the IQ of a person who is 14 years old but has a mental age of 7? "
  elif randomNumber == 8:  
    question = "If someone has an IQ of 130 have many standard deviations are to from the average? "
  elif randomNumber == 9:  
    question = "What does GAI stand for? "
  elif randomNumber == 10:
    question = "What does CPI stand for? "
  elif randomNumber == 11:
    question = ""
  elif randomNumber == 12:  
    question = "What are the three elements of Verbal Comprehension Index? "
  elif randomNumber == 13:  
    question = "What are the two/three elements of Perceptual Reasoning Index? "
  elif randomNumber == 14:
    question = "What are the two elements of Working Memory Index? "
  elif randomNumber == 15:  
    question = "What are the two elements of Processing Speed Index? "
  elif randomNumber == 16:  
    question = "Is promoting the idea that certain groups of people are more intelligent then others based on race or ethnicity is an example of what? "
  elif randomNumber == 17:
    question = "What are the 3 reasons why there may be race differences in IQ testing? "
  elif randomNumber == 18:  
    question = "If someone belongs to a stereotypically considered less inteligent group, it can create anxiety about confirming this stereotype thus leading to lower scores. What is this an example about? "
  elif randomNumber == 19:  
    question = "What are the two types of intelligence defined by Carol dweck? "
  elif randomNumber == 20:
    question = "What is the type of intelligence defined by Carol Dweck that states the belief that inteligence is fixed characteristic that is difficult/impossible to change? "
  elif randomNumber == 21:  
    question = "What is the type of intelligence defined by Carol Dweck that states the belief that inteligence can be shaped by experiences, practice and effort? "
  elif randomNumber == 22:  
    question = "Those who rate high in general intelligence should do well in math, language, and mechanics correct? "
  elif randomNumber == 23:
    question = "What is a type of intelligence used in learning new info and solving new problems not based on knowledge the person already has ? "
  elif randomNumber == 24:  
    question = "Where in the bell curve of IQ scores would you find a score of 145? "
  elif randomNumber == 25:  
    question = "Helena is completing the vocabulary and similarities of the WAIS (Wechsler Adult Intelligence Scale). What are these components designed to measure? "
  elif randomNumber == 26:
    question = "Jamal takes academic and intellectual risks such as enrolling in challenging classes and solving complicated analytical problems. Jamal likely believes that intelligence is...? "
  elif randomNumber == 27:  
    question = "While Sophie can solve analytical problems well, Max has extraordinary insight and knowledge of facts about World War II. It is likely that Sophie is high in ____________, while Max is high in ________________. (seperate answers by commas) "
  elif randomNumber == 28:  
    question = "According to Gardner's multiple intelligences, a(n) ____________ would rely on verbal/linguistic intelligence whereas a(n) ____________ would utilize interpersonal intelligence. (seperate answers by commas) "
  elif randomNumber == 29:
    question = "On which type of task would a man typically perform better than a woman? "
  elif randomNumber == 30:  
    question = "One explanation of the Flynn effect suggests that earlier tests might have ____________ the intelligence of earlier generations because the tests were ________ sophisticated and _________ culture-fair. (seperate answers by commas) "
  elif randomNumber == 31:  
    question = "You are investigating how stress levels affect academic achievement. You decide to collect data from middle school students, high school students, undergraduate, and graduate students at one point in time. You are using a __________ design. "
  elif randomNumber == 32:
    question = "As a ___________, ____________ consumption during prenatal development particularly causes learning disabilities, physical growth retardation, facial malformations, and behavioural disorders. "
  elif randomNumber == 33:  
    question = "Research on children's development of motor milestones suggests that while there are _______________ limits on development, _____________ shape the variations in motor development. "
  elif randomNumber == 34:  
    question = "Carly's kids love cookies. They each get one cookie every day after dinner. Stella's cookie broke in half, and Hannah starts to cry because her sister has more cookie than she does! Hannah has not mastered _____________. She is likely in Piaget's _____________ stage. "
  elif randomNumber == 35:
    question = "Alexa is three years old. She sees a zebra and calls it a horse, because they think any large four legged animal with a tail should be a horse. Alexa's thinking represents an example of ___________ according to Piaget. "
  elif randomNumber == 36:  
    question = "As compared to Piaget's theory, Vygotsky's theory of cognitive development best explains how a child learns to ___________. "
  elif randomNumber == 37:  
    question = "Some infants continuously cling to their caregivers, they don't necessarily explore their environment, protest to their caregivers upon their return if they were left alone, and they are usually difficult to soothe. Which of the following is the attachment style of these infants based on the Strange Situation? "    
  elif randomNumber == 38:  
    question = "Celia puts some gummy worms in a crayon box and offers them to her sister. What cognitive skill must Celia have mastered for them to know their sister will be fooled by the trick? "
  elif randomNumber == 39:  
    question = "Eric slept in and has missed an exam! He does not speed on his drive to get to the university, however, because Eric doesn't want to break the law. His thought process reflects which of the following? " 
  elif randomNumber == 40:  
    question = "Susie has just moved into a new home. All of her close friends have serious boyfriends. She likes the idea of a romantic partner but is also enjoying being alone and independent in her new space. According to Erikson, which psychosocial conflict describes her situation? "
  elif randomNumber == 41:  
    question = "Jeannie and Tim are 80 years old and have been married since they were 24. At what point in their lives will their marriage satisfaction be the lowest? "
  elif randomNumber == 42:
    question = "Which of the following experiments uses a high amplitude sucking procedure? "
  elif randomNumber == 43:  
    question = "During which stage does a child master conservation? "
  elif randomNumber == 44:  
    question = "Lucy has not eaten in several hours, and her blood sugar is dropping. Which part of Lucy's brain will tell her to eat by signalling feelings of hunger when it detects that her blood glucose is low? "
  elif randomNumber == 45:
    question = "Nicole has an eating disorder and is severely underweight. She typically eats 200-400 calories a day. What eating disorder is Nicole MOST likely experiencing? "
  elif randomNumber == 46:  
    question = "Which of the following is a critique of the research on sexual behaviour conducted by Alfred Kinsey? "
  elif randomNumber == 47:  
    question = "Gary is a gay man, and his brother Harry is a heterosexual man. Based on this difference in sexual orientation, which part of the two men's brains is likely to DIFFER THE MOST in size? "    
  elif randomNumber == 48:  
    question = "Lucinda is working on a creaky old boat this summer as part of a research team. Which of the following needs does Lucinda need to have in place before she pursues her need to belong with the crew? "
  elif randomNumber == 49:  
    question = "? " 
  elif  randomNumber == 50:
    question = "What is the historical terms refering to the method of measuring physical and mental variations in humans? (what and what) "
  elif  randomNumber == 51:
    question = "?"

  elif randomNumber != range(1,y):
    print(f"Random Number Error, the number is: {randomNumber}")
    return None
  return question



def answers(randomNumber,y):

  if randomNumber == 1:
    answer = ["anthropometrics", "anthropometric"]
  elif randomNumber == 2:  
    answer = ["thinking", "understanding", "reasoning", "adapting to", "overcoming"]
  elif randomNumber == 3:  
    answer = ["francis galton", "galton"]
  elif randomNumber == 4:
    answer = ["louis terman", "terman"]
  elif randomNumber == 5:  
    answer = ["william stern", "stern"]
  elif randomNumber == 6:  
    answer = ["mental", "age"]
  elif randomNumber == 7:
    answer = ["50"]
  elif randomNumber == 8:  
    answer = ["2","2 standard deviations"]
  elif randomNumber == 9:  
    answer = ["general ability index"]
  elif randomNumber == 10:
    answer = ["cognitive proficiency index"]
  elif randomNumber == 11:
    answer = [""]
  elif randomNumber == 12:  
    answer = ["similarities", "vocabulary", "information"]
  elif randomNumber == 13:  
    answer = ["visual puzzels", "matrix reasoning"]
  elif randomNumber == 14:
    answer = ["digit span", "arithmetic"]
  elif randomNumber == 15:  
    answer = ["symbol search", "coding"]
  elif randomNumber == 16:  
    answer = ["social darwinism", "eugenics"]
  elif randomNumber == 17:
    answer = ["the tests are culturally biased", "cultural bias", "the process of testing itself is biased", "testing itself is bias", "stereotype threat"]
  elif randomNumber == 18:  
    answer = ["stereotype threat"]
  elif randomNumber == 19:  
    answer = ["entity theory", "incremental theory", "incremental", "entitiy"]
  elif randomNumber == 20:
    answer = ["entity theory"]
  elif randomNumber == 21:  
    answer = ["incremental theory"]
  elif randomNumber == 22:  
    answer = ["yes", "correct"]
  elif randomNumber == 23:
    answer = ["fluid intelligence"]
  elif randomNumber == 24:  
    answer = ["upper tail", "top 2%", "top 2 percent"]
  elif randomNumber == 25:  
    answer = ["verbal comprehension"]
  elif randomNumber == 26:
    answer = ["a flexible process"]
  elif randomNumber == 27:  
    answer = ["fluid intelligence, crystalized intelligence"]
  elif randomNumber == 28:  
    answer = ["Linguist, psychologist"]
  elif randomNumber == 29:
    answer = ["mental rotation"]
  elif randomNumber == 30:  
    answer = ["underestimated, more, less"]
  elif randomNumber == 31:  
    answer = ["cross-sectional", "cross sectional"]
  elif randomNumber == 32:
    answer = ["teratogen, alcohol"]
  elif randomNumber == 33:  
    answer = ["physiological, parenting style and culture", "physiological, parenting style & culture"]
  elif randomNumber == 34:  
    answer = ["conservation, preoperational"]
  elif randomNumber == 35:
    answer = ["assimilation"]
  elif randomNumber == 36:  
    answer = ["do things that are hard to figure out alone", "things that are hard to figure out alone"]
  elif randomNumber == 37:  
    answer = ["insecure-anxious", "insecure anxious"]
  elif randomNumber == 38:  
    answer = ["theory of mind"]
  elif randomNumber == 39:  
    answer = ["conventional morality"] 
  elif randomNumber == 40:  
    answer = ["intimacy vs isolation", "intimacy vs. isolation","intimacy verse isolation"]
  elif randomNumber == 41:  
    answer = ["between the birth of their first child and their last child beginning school", "the birth of their first child and their last child beginning school", "between birth of first child and last child beginning school"]
  elif randomNumber == 42:
    answer = ["when babies suck a soother, they can control the story being played", "babies sucking a soother can control the story being played"]
  elif randomNumber == 43:  
    answer = ["preoperational"]
  elif randomNumber == 44:  
    answer = ["hypothalamus"]
  elif randomNumber == 45:
    answer = ["anorexia nervosa"]
  elif randomNumber == 46:  
    answer = ["he used too narrow a sample of individuals for his research", "his sample size was too narrow for his research"]
  elif randomNumber == 47:  
    answer = ["hypothalamus"]
  elif randomNumber == 48:  
    answer = ["safety needs"]
  elif randomNumber == 49:  
    answer = [""] 
  elif randomNumber == 50:
    answer = ["intelligence and mental age", "mental age and intelligence"]    
  elif randomNumber == 51:
    answer = [""] 

  elif randomNumber != range(1,y):
    #print(f"Random Number Error, the number is: {randomNumber}")
    return None
  return answer



def verification(user_input, answerKey):
  userAnswer = user_input.split(',')
  validAnswers = []

  for answers in userAnswer:
    answers = answers.strip()

    if answers in answerKey:
      validAnswers.append(answers)
  return validAnswers


def programCounter(x):
  elementsInArray = (MAX_NUMBER_OF_QUESTIONS + 1) - x
  return elementsInArray



def main():

  numbersInList = arrayGenerator()
  playing = (input(f"There will be {MAX_NUMBER_OF_QUESTIONS} different questions, Are you in? ")).lower()
  if playing == "yes":
    score = 0

    for i in range(1,MAX_NUMBER_OF_QUESTIONS + 1):
      elementsInArray = programCounter(i)
      randomNumber = randomGenerator(numbersInList)
      answerKey = answers(randomNumber, elementsInArray)
      print("\n----------------------------------------\n")
      print(f"Q: {MAX_NUMBER_OF_QUESTIONS - programCounter(i) + 1}/{MAX_NUMBER_OF_QUESTIONS}")
      print(f"questions/answer number: {randomNumber}")
      user_input = input(questions(randomNumber, elementsInArray))
      validAnswers = verification(user_input, answerKey)

      if validAnswers:
        score += 1
        print("Correct!")

      else:
        print("Incorrect")
        print(f"The correct answers: {answers(randomNumber, elementsInArray)}")
    print(f"Your score is: {score}/{MAX_NUMBER_OF_QUESTIONS}")
    quit()

  elif playing == "no":
    print("Quitting Game")
    quit()



while True:
  main()