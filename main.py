import random
print('''
######## Welcome to the "Guess the number" Game ########
    This is a game where the computer guesses a word and you have to guess the number.
    Please choose an option
        1. Enter the game (Enter '1')
        2. Close the game (Enter '2')
''')
while(True):
    startOption=input("What is you option? ")
    if startOption=='2':
        exit()
    elif startOption=='1':
        break
    else:
        print("Please eneter a valid option")

guesses=1
randomInteger=random.randint(1,101)
print("I have picked a number between 1 to 100. Try to guess the number in minimum guesses")
while(True):
    userEnteredNumber=int(input("Enter you guess: "))
    if userEnteredNumber==randomInteger :
        print(f"Yaayy!! You won! You have won the game in {guesses} guesses. Congratulations.")
        exit()
    else:
        print("Oops!! This is not the number.")
        if userEnteredNumber > randomInteger:
            print("The number is higher than what I picked. Try a lower value")
        else:
            print("The number is lower than what I picked. Try a higher value")
    guesses +=1
