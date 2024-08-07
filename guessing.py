import random
import math
low = int(input("Enter lower boundary: "))
up = int(input("Enter upper boiundary: "))
x=random.randint(low,up)
chances = 5
print("you are only having the total " ,chances," to guess the number")
count = 0
flag = False
while count<chances:
    count+=1;
    guess = int(input("Guess a number: "))
    if x==guess:
        print("Congratulations!, you guessed the correct number")
        flag = True
        break
    elif x>guess:
        print("You guessed too high!")
    elif x<guess:
        print("You guessed too low!")
if not flag:
    print("\nThe number is %d" % x)
    print("\nBetter luck next time!")