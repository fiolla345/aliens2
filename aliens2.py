#imports a library that allows for creation of pause throughout code
import time

# Lines 5-16 give the user a description 
print("This program is to figure out how many aliens")
time.sleep(0.4)
print("will be on earth after a certain amount of time passes.")
time.sleep(0.4)
print("----------------------------------------")
time.sleep(0.4)
print("Every alien from a generation that is")
time.sleep(0.4)
print("odd will be red and every even generation will be blue.")
time.sleep(0.4)
print("----------------------------------------")
time.sleep(0.8)

# Declare the variables 
firstLanding = int(input("How many aliens first landed on earth?"))
weeks = int(input("And how many weeks have they been on earth?"))

countingVar = 1

weeks2 = weeks 

#Tell the user that only the original population exists
if weeks == 0:
  print("There are only",firstLanding,"aliens on Earth")

#Tell the user how many aliens there are after (x) weeks
if weeks > 0:

  #added while loop to count the population week by week 
  while countingVar < (weeks + 1):
    print( firstLanding * (2 ** countingVar),"aliens are on earth after", countingVar ,"weeks")
    countingVar = countingVar + 1
    time.sleep(.5)
    
  print("----------------------------------------")
  time.sleep(.5)
  print("And now for the colors")
  time.sleep(.5)
  print("----------------------------------------")
  time.sleep(.5)

  #2nd while loop to destinguish generation and color 
  countingVar2 = 0

  while countingVar2 < (weeks2):
    if (countingVar2 + 1) % 2 == 0:
      print("The #", countingVar2 + 1, "generation will be blue")
    else:
      print("The #", countingVar2 + 1, "generation will be red")
    countingVar2 = countingVar2 + 1
    time.sleep(.5)
