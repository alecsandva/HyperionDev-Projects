# Replace the "!" with " " 

string_1 = "The!quick!brown!fox!jumps!over!the!lazy!dog."
new_string = string_1.replace("!", " ")
print(new_string)

# Print new string in upper case

upper_string = new_string.upper()
print(upper_string)

# Print strings in reverse

reverse_string_1 = new_string[::-1]
print(reverse_string_1)
reverse_string_2 = upper_string[::-1]
print(reverse_string_2)