#PGR107
#Kandidatnr: 100
#Question 1

import random

textFile = open("Words.txt", "r")



words = textFile.readlines()
cleaned_words = [word.strip() for word in words]
secret_word = random.choice(cleaned_words)


numberOfGuesses = len(secret_word)
display_word = ["_"] * len(secret_word)


attempts = 0
max_attempts = len(secret_word)

print(f"The word you need to guess has {len(secret_word)} characters.")
print(f"You have now {len(secret_word)} guesses.")
print(' '.join(display_word))


while attempts < max_attempts:
    guess = input('Guess a character: ').lower()
    
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i]==guess:
                display_word[i] = guess
                print(' '.join(display_word))
                print(f"You have {numberOfGuesses} guess(es) left.")
    else:
            attempts+=1
            numberOfGuesses-=1
            print("Sorry. That letter is not in the word.")
            print(f"You have {len(secret_word) - attempts} guess(es) left.")
            
    
    if '_' not in display_word:
            print('Congratulations! You guessed the word: ', secret_word)
            break
 

if attempts == max_attempts:
    print('You lost. The word was: ' + secret_word)





textFile.close()


