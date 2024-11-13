import random

def guessing_game():
    # Random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    guess = None

    print("Are you bored?.....let us have some fun")
    
    print("I'm thinking of a number between 1 and 100. Can we think in the same lane?")

    # Loop until the user guesses the number
    
    while guess != secret_number:
        
        guess = int(input("Enter your guess: "))
        

        if guess < secret_number:
            
            print("Too low! Try again.")
            
        elif guess > secret_number:
            
            print("Too high! Try again.")
            
        else:
            
            print("Congratulations! You've guessed the number!")
            

# Call the function to start the game

guessing_game()
