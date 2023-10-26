import random
import os
from art import logo


def guess_number():
    play_again = input("Do you want to play Guess The Number? Type 'y' or 'n': ")
    if play_again.lower() == 'y':
        os.system("clear")
        print(logo)
        random_number = random.randint(0, 100)
        difficulty = input("Choose your difficulty, Type 'easy' or 'hard': ")
        if difficulty.lower() == 'easy':
            attempts = 10
        elif difficulty.lower() == 'hard':
            attempts = 5
            
        while attempts > 0:
            guess = int(input("Make a guess: "))
            if guess < random_number:
                print(" Too low. Guess again.")
                attempts -= 1
                if attempts == 0:
                    print("You run out of attempts. You lose.")
                    print(f"The number was {random_number}")
                    guess_number()
                    return None
                else:
                    continue
            elif guess > random_number:
                print(" Too high. Guess again.")
                attempts -= 1
                if attempts == 0:
                    print("You run out of attempts. You lose.")
                    print(f"The number was {random_number}")
                    guess_number()
                    return None
                else:
                    continue
            else:
                print(f"Congrats, you got it. The answer was {random_number}.")
                guess_number()
                return None
    else:
        return None
    
    
guess_number()
