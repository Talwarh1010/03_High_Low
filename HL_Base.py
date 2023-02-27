import random
import math


def instructions():
    print("""How to play Higher Lower game
    Enter a low and high number
    The computer will randomly choose a secret number between your chosen numbers
    Enter the number of rounds you want to play
    The computer will choose the amount of guesses you are allowed
    Guess the secret number
    Good Luck!""")
    
        
def num_check(question, low, high):
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return int(response)
            else:
                print(f"Please choose a number less than {str(low)} and more than {str(high)}")

        except ValueError:
            print("Please input a number")
            
def statement_generator(statement, character):
    top_bottom = len(statement) * character
    sides = character * 3
    final_greeting = f'{statement}'
    print(f"{sides}{top_bottom}{sides}")
    print(f'{sides}{final_greeting}{sides}')
    print(f"{sides}{top_bottom}{sides}")

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

def min_max_rounds_check(question):
    while True:
        response = input(question)
        if response.isdigit() == True and int(response)> 0: 
            return int(response)
        else:
            print("Please input an integer more than 0")
# Main routine
statement_generator("Welcome to High Low game", "*")

yes_no("Have you played the game before? Yes / No  ")

play_again = ""
while play_again == "":
    rounds_played = 1
    guesses = 0
    used_list = []
    minimum = min_max_rounds_check("Pick a minimum value: ")
    maximum = min_max_rounds_check("Pick a maximum value: ")
    if int(maximum) < int(minimum):
        print("Please enter a minimum value bigger than the maximum value")
        continue
    secret = random.randint(int(minimum), int(maximum))
    range = int(maximum) - int(minimum) + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print(f"Max guesses: {max_guesses}")
    print()
    rounds_play = min_max_rounds_check("How many rounds would you like to play: ")
    if rounds_play == "":
        print(f"Continuous mode: # {str(rounds_played)}")
        
    else:
        print(f"Round: #{str(rounds_played)} out of #{str(rounds_play)}")
    break
    
while guesses != max_guesses:
        
    chosen = num_check(f"Guess the secret number:", low = minimum, high = maximum)
        
    if chosen in used_list:
            print("You have already used this letter")
            continue
        
    used_list.append(chosen)
    guesses += 1
    rounds_played += 1
    if guesses == max_guesses:
        print("Sorry, you ran out of guesses")
        print(f"The number was {secret}")
        break
    elif chosen > secret:
        print("Too high")
    
    elif chosen < secret:
        print("Too low")
    
    elif chosen == secret: 
        statement_generator("Congratulations, you guessed the number", "^")
        break
    
show_stats = input("Press <enter> to see the statistics of the rounds")
if show_stats == "":
    print()
play_again = input("Thank you for playing, would you like to play again? <enter> to play again?")



