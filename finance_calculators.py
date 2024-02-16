def main():
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")
    print("Enter either 'investment' or 'bond' from the meny above to proceed.")

    while True:
        choice = input().lower()

        if choice == "investment":
            deposit = float(input("Enter the amount of money you are depositing: "))
            interest_rate = float(input("Enter the interest rate as a percentage (eg. 7 for 7%)")) / 100
            years = int(input("Enter the number of years you plan on investing: "))
            interest_type = input("Choose interest type 'simple' or 'compound': ").lower()

            if interest_type == "simple":
                total_amount = deposit * (1 + interest_rate * years)
                print("You selected simple interest. Your total amount after the given time period will be: ", total_amount)
            elif interest_type == "compound":
                total_amount == deposit * (1 + interest_rate) ** years
                print("You have selected compound interest. Your total amount after the given time period will be: ", total_amount)
            else:
                print("Invalid interest type. Please either 'simple' or 'compound'.")

        elif choice == "bond":
            house_value = float(input("Enter the present value of the house: "))
            interest_rate = float(input("Enter the interest rate (eg 7 for 7%): "))
            months = int(input("Enter the number of months you need to repay the bond: "))

            monthly_interest = interest_rate / 12
            monthly_payment = (monthly_interest * house_value) / (1-(1+ monthly_interest) ** (-months))

            print("Monthly bond payment: ", {monthly_payment})

        else:
            print("Invalid input. Please select either 'investment' or 'bond'.")

if __name__== "__main__":
    main()