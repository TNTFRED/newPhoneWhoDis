# This program is playing with binary searches, one made by Sam Fred(searchList()) then a ChatGPT implemented binary search

LIST_LENGTH = 10
TARGET_NUMBER = 5


# The populateList() populates the list with numbers

def populateList():
  testList = []
  for i in range(LIST_LENGTH):
    testList.append(i)

  return testList

print(populateList())