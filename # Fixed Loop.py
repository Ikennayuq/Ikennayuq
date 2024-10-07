# Fixed Loop
total = 0
for i in range(0,3):
    print("Enter the cost of three of your favourite mobile phone apps")
    app_price = float(input())
    total = total + app_price
print("The total cost of the apps is: £",round(total,2))
# the round total on the end of the brackets is to indicate that it is to 2 decimal places
if total > 10:
    print("You have spent more than £10 and receive a free app")
else:
    quit()