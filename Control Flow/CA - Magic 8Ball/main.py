import random

# Define Magic 8 ball statements
opt1 = "Yes - Definitely"
opt2 = "It is decidely so"
opt3 = "Without a doubt"
opt4 = "Reply hazy, try again"
opt5 = "Ask again later"
opt6 = "Better not tell you now"
opt7 = "My sources say no"
opt8 = "Outlook not so good"
opt9 = "Very doubtful"
opt10 = "Adopt more cats"
opt11 = "Ask again after drinking coffee"
opt12 = "Play Green Day"
# define user info
name = "Adam"
question = "Should I adopt another cat?"

# Gen random int
random_number = random.randint(1,12)

if name:
    print(name + " asks: " + question)
else:
    print("Question: " + question)

if  not question:
    print("Error! You did not ask a question. Please ask a question to continue!")
else:
    # Output Magic 8 Ball responses
    if random_number == 1:
        print("Magic 8-Ball's answer: " + opt1)
    elif random_number ==2:
        print("Magic 8-Ball's answer: " + opt2)
    elif random_number ==3:
        print("Magic 8-Ball's answer: " + opt3)
    elif random_number ==4:
        print("Magic 8-Ball's answer: " + opt4)
    elif random_number ==5:
        print("Magic 8-Ball's answer: " + opt5)
    elif random_number ==6:
        print("Magic 8-Ball's answer: " + opt6)
    elif random_number ==7:
        print("Magic 8-Ball's answer: " + opt7)
    elif random_number ==8:
        print("Magic 8-Ball's answer: " + opt8)
    elif random_number ==9:
        print("Magic 8-Ball's answer: " + opt9)
    elif random_number ==10:
        print("Magic 8-Ball's answer: " + opt10)
    elif random_number ==11:
        print("Magic 8-Ball's answer: " + opt11)
    elif random_number ==12:
        print("Magic 8-Ball's answer: " + opt12)

    else:
        print("Error")


