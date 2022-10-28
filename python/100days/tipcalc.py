# ------------------------------------
# From Angela Yu's "100 Days of Code"
# ------------------------------------

# Create a program to calculate a tip
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("How much was the bill? €"))
tip = int(input("What percent to give as tip? "))
tip = tip / 100 + 1
people = int(input("Split between how many people? "))

split_charge = round((bill / people) * tip,2)

final = "{:.2f}".format(split_charge)
print(f"Each person should pay €{final}")
