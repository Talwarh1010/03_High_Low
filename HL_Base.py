import math
import random
# Displays instructions
def instructions():
    print("""How to play Higher Lower game
    Enter a low and high number
    The computer will randomly choose a secret_number number between your user_guess numbers
    Enter the number of rounds you want to play
    The computer will choose the amount of guesses_taken you are allowed
    Guess the secret_number number
    Good Luck!""")


# Checks users enter an integer between a low and high number
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"
    while True:
        try:
            response = int(input(question))
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}")
                    continue

            elif situation == "low only":
                if response <= low:
                    print(f'Please enter an integer more than {low}')
                    continue
            return response
        except ValueError:
            print("Please enter an integer")
            continue


# Adds decoration to key statements
def statement_generator(statement, character):
    sides = character * 3
    statement = "{} {} {}". format(sides, statement, sides)
    top_bottom = len(statement) * character
    
    print(f"{top_bottom}")
    print(f'{statement}')
    print(f"{top_bottom}")
    return ""

# checks user enters yes / no to a given question
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "y" or response == "yes":
            return response

        elif response == "no" or response == "n":
            instructions()
            return response
        else:
            print("Please choose yes / no ")


# Main routine
statement_generator("Welcome to High Low game", "*")

# Asks the user if they have played the game before and displays instructions
yes_no("Have you played the game before? Yes / No  ")

# Looping component
play_again = ""
while play_again == "":
    while play_again == "":
        win = 0
        loss = 0
        pure_win = 0
        rounds_played = 0
        guesses_list = []
        # Asks the user for a minimum and maximum value
        print()
        minimum = int_check("Pick a minimum value: ", low=0)
        print()
        maximum = int_check("Pick a maximum value: ", low=minimum)

        # Calculates the max number of guesses_taken as well as the secret_number number
        var_range = int(maximum) - int(minimum) + 1
        max_raw = math.log2(var_range)
        max_upped = math.ceil(max_raw)
        max_guesses = max_upped + 1
        print(f"Max guesses: {max_guesses}")
        print()
        
        # Asks user for number of rounds
        rounds_wanted = int_check("How many rounds would you like to play: ", low = 0)
        break

    while rounds_played < rounds_wanted:
        rounds_played += 1
        
        # Displays round number and generates secret_number number
        statement_generator(f"The #{rounds_played} round has begun", character="")
        used_list = []
        guesses_taken = 0
        secret_number = random.randint(int(minimum), int(maximum))

        while guesses_taken < max_guesses:
            user_guess = int_check(f"Guess the secret number number:", low=minimum, high=maximum)

            # Checks if user input has been user_guess before
            if user_guess in used_list:
                print("You have already used this letter")
                continue

            used_list.append(user_guess)
            guesses_taken += 1
            
            # if user runs out of guesses_taken
            if guesses_taken == max_guesses and user_guess != secret_number:
                print()
                statement_generator("Sorry, you ran out of guesses_taken", character = "!")
                print(f"The number was {secret_number}")
                guesses_list.append(guesses_taken)
                loss +=1 
                break

            elif user_guess > secret_number:
                print("Too high")

            elif user_guess < secret_number:
                print("Too low")

            # When user guesses_taken the secret_number number
            elif user_guess == secret_number and guesses_taken != 1:
                print()
                statement_generator("Congratulations, you guessed the number", "^")
                secret_number = random.randint(int(minimum), int(maximum))
                guesses_list.append(guesses_taken)
                win += 1
                break
            
            else:
                statement_generator("Congratulations, you guessed the secret number in your first try", "!")
                secret_number = random.randint(int(minimum), int(maximum))
                guesses_list.append(guesses_taken)
                pure_win += 1
                break
    best_score = max(guesses_list)
    worst_score = min(guesses_list)
    average_score = math.ceil(sum(guesses_list) / len(guesses_list))

    # Displays results
    print(f"""      Statistics
                        Wins : {win}
                        Loss: {loss}
                        Gold wins: {pure_win}
                        
                        
                        Best score: {worst_score} guesses
                        Worst score: {best_score} guesses
                        Average score: {average_score} guesses""")
    print()
    play_again = input("Press enter to play again or any key than enter to quit")
print()
statement_generator("Thank you for playing High Low game", character = "♡")