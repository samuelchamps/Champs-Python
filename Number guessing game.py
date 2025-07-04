print("Number guessing game.")
right_number = 7
attempts = 0
maximum = 5

while attempts < maximum:
    user_input = int(input("Enter a number: "))
    if user_input == right_number:
        print("You guessed right.")
        break
    else:
        print("Try again")
        attempts = attempts + 1
if attempts == maximum:
    print(f"You have reached your maximum guesses.")