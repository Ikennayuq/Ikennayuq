# Lucky Prize Draw 
print("This is the lucky prize Draw")
prizes = []
names = []

for n in range(10):
    name = input("Enter 10 names")
    names.append(name)


for x in range(4):
    prize = input("Enter 4 prizes")
    prizes.append(prize)


import random
print(random.choice(names), "You won!")
print("Here is your chosen prize:", random.choice(prizes))





