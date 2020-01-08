import random

PUZZLE = "HFFMFGZUAHZMCOVIJNLINTEGERBOBWDJCIAUIYEHLCMINTOGSPKFBJTOJMGLMZWTYTSUBLOMEQXBOYLTRTRNIPYNTEXSVOHYAYOCJATJLCTACOATTPJTJOCSFRRANSEURWHILEYLIILCCMPIBUHOHNONANYIELNLGUYNTAGBWPINETJSTNUATHLUKUTBOOLEANXBDEGSJTVRILPABEERRORPFXXUNFYYP"
PUZZLE  = PUZZLE.replace(" ","")


def display_puzzle2(puzzle):
     x = 0
     y = 1
     for i in range (15):
         print()
         for i in range (15):
            print(puzzle[x:y], end = "|")
            x += 1
            y += 1





WORDS =["function",#(51,67,83,99,115,131,147,163)
     "variable",#(92,107,122,137,152,167,182,197)
     "syntax",#(119,134,149,164,179,194)
     "print",#(113,128,143,158,173)
     "input",#(137,153,169,185,201)
     "Python",#(49,64,79,94,109,124)
     "integer",#(19,20,21,22,23,24,25)
     "float",#(120,135,150,165,180)
     "boolean",#(187,188,189,190,191,192,193)
     "string",#(91,106,121,136,151,166)
     "comment",#(12,27,42,57,72,87,102)
     "while",#(129,130,131,132,133)
     "ifstatement",#(36,51,66,81,96,111,126,141,156,171,186)
     "try",#(65,80,95)
     "list",#(18,33,48,63)
     "tuple",#(112,127,142,157,172)
     "ASCII",#(110,125,140,155,170)
     "error",#(210,211,212,213,214)
     "loop",#(40,55,70,85)
     "local"#(78,93,108,123,138)
        ]

QUESTIONS = ["What is a block of re-usable block of code that can be in any place in your code?",
             "What is a storage area for a peice of data?",
             "What are the set of rules for a language?",
             "What is a function that will display a value to the screen?",
             "Which function will let you ask the user a question and get a response back?",
             "Which programming language are we using in our class this year?",
             "Which data type will let you store whole numbers?",
             "Which data type holds numbers with a decimal?",
             "Which data type has only two possible values, True or False?",
             "Which data type has to be surrounded in quotation marks?",
             "What is a line of code that is not acknowledged by the program and just for human readers?",
             "Which kind of loop will keep running as long as a logical expression is true?",
             "What will make a group of code run only if a logical expression is true?",
             "What will make a code run, but if it doesn't work it will do something else?",
             "What is a type of variable that can hold multiple data values and surrounded by brackets?",
             "What is a type of variable that can hold multiple data values and can't be changed?",
             "What is the American Standard Code for Information Interchange?",
             "What is a problem in your code that could not let it run, halt it, or return something wrong back?",
             "What will let you execute the same group of code repeatedly?",
             "What kind of variable is only used in a function then deleted after the function ends?"]

# game data
picked = []


print()
print()

def rand_question(words, questions):
     copyquest = questions
     copyword = words
     picked = random.randint(0,len(copyword)-1)
     asked_words = words.pop(picked)
     asked_question = questions.pop(picked)    
     return asked_question, asked_words



def get_word(puzzle):
     while True:
          num=[]
          placement= ""
          find= input("Input your placement for the word your looking for (in order)")
          for i in find:
               if i != ",":
                    placement = placement + i
               else:
                    if placement.isdigit():
                         num.append(int(placement))
                         placement= ""
          num.append(int(placement))
          if num[0]+1 == num[1]  or num[0]-1 == num[1] or num[0]+15 == num[1] or num[0]-15 == num[1]\
          or num[0]+16 == num[1] or num[0]+14 == num[1] or num[0]-16 == num[1] or num[0]-14 == num[1]:
               print("Good Word!")
               word= ""
               while num:
                    x= num.pop(0)
                    word = word + puzzle[x]
               print(word)
               return word
          else:
               print("You cheater!")


def main_game(words,questions,puzzle):
     score = 0
     display_puzzle2(puzzle)
     print()
     print()
     while QUESTIONS:          
          asked_question, asked_words = rand_question(words,questions)
          asked_words = asked_words.upper()
          print(asked_question)
          input_word = get_word(PUZZLE)
          print("The answer is ", asked_words)
          if input_word == asked_words:
               print("Correct!")
               score += 1
          else:
               print("Incorrect")
          print()
     print()
     print("Your final score is :", score)
          
main_game(WORDS,QUESTIONS,PUZZLE)
input()
