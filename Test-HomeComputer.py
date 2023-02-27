import random
from re import L
def instructions():
    print("""Instructions:
          Pick a lower limit and a higher limit
          The computer will randomly choose a secret number bewteen your chosen limits
          You choose the amount of rounds you would like to play
          The computer will choose the amount of guess you will have
          Your goal is to guess the secret number before you run out of guesses
          good luck
          
          """)
minimum = int(input("Pick a minimum value? "))
maximum = int(input("Pick a maximum value? "))
def rounds_check(question):
    while True:
        answer = input(question)
        if answer.isnumeric() == False or answer == "" :
            return answer
        else:
            print("Please input the amount of rounds you would like to play")

def num_check(question):
    while True:
        try:
            response = input(question)
            if minimum <= int(response) <= maximum:
                return int(response)
            else:
                print(f"Please choose a number less than {maximum} and more than {minimum}")

        except ValueError:
            print("Please input a number")
            
used_numbers = []
yes_no = ["yes", "y", "no", "n"]
show_instructions = input("Have you played the game before").lower()
if show_instructions in yes_no and show_instructions ==  yes_no[2] or yes_no[3]:
    instructions()
elif show_instructions not in yes_no:
    print("Please choose yes or no")
choice = random.randint(minimum, maximum)
print(choice)
print()
guesses = 0
rounds = rounds_check("How many rounds would you like to play? ")
rounds_played = 0
while True:
    rounds_played += 1
    print(f" Round: #{rounds_played} out of {rounds}")
    user_choice = num_check(f"Choose a number between {minimum} and {maximum}:")
    if user_choice in used_numbers:
        print("You have already chose that number")
        
    used_numbers.append(user_choice)
    
    guesses += 1
    if int(user_choice) > choice:
        print("Too high")
    elif int(user_choice) < choice:
        print("Too low")
    elif guesses == 5:
        print("You ran out of guesses")
        print(f"The number was {choice}")
        break
    elif int(user_choice) == choice:
        print("You guessed the number")
        break
    
print('Thanks for playing')
