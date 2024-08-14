import random

# List of words to choose from
words_list = ['apple', 'banana', 'cherry', 'date', 'elderberry','Rohit']

# Choose a random word
words_list = random.choice(words_list)


# Create a list to store the guessed letters
guessed = ['_'] * len(words_list)

# Set the limit for incorrect guesses
limit = 5

# Initialize the number of incorrect guesses
incorrect = 0

while True:
    # Show the current state of the word
    print(' '.join(guessed))
    
    # Ask the player for a guess
    guess = input("Guess a letter: ")
    
    # Check if the guess is in the word
    if guess in words_list:
        # Reveal the correct letters
        for i in range(len(words_list)):
            if words_list[i] == guess:
                guessed[i] = guess
    else:
        # Increment the number of incorrect guesses
        incorrect += 1
        
        # Check if the limit has been reached
        if incorrect == limit:
            print(f"Game over! The word was {words_list}.")
            break
    
    # Check if the word has been fully guessed
    if '_' not in guessed:
        print(' '.join(guessed))
        print("Congratulations, you won!")
        break




