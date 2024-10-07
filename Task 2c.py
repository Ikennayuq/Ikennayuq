full_price = float(input("What is the full price of the item you want to buy?"))
Discount = full_price * 0.2
Final_Price = full_price - Discount 
print("The price of the item with a discount of 20% is now", Final_Price)
saved = full_price - Discount
print("You saved", Discount, "!")