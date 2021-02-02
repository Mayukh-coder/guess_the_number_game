import random
import time
print('''
######## Welcome to the "Guess the number" Game ########
    This is a game where the computer guesses a word and you have to guess the number.
    Please choose an option
        1. Enter the game (Enter '1')
        2. Close the game (Enter '2')
        3. Check the highscore(the least guesses) (Enter '3')
''')
while(True):
    startOption=input("What is you option? ")
    if startOption=='2':
        exit()
    elif startOption=='1':
        break
    elif startOption=='3':
        with open("highscore.txt") as f:
            highscore=int(f.read())
        if highscore==0 :
            print("You haven't played the game yet")
        else:
            print(f"The number has been guessed in just {highscore} guesses. Try to break it")
    else:
        print("Please eneter a valid option")

guesses=1
randomInteger=random.randint(1,101)
print("I have picked a number between 1 to 100. Try to guess the number in minimum guesses")
while(True):
    userEnteredNumber=int(input("Enter you guess: "))
    if userEnteredNumber==randomInteger :
        print(f"Yaayy!! You won! You have won the game in {guesses} guesses. Congratulations.")
        print("Let me check the highscores ...")
        time.sleep(3)
        with open("highscore.txt") as f:
            highscore=int(f.read())
        if highscore==0 :
            print("Wohoo!! You have beaten the highscore")
            with open("highscore.txt",'w') as f:
                f.write(str(guesses))
        elif highscore > guesses:
            print("Wohoo!! You have beaten the highscore")
            with open("highscore.txt",'w') as f:
                f.write(str(guesses))
        else:
            print("Oops you missed in breaking the highscore")
        exit()
    else:
        print("Oops!! This is not the number.")
        if userEnteredNumber > randomInteger:
            print("The number is higher than what I picked. Try a lower value")
        else:
            print("The number is lower than what I picked. Try a higher value")
    guesses +=1
