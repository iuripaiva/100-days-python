import random as r

names_string = input("Write all the names separated by comma and space (e.g: Iuri, Larissa, Vinicius): ")
names = names_string.split(", ")

roulette = r.randint(0, len(names)-1)

print(f"{names[roulette]} is going to buy the meal today!")
