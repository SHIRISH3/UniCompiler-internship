import random


print("***Guess Game***")
print("* Rules \n")
print("* 1 - 5 attempts will be given to find.\n ")
print("* 2 - every wrong answer will be deduct the points \n")
print("* 3 - Hint will provided to guess \n")



def guess_game(n):
    c = random.randint(1, 10)  # computer will generate only number from 1 to 10

    i = 0
    guess = 0  # initial guess
    score = 5  # initial score

    while i != c:
        i = int(input(f"input number between 1 to {n}:  "))  # input will be taken from user
        guess = guess+1
        score = score-1

        m=1
        while m!= c:
            if c*m%3 == 0:
                print("Hint- number is divisible by 3")
                break

            elif c*m%4 == 0:
                print("Hint- number is divisible by 4")
                break

            elif c*m%5 == 0:
                print("Hint- number is divisible by 5")
                break

        else :
            if(c % 2) == 0:
                print("Hint - Number is Even")

            elif (c % 2) != 0:
                print("Hint - Number is Odd")
                continue

        if i > c:
            print(f"number is lower , you tried {guess} times and score is:- {score} .")

        elif i < c:
            print(f"number is high, you tried {guess} times and score is:- {score} .")

    print(f"your guess is correct and your score is this:- {score+1} .")




guess_game(10)