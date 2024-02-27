str_manip = input("Please enter your favourite quote: ")

#Calculate and display lenght of string
print(len(str_manip))

#Find the last letter and replace with "@"
last_letter = str_manip[-1]
str_replacement = str_manip.replace(last_letter, "@")
print(str_replacement)

#Print last 3 characters backwards
last_characters = str_manip[-3:]
reverse_characters = last_characters[::-1]
print(reverse_characters)

#Create 5 letter word from first 3 and last 2 characters
first_characters = str_manip[:3]
last_two_characters = str_manip[-2:]
concatenated_word = first_characters + last_two_characters
print(concatenated_word)