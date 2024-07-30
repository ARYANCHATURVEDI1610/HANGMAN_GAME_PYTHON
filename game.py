import random

# List of words to choose from
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer', 'algorithm']

def choose_word():
    return random.choice(word_list)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
           -
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / 
           -
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |    
           -
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    
           |    
           -
        """,
        """
           ------
           |    |
           |    O
           |   \\|
           |    
           |    
           -
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
           -
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |    
           -
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |    
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    correct_guesses = set()
    tries = 7

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print("Word to guess: " + "_ " * len(word))

    while len(word_letters) > 0 and tries > 0:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word_letters:
            word_letters.remove(guess)
            correct_guesses.add(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            tries -= 1
            print(f"Wrong guess! {guess} is not in the word.")
        
        guessed_letters.add(guess)
        current_word = [letter if letter in correct_guesses else '_' for letter in word]
        print(display_hangman(tries))
        print("Current word: " + ' '.join(current_word))
        print("Guessed letters: " + ', '.join(sorted(guessed_letters)))

    if tries == 0:
        print(f"Game over! The word was '{word}'. Better luck next time!")
    else:
        print(f"Congratulations! You guessed the word '{word}' correctly!")

if __name__ == "__main__":
    play_hangman()
