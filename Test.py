import random



def num_check(question, minimum, maximum):
    while True:
        try:
            response = input(question)
            if minimum <= int(response) <= maximum:
                return response
            else:
                print(f"Please choose a number less than {maximum} and more than {minimum}")

        except ValueError:
            print("Please input a number")


def computer_choice():
    minimum = num_check("Pick a minimum value? ")
    maximum = num_check("Pick a maximum value? ")
    choice = random.randint(minimum, maximum)
    print(choice)


print()
guesses = 0
rounds = int(input("How many rounds do you want to play"))
rounds_played = 0
while True:
    rounds_played += 1
    print(f" Round: #{rounds_played} out of {rounds}")
    user_choice = num_check(f"Choose a number between {minimum} and {maximum}:")
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
    elif rounds == rounds_played:
        break

    
print('Thanks for playing')
