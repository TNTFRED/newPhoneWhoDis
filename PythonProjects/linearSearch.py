# This program is playing with linear searches, one made by Sam Fred(searchList())

LIST_LENGTH = 100000000
TARGET_NUMBER = 99999999


# The populateList() populates the list with numbers

def populateList():
  testList = []
  for i in range(LIST_LENGTH):
    testList.append(i)

  return testList

# The searchList() function is a linear search algorithim thought of by Sam Fred 

def searchList(target):
  list = populateList()
  found = "Not in Array"
  for index in range(LIST_LENGTH):
    if list[index] == target:
      found = f"{list[index]} found"
  return found



print(searchList(TARGET_NUMBER))