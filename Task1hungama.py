import random

# List of words for the game
words = ["apple", "banana", "cherry", "grape", "orange"]
word = random.choice(words)
guesses = ""
lives = 6
print("--- Hangman Game ---")
while lives > 0:
    failed = 0
    
    # Print the hidden word with blanks or letters
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            failed += 1
            
    # Check if you guessed all letters
    if failed == 0:
        print("\n🎉 You Win!")
        break

    # Get user guess from the terminal
    guess = input("\n\nGuess a letter: ").lower()
    guesses += guess

    # If the letter is wrong, lose a life
    if guess not in word:
        lives -= 1
        print(f"❌ Wrong! Lives left: {lives}")

# Out of lives
if lives == 0:
    print(f"\n💥 Game Over! The word was: {word}")