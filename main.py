import random
print('''
######## Welcome to the "Guess the number" Game ########
''')
randomInteger=random.randint(1,101)
print("The computer has guessed a number. Try to guess the number in minimum guesses")
while(True):
    userEnteredNumber=int(input("Enter you guess: "))
    if userEnteredNumber==randomInteger :
        print("Yaayy!! You won!")
        exit()
    else:
        print("Oops This is not the number. Try again")