#Bryan Morris
#10/14/19
#Blue Moon

blueMoon = input("Is there a blue moon tonight (Yes/No)?")
weekDay = input("What is the day of the week (Monday - Sunday)")
monthDay = int(input("What is the day of the month (1 - 31)?"))

blueMoon = blueMoon.title()
weekDay = weekDay.title()

if blueMoon == "Yes":
    print("Once in a Blue Moon")
elif monthDay <= 7:
    if weekDay == "Monday":
        print("Manic Monday")
    elif weekDay == "Tuesday":
        print("Tuesday's Gone")
    elif weekDay == "Wednesday":
        print("Just Wednesday")
    elif weekDay == "Thursday":
        print("Sweet Thursday")
    elif weekDay == "Friday":
        print("Friday I'm in Love")
    elif weekDay == "Saturday":
        print("Saturday in the Park")
    elif weekDay == "Sunday":
        print("Lazing on a Sunday Afternoon")
    else:
        print("Days of the Week")
else:
    print("Day Dream Believer")

input()
