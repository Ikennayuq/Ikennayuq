stadium_capacity = 0
number_entered = 0
more_supporters = "yes"
stadium_capacity = int(input("What is the stadium capacity?"))
while stadium_capacity < 1 or stadium_capacity > 3023:
    print("Error, that is not a valid stadium capacity")
    stadium_capacity = int(input("Enter a valid stadium capacity"))
remaining_capacity = 3023 - int(input())