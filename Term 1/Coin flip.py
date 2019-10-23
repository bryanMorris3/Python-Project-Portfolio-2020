#Bryan Morris
#9/25/19
#
import random
def coinFlip(x):
    if x.isdigit():
        x=int(x)
        if x > 0:
            for i in range(x):
                coin = random.randint(1,2)
                if coin == 1:
                    print("heads")
                if coin == 2:
                    print("tails")
        else:
            print("Not a good range")
    else:
        print("Not a good range")  
x = input("How many times do you want to flip?")
coinFlip(x)

input()
