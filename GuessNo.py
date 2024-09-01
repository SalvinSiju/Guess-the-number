import random
import math
lower=int(input("Enter the lower bound"))
high=int(input("Enter the higher bound"))
x = random.randint(lower,high)
chances = random.randint(1, int(math.log(high - lower + 1, 2)) + 5)
count=0
flag=0
while chances>count:
    count+=1
    guess=int(input("Enter a number:"))
    if guess==x:
        print("Congratulation you made it in",count)
        flag=1
        break
    elif x>guess:
        print("your guess is smaller than actual value")
    elif x<guess:
        print("your guess is greate than actual value")
if flag==0:
    print("Better luck next time")


