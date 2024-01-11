import random
random_number=random.randint(0,15) # The randint function is using the given range (0-15) and generates a random number based on it.



user_guess=int(input("Guess the number between 1 and 15 ")) #The input function prompts the user to guess a number.

attempts = 1
max_attempts = 5


while attempts < max_attempts:# The while loop continues until the user will use all the five attempts.
    if user_guess < random_number:
        print(f"You answered {user_guess}. Your number is lower!") # If , elif and else statements check whether user's guess is lower, higher or equal to the random number.
        attempts += 1
        user_guess=int(input("New Guess the number: "))

    elif user_guess > random_number:
        print(f"You answered {user_guess}. Your number is higher!")
        attempts += 1
        user_guess=int(input("New Guess the number: "))

    else:
        print(f"You answered {user_guess}. You won !")
        break # Loop stops here.

