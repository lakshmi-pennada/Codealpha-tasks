import random

# Predefined list of 5 words
word_list = ["python", "coding", "program", "laptop", "display"]
secret_word = random.choice(word_list)

guessed_letters = []
incorrect_guesses = 0
max_lives = 6

print("--- Welcome to Hangman! ---")

while incorrect_guesses < max_lives:
    # Display the current state of the word (e.g., p _ t h _ n)
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord: " + display_word.strip())
    print(f"Remaining lives: {max_lives - incorrect_guesses}")
    
    # Check if player won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word!")
        break
        
    # Get user guess
    guess = input("Guess a letter: ").lower()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
        
    guessed_letters.append(guess)
    
    # Check if the guess is right or wrong
    if guess in secret_word:
        print("Good guess!")
    else:
        print("Incorrect guess!")
        incorrect_guesses += 1

else:
    print(f"\n Game Over! The word was: {secret_word}")