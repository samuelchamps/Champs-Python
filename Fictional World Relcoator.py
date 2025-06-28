### Based on user preferences, recommend a fictional world like:

"""* Star Wars
* Game of Thrones
* Marvel Universe
* Harry Potter
* The Matrix"""

### 🧩 **Algorithm:**

### **Start the program**
print("Welcome to the Fictional World Relocator!")###Display a welcome message:
    # *“Welcome to the Fictional World Relocator!”

print()

print("Kindly, use Y for Yes and N for No")

print()

first_question = input("Do you like space travel? ") # **Ask the user a series of preference questions** (using `input()`):
if first_question.lower() == "y":
    print("You will love Star Wars")
else:
    print("Alright, you can check others.")

second_question = input("Do you enjoy magic? ")
if second_question.lower() == "y":
    print("You are a fan of Harry Potter!")
else:
    print("Alright, you can check others.")

third_question = input("Do you like superheroes? ")
if third_question.lower() == "yes":
    print("Welcome to Marvel Universe")
else:
    print("Alright, you can check others.")

fourth_question = input("Are you okay with dragons and medieval settings? ")
if fourth_question.lower() == "y":
    print("That means you are a huge fan of Game of Thrones.")

else:
    print("Alright, you can check others.")

fifth_question = input("Do you like simulated/virtual reality ideas? ")
if fifth_question.lower() == "y":
    print("I think you will love The Matrix!")
else:
    print("Alright, you can check others.")
print()