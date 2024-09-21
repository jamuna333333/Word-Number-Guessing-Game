

import random

print("WELCOME TO GUESSING GAME")
name=input("\nEnter your name: ")
print(f"\nHi {name}\nDo you want to play Number Guessing Game or Word Guessing Game?")
gametype=input(f"Enter 'Number' to play number guessing game\nEnter 'Word' to play guessing game: ")
def set_attempt(level):
    if (level_type.lower()=="hard"):
        return 10
    elif (level_type.lower()=="easy"):
        return 20
    else:
        return -1

    
def wordlist(level_type):
    if(level_type.lower()=="easy"):
        return ("Apple","House", "Chair", "Table", "Dog", "Cat", "Book", "Sun", "Car", "Tree", 
                           "Ball","Bird", "School", "Pen", "Cup", "Fish", "Hat", "Shirt", "Door", "Chair",
                           "Bed", "Hand", "Chair", "Moon", "Star", "Boat", "Milk", "Leaf", "Road", "Bike",
                           "Sky", "Rain", "Toy", "Desk", "Park", "Hand", "Sofa", "Shoes", "Hat", "Farm")
    elif(level_type.lower()=="hard"):
        return ("Adventure", "Harmony", "Journey", "Euphoria", "Mystical", "Oasis", "Quarantine", 
                          "Radiant", "Sanctuary", "Tranquil", "Universe", "Velvet", "Whimsical", "Retrospect",
                          "Yawn", "Zenith", "Eloquent", "Fabricate", "Gallant", "Hypothesis", "Ignition", 
                          "Jubilant", "Knowledge", "Luminous", "Melancholy", "Nebula", "Obstacle", "Pensive",
                          "Quixotic", "Resilient", "Serene", "Tranquil", "Unveil", "Vortex", "Wanderlust",
                           "Xenon", "Yield", "Zephyr", "Ambiguous", "Cascade")
    else:
        print("Invalid level of difficulty")
        exit



if(gametype.lower()=="number"):
    print("\nLet's play Number Guessing Game.....")
    print("For 'easy' level of difficulty you will have 20 attempts, and for 'hard' level of difficulty you will have 10 attempts")
    level_type=input("Enter 'Hard' for a hard level of difficulty or enter 'Easy' for easy level of difficulty: ")
    attempts=set_attempt(level_type)
    lower_limit=int(input("Enter a lower limit number: "))
    upper_limit=int(input("Enter a upper limit number: "))
    print("Let me decide a number.....")
    number=random.randint(lower_limit, upper_limit)
    



    def check_answer(guess, number, attempts):
        if(guess<number):
            print("Your guess is lower than the actual number")
        elif(guess>number):
            print("Your guess is higher than your number")
        else:
            print(f"You guess it right!!! Answer is {number}\nCongratulations {name}")
            
    guess=0
    if(attempts<=0):
        print("You have entered invalid level of difficulty")
    else:
        while(guess!=number):
            print(f"\nYou are left with {attempts} attempts")
            guess=int(input("Enter your guess :"))
            if(guess<lower_limit or guess>upper_limit):
                print("Your guess is not within the entered range. \nPlease enter a number that is within the entered limit")
            else:
                check_answer(guess, number, attempts)
            attempts-=1
            if(attempts==0):
                print(f"You have run out of attempts\nThe currect answer is {number}\nBetter luck next time")
                break
        

#word guessing game

    
elif(gametype.lower()=="word"):
    print("\nLet's play Word Guessing Game")
    print("For 'easy' level of difficulty you will have to guess simple words, and for 'hard' level of difficulty you will have to guess advanced words. \nYou will have 20 attempts ")
    entered_level=input("\nEnter 'Hard' for a hard level of difficulty or enter 'Easy' for easy level of difficulty: ")

    print("\nLet me think of a word.....")

    attempts=20
    words=wordlist(entered_level)


    if words:
        word=random.choice(words)
        answer=word
        jumble=""

        word_list=list(word)
        random.shuffle(word_list)
        jumble=''.join(word_list)
    
        print("\nLets start the game!!!!")
        print(f"You have {attempts} attempts left")
        print("For hint enter 'Hint'\nTo quit the game enter 'Quit' ")
        print("The jumbled word is ", jumble)
    
        while(attempts>0):
            attempts-=1
            guess=input("\nEnter your guess: ")
            if guess.lower()==answer.lower():
                print(f"You guess it right!!! The correct answer is {answer}\nCongratulations {name}")
                break
            elif (guess.lower()=="hint"):
                i=random.choice(range(len(jumble)))
                print(f"Hint: Position {i + 1} has the letter '{answer[i]}'")
            elif (guess.lower()=="quit"):
                print("Oops! You gave up\nBetter luck next time!")
                print(f"The word is {answer}")
                break
            else:
                if(len(answer)==len(guess)):
                    print("Wrong answer!\nTry again")
                else:
                    print(f"The {jumble} word has {len(jumble)} letters and not {len(guess)} letters")
                    print("Wrong answer!\nTry again")
                if(attempts==0):
                    print(f"You have run out of attempts\nThe currect answer is {answer}\nBetter Luck Next Time!!!")
                else:
                    continue

else:
    print("Your choice is invalid")

