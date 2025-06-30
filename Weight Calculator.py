print(""" Weight Calculator. """)

user_weight = int(input("Kindly, put in your weight "))
unit = input("Kilograms (Kg) or Pounds (Lbs)")
if unit.upper() == "KG":
    total_weight = float(user_weight) * 2.204623
    print(f" Your weight is {total_weight}lbs")
elif unit.upper() == "LBS":
    total_weight = float (user_weight) * 0.4535924
    print(f"Your weight is {total_weight}kg")
else:
    print(f"Invalid unit! Please, input a valid unit")