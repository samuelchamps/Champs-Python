print("Fill-in the blank lyrics!")
statement = print("Never going to _____ you up")
right_answer = "give"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    fill_in_the_blank = input(" ").lower()
    if fill_in_the_blank == "give":
        print(f"Well done, it only took you {attempts + 1} !")
        break
    else:
        print("Nope, try again.")
        attempts = attempts + 1
if attempts == max_attempts:
    print(f"You don't know my favorite line.")