swimming = int(input("How many minuted did it take you to complete swimming? "))
cycling = int(input("How many minutes did it take you to complete cycling? "))
running = int(input("How many minutes did it take you to complete running? "))

total_time = int(swimming + cycling + running)
print("Your total time was: " + str(total_time))

if total_time <= 100:
    print("You've won the Provincial Colours!")
if total_time >100 and total_time <= 105:
    print("You've won the Provincial Half Colours!")
if total_time >=106 and total_time <=110:
    print("You've won the Provincial Scroll!")
if total_time >=111:
    print("Sorry, no award.")