import random

number = random.randint(0, 200)

while True:
    answer = input("Please, enter your number: ")
    if answer == '' or answer == 'exit':
        print("Finish of work")
        break
    if not answer.isdigit():
        print("Enter correct number")
        continue

    answer = int(answer)

    if answer == number:
        print("You are the winner")
        break
    elif answer < number:
        print("Number is bigger")
    else:
        print("Number is lower")