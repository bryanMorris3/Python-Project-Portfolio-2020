#Bryan Morris
#10/28/19
#

import random


#Get a number
def checkNum(message):
    while True:
        opt = input(message)
        if opt.isdigit():
            opt = int(opt)
            return opt
        print("Not a number")

#Get a number in the range
def getNumInRange(message,rmin,rmax):
    while True:
        guess = checkNum(message)
        if guess >= rmin and guess <= rmax:
                return guess
        print("not a good value")

#How to confirm
def confirm(message):
    while True:
        answer = input(message)
        answer = answer.lower()
        if "y" in answer:
            return True
        elif "n" in answer:
            return False
        print("not a good option")
        
#The game menu
def menu(rmin,rmax,maxGuess):
    print("""
                    |MENU|
                Difficulty Menu: press 1
                Play Game: press 2
                Quit: press 3
        """)
    while True:
        opt = getNumInRange("Choose an option from 1 to 3\n",1,3)
        if opt ==1:
            optionsMenu()
        elif opt == 2:
            guessGame(rmin,rmax,maxGuess)
        elif opt == 3:
            x = confirm("Do you want to quit")
            if x:
                quit()
            else:
                continue
                

#The options menu
def optionsMenu():
    while True:
        print("""
                    |OPTIONS|
                Easy: press 1
                Normal: press 2
                Hard: press 3
                Custom: press 4
        """)
        opt = getNumInRange("Choose an option from 1 to 4\n",1,4)
        global maxGuess
        global rmin
        global rmax
        while True:
            if opt ==1:
                maxGuess = 5
                rmin = 1
                rmax = 7
                guessGame(rmin,rmax,maxGuess)
            elif opt == 2:
                maxGuess = 3
                rmin = 1
                rmax = 10
                guessGame(rmin,rmax,maxGuess)
            elif opt == 3:
                maxGuess = 3
                rmin = 1
                rmax = 50
                guessGame(rmin,rmax,maxGuess)
            elif opt == 4:
                pass



#The main game
def guessGame(rmin,rmax,maxGuess):
    guessCount = 0
    theNumber = random.randint(rmin,rmax)
    while True:
        guessedNum = getNumInRange("Guess a number between " + str(rmin) + " and " + str(rmax) ,rmin, rmax)
        guessCount += 1
        while guessCount != maxGuess and guessedNum != theNumber:
            if guessedNum > theNumber:
                print("guess lower")
            else:
                print("guess higher")
            guessedNum = getNumInRange("Guess a number between " + str(rmin) + " and " + str(rmax) ,rmin,rmax)
            guessCount += 1
        if guessedNum == theNumber:
            print("You Won!")
            break
        else:
            print("You Lost!")
            break

maxGuess = 3
rmin = 1
rmax = 10

menu(rmin,rmax,maxGuess)
