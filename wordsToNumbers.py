alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = {"O":"0",
           "I":"1",
           "L":"1",
           "Z":"2",
           "E":"3",
           "A":"4",
           "H":"4",
           "S":"5",
           "G":"6",
           "T":"7",
           "B":"8",
           "Q":"9"}

print(numbers["Q"])


user_input = input("Enter a string: ")

user_output = ""

user_capitalised = ""



if user_input in numbers:
    print("yes")
for x in range(len(user_input)):

    user_capitalised += user_input[x].upper()

    
    
    if user_capitalised[-1] in numbers:
        user_output += numbers[user_capitalised[-1]]
    else:
        user_output += user_capitalised[-1]


print(user_output)