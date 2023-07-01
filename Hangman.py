import hangman_words 
import hangman_art
import random

word_list = hangman_words.word_list
Word = random.choice(word_list)
Word_length = len(Word)
print(hangman_art.logo)
display = []
for _ in range(Word_length):
    display += "_"
print(display)

stages = hangman_art.stages

Lives = 6
end_game = False

while not end_game:
    guess = input("Guess a letter").lower()
    for pos in range(Word_length):
        letter = Word[pos]
        if letter == guess:
            display[pos] = letter
    if guess in display:
        print(f"You\'ve already guessed {guess}.")
    if guess not in Word:
        print(f"{guess} in not in this word.")
        Lives -= 1
    
    print(stages[Lives])
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_game = True
        print("You Win")
    elif Lives == 0:
        end_game = True
        print("GAME OVER")