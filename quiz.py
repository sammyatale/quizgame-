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
if answer.lower() == "application Programming Interface":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" "What is the main purpose of a firewall? ")
if answer.lower() == "to protect network from unauthorized access":
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

answer = input("question :" " Which programming language is commonly used for developing mobile applications for both iOS and Android platforms? ")
if answer.lower() == "Swift":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" " Which technology is used for wireless communication between devices over short distances, such as transferring files between smartphones? ")
if answer.lower() == "Bluetooth":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" " In the context of cloud computing, what does the acronym 'IaaS' stand for? ")
if answer.lower() == "Infrastructure as a Service":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" " Which company developed the programming language 'JavaScript'? ")
if answer.lower() == "Netscape":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" " What does the term 'URL' stand for in the context of web addresses? ")
if answer.lower() == "Uniform Resource Locator":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" " What is the function of an accelerometer in a smartphone or tablet? ")
if answer.lower() == "Detect motion and orientation":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" " What does OOP stand for ? ")
if answer.lower() == "Object-oriented programming":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')

answer = input("question :" " What does OOP stand for ? ")
if answer.lower() == "Object-oriented programming":
    print('correct..!')
    score += 1
else:
    print('Incorrect..!')


print("your score is " + str(score)+ " questions correct!")
