#Cafe project

#list of menu items 
menu = ["brioche", "bagel", "croissant", "apple pie", "carrot cake"]
#dictionary for stock levels
stock = {"brioche":20, "bagel":15, "croissant":25, "apple pie":10, "carrot cake":7}
#dictionary for prices 
price = {"brioche":3, "bagel":2, "croissant":3, "apple pie":4, "carrot cake":5}

#total stock worth
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

print(f"The total stock worth in the cafe is: £{total_stock_worth}")