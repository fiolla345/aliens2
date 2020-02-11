import time

firstLanding = int(input("How many aliens first landed on earth?"))
weeks = int(input("And how many weeks have they been on earth?"))

countingVar = 1

if weeks == 0:
  print("There are only",firstLanding,"aliens on Earth")
#
while countingVar < (weeks + 1):
  print( firstLanding * (2 ** countingVar),"are on earth after", countingVar ,"weeks")
  countingVar = countingVar + 1
  time.sleep(.5)
