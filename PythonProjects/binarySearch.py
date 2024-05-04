# This program is playing with binary searches, one made by Sam Fred(searchList()) then a ChatGPT implemented binary search

LIST_LENGTH = 100000000
TARGET_NUMBER = 99999999


# The populateList() populates the list with numbers

def populateList():
  testList = []
  for i in range(LIST_LENGTH):
    testList.append(i)

  return testList


# The searchList() function is a binary search algorithim thought of by Sam Fred 

def searchList(target):
  list = populateList()
  found = "Not in Array"

  if TARGET_NUMBER <= (LIST_LENGTH/2):
    for index in range(0, LIST_LENGTH, 1):
      if list[index] == target:
        found = f"{list[index]} found"
        break

  elif TARGET_NUMBER > (LIST_LENGTH/2) and TARGET_NUMBER <= LIST_LENGTH:
    for index in range(LIST_LENGTH, 0, -1):
      if list[index-1] == target:
        found = f"{list[index-1]} found"
        break

  elif TARGET_NUMBER > LIST_LENGTH:
    found = "Not in Array"
    
  return found


# The binarySearch() is a function implimented by ChatGPT

def binarySearch(target):
  list = populateList()
  found = "Not found"
  
  left = 0
  right = len(list) - 1

  while left <= right:
    mid = (left + right) // 2
    if list[mid] == target:
      return mid
    elif list[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return found


# print(binarySearch(TARGET_NUMBER))
print(searchList(TARGET_NUMBER))