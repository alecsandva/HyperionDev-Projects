#while loop exercise

total_numbers = 0
count_numbers = 0

while True:
    number = int(input("Enter a number (or -1 to stop): "))
    if number == -1:
       break
   
    total_numbers += number 
    count_numbers += 1

if count_numbers > 0:
    average_number = total_numbers / count_numbers
    print ("The average of the numbers is: ", average_number)
     

else: 
    print("No numbers entered.")


