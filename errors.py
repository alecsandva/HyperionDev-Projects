# Error Handling


# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
# Comments with single hash (#) were preexistent, double hash (##) I have added.

## Syntax error, print should be followed by ().
## Syntax error in following line, wrong indentation, missing ().
print("Welcome to the error program")
print("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result
## Syntax error, incorrect indentation for next 5 lines of code, aligned all of them.
## Syntax error, comparison operator instead of assignment operator in age_Str.
## Runtime error in str to int conversion, invalid input, I have removed 'years old'.
## Runtime error, cannot concatenate strings and integers, I converted to f-string instead.
age_Str = "24" 
age = int(age_Str) 
print(f"I'm  {age}  years old.")

    # Variables declaring additional years and printing the total years of age
## Runtime error, one variable is str the other is int, I converted to int.
years_from_now = int("3")
total_years = age + years_from_now

## Syntax error, missing () again
## Logical error, program runs but 'answer_years' is an undefined variable, replaced with total_years, convert to f-string.
print(f"The total number of years: {total_years}")

# Variable to calculate the total amount of months from the total amount of years and printing the result.
## Syntax error, missing ().
## Runtime error, undefined variable, made it 'total_years' to match, however (go to last error).
## Runtime error, incorrect concatenation again, converted to f-string.
## Logical error, the program runs but it is not the desired output.
## I have manually added 6 months.
total_months = total_years * 12
total_months += 6
print(f"In 3 years and 6 months, I'll be  {total_months}  months old")

#HINT, 330 months is the correct answer