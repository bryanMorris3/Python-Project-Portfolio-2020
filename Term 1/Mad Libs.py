#Bryan Morris
#9/19
#Mab Libs
#variables for words to be entered
word1 = input("Enter a Noun")
word2 = input("Enter a Noun")
word3 = input("Enter a Noun")
word4 = input("Enter an Occupation")
word5 = input("Enter a Verb")
word6 = input("Enter a Place")
word7 = input("Enter a Verb ending in 'ed' ")
word8 = input("Enter a Noun")
word9 = input("Enter a Verb ending in 'ing' ")
word10 = input("Enter a Noun")
word11 = input("Enter an Emotion")
#the mab lib
text = str.format("""
It was during the battle of {} when I was running through a {} when a {} went
off right next to my platoon. Our {} yelled for us to {} to the nearest {} we
could find. When we got to the {} we {} to start a fire. As we were starting the fire the enemy saw
the {} from the fire and started {} at us. We all quickly ducked behind the
{} at the {} and returned fire. We quickly eliminated the enemy and were {}
that we had won the battle.""",word1,word2,word3,word4,word5,word6,word6,word7,word8,word9,word10,word6,word11)
print(text)
