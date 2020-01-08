#Bryan Morris
#12/3/19
#Python 1-2 2019 Midterm Exam

import sys

def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        return file
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()

def next_line(the_file):
    line = the_file.readline()
    line = line.strip("\n")
    line = line.replace("/","\n")
    return line

def question_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to my Python Trivia Challenge!\n")
    print("\tthis test was created by", title, "\n")

def get_file_name():
    while True:
        file_name = input ("enter in the name of your file including the .txt")
        if ".txt" in file_name and " " not in file_name:
            return file_name
        else:
            print("not a good file name")
    
def main():
    file_name = get_file_name()
    file = open_file(file_name, "r")
    title = next_line(file)
    user_name = input("Enter your full name")
    questions = 0
    score = 0
    category, question, answers, correct, explanation = question_block(file)
    welcome(title)
    while category:
        print(category)
        print()
        print(question)
        print()
        for i in range(len(answers)):
            print("\t", i + 1, "-", answers[i])
        user_answer = input("What is your answer?: ")
        if user_answer == correct:
            print("Correct!")
            score += 1
            questions += 1
        else:
            print("wrong")
            questions += 1
        print()
        print(explanation)
        category, question, answers, correct, explanation = question_block(file)
    file.close()
    print("That was the last question!")
    input("press enter to see your report card")
    report_card(user_name, questions, score)
        
            
        


def report_card(user_name, questions, score):
    point_worth = 100.0/questions 
    final_score = score*point_worth
    letter = None
    message = None
    if final_score >= 90:
        letter = "A"
        message = "Great job!"
    elif final_score >= 80:
        letter = "B"
        message = "That's okay."
    elif final_score >= 70:
        letter = "C"
        message = "You passed."
    elif final_score >= 60:
        letter = "D"
        message = "Try harder next time."
    elif final_score <= 59:
        letter = "F"
        message = "You Failed!"
    card = str.format("""
    *****************
    Report Card
    *****************
        Student: {}
        You Answered {}/{} Correct
        Each Question was worth {} points
        You Received {}/100.0 points
        You Got a {}%

        {}

        {}

    *************************
     """,user_name,score,questions,point_worth,final_score,final_score,letter,message)
    print(card)

main()
input("press enter to close")
