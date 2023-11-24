print("Welcome...! To my quiz game....")

playing = input("Do you want to play our quiz game? ")

if playing.lower() == "yes":
    print("Well..! Let's play...")
else:
    print("Maybe next time. Goodbye!")

score = 0

'''fields = input('Enter your field   1. technology, 2. Agriculture, 3. Science')
if fields.lower() == "technology":'''


answer = input("question :" "What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question:" "In programming, what does API stand for? ")
if answer.lower() == "application arogramming anterface":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" "What is the main purpose of a firewall? ")
if answer.lower() == "to protect a network from unauthorized access":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" "Which programming language is known for its use in machine learning and data analysis? ")
if answer.lower() == "python":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')


print("your score is " + str(score)+ " questions correct!")
