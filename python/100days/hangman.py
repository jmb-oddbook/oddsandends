# Hangman
import random
from hangman_art import logo, stages

print(logo)

# Get a random word
word_list = open("suppl/test.txt", "r").read().splitlines()

chosen_word = random.choice(word_list).lower()
print(chosen_word)

# display an underscore for each letter in the chosen word
display = ["_"] * len(chosen_word)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # loop through positions in chosen_word, for each position that matches
    # guess, display that letter in its position
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    
    if guess not in chosen_word:
        print(f"Your guess {guess} is not in the chosen word.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
                
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
