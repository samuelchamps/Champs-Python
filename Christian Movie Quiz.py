print("Christian Movie Quiz!")

movie = input("What is your favorite Christian movie? ")
if movie.lower() == "war room":
    print(f"Ah! A movie on prayer.")
    character = input("What character inspired you most? ")
    if character.lower() == "miss clara":
        print(f"She’s fire! A true prayer warrior.")
    else:
        print(f"Nice! That character was inspiring too.")

elif movie.lower() == "god's not dead":
    print(f"That movie makes a strong case for faith!")
    final_debate = input("Do you remember the final debate? ")
    if final_debate.lower() == "yes":
        print(f"Powerful moment, right?")
    else:
        print(f"You should definitely rewatch it!")
else:
    print(f"{movie} is a great choice! Thanks for sharing.")