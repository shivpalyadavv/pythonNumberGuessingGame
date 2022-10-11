import random
import math
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
#generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

#Intializing the number of guessess.
count = 0
#for calculation of min number of guessess depends upon range
while count < math.log(upper - lower + 1, 2):
      count += 1
      guess = int(input("Guess a number:- "))

      #condition testing
      if x == guess:
            print("Congratulation you did it n ", count, "try")
            break
      elif x > guess:
            print("You guessed too small")
      elif x < guess:
            print("You Guessed too high")
      #Shows this output.

      if count >= math.log(upper-lower +1, 2):
            print("\nThe number is %d" % x)
            print("\tBetter Luck Next time!")

