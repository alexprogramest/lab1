import random  # working with the random module

random.seed()

capacity = 100
weights = []  # in kilograms
count = range(random.randint(8, 11))

for i in count:
    weights.append(round(random.random() * 15 + 10, 2))
print(weights, " (weights of bars)")
weights.sort()
print(weights, " (sorted weights)")

while capacity > min(weights):
    capacity -= weights[0]
    print(weights[0])
    weights.remove(weights[0])
print("Maximum weight of gold that fits into a knapsack with capacity of W", 100 - capacity)
