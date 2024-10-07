# test score
test_score = int(input("What did you get in yor test score out of 70?"))
perc = (test_score / 100) * test_score
if perc > 70:
    print("Congratulations! You have passed")
else:
    print("you did not pass your test")

