# Task 7 -  Concert cost
total_cost = 0
concert = 1
for cost in range(0,5):
    print("what was the cost of Your concert number", concert,)
    cost = float(input())
    total_cost = total_cost + cost
    concert = concert + 1
if total_cost > 500: 
    print("You have qualified for a free ticket to a concert of your choice")
else:
    quit()
        