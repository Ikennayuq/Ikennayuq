#Task 7 b - Race
average_cycles = 0
total_number_cycles = 0 
name = input("What is your name?")
target_month_cycles = 0
for i in range(0,4):
    average_miles = input("What is your target average miles cycled?")
    target_month_cycles = target_month_cycles + average_miles
    print("What isthe number of cycles this week?")
    number_cylces = float(input())
    total_number_cycles = total_number_cycles + number_cylces    
average_cylces = total_number_cycles / 2    
print(name, "You have averaged", average_cycles,"miles per week")
if average_cycles >= target_month_cycles
    print("Congratulations, you have met your target")
else:
    print("Sorry you have not met your target")


