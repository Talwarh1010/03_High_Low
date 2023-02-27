import math

for item in range(0,4):
    
    low = int(input('What is the minimum number? '))
    high = int(input("What is the maximum number? "))
    
    range = high - low + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print(f"Max guesses: {max_guesses}")
    print()