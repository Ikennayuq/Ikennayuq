mark = int(input("What mark did you get in your recent exam?"))
if mark >= 90:
    print("You got a A")
if mark >= 70 and mark < 90:
    print("You got a B")
if mark >= 50 and mark < 70:
    print("You got a C")
elif mark >= 40 and mark < 50:
    print("Yo got a D")
else:
    print("You failed")