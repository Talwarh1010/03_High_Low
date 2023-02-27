secret  = 7
guesses_allowed = 5
already_guessed = []
guesses_left = guesses_allowed
num_won = 0
guess = ""

while guess != secret and guesses_left >= 1:
    guess = int(input("What is the number? "))
    
    if guess in already_guessed:
        print("You have already guessed that number")
        continue
    
    guesses_left -= 1
    already_guessed.append(guess)
    
    if guess > secret:
        print("Too high")
        
    elif guess < secret:
        print("Too low")
    
    else:
        finished = guesses_allowed - guesses_left
        print(f"Good work you guessed the number in {finished} guesses")