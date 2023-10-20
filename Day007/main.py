import random
import hangman_art
import hangman_words

print(hangman_art.logo1) 

random_word = random.choice(hangman_words.word_list)
len_random_word = len(random_word)
my_word = ['_'] * len_random_word
lives = 6
#print(random_word)
while True:    
    print(hangman_art.gallow_steps[lives])
    guess = input('Guess a letter: ').lower()
    if guess in my_word:
        print(f'You have already enter the letter "{guess}"')
    count = 0
    for i in range(len_random_word):        
        if random_word[i] == guess:
            my_word[i] = guess            
        else:
            count += 1    
    print(f"{' '.join(my_word)}")
    if '_' not in my_word:
        print(hangman_art.gallow_steps[lives])
        print('Victory!!!')
        break        
    if count == len_random_word:
        if guess not in my_word:
            print(f'Guess again, the letter "{guess}" is not in the word. You lose a life.' )
        lives -= 1
    if lives == 0:
        print(hangman_art.gallow_steps[lives])
        print('Game Over')
        break