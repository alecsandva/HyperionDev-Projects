# optional_challenge
# Create a program with two compilation errors, a runtime error and a logical error
# Comment and exmplain what the error is and why it occurs

# syntax errors: indentation, missing ':'
# runtime error: missing data 
# logical error: mistake in calculation

# This program is a cat grooming salon, calculating whether the patient should schedule an appointment

cat_name = str(input("Enter your cat's name: "))
    cat_age = int(input("Enter your cat's age: in years: (e.g. 0-1 for kitten, 2 and above for adult)"))   # syntax error, wrong indentation
last_appointment = int(input("Enter the number of months since last appointment: "))
### correction - has_fleas = input("Does the cat have fleas? (yes/no)")    # running error on line 30,31)

print("Hello" + " " + cat_name + " " + "and parents!")

if cat_age < 2: #kitten
    if last_appointment >= 6   # syntax error, missing ":"
        print("Bring your kitten in for a grooming!")
    else: 
        print("You can wait until 6 months from your last appointment.")

else: #adult
    if last_appointment > 3:   # logical error, >= should be used to print statement at the 3 months mark 
        print("Bring your cat in for a grooming!")
    else:
        print("Your cat can wait until 3 months from their last appointment")

if has_fleas.lower() == "yes":     # running error, missing data. need to add a variable to determine if cat has fleas in first few lines
    print("Time to see the vet!")