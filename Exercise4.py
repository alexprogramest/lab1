capacity = int(input("capacity of the bag: "))
barAmount = int(input("enter amount of bars: "))
all_bars = []  # all our gold bars

# inputting of bars values
for i in range(barAmount):
    repeat_input = True
    while repeat_input:
        bar_value = int(input("weight of {0} bar 'till {1}: ".format(i + 1, capacity)))
        if 0 < bar_value < capacity:
            all_bars.append(bar_value)
            repeat_input = False
        else:
            print("Out of bounds! Type again!")
print("All our bars: ", all_bars)

counted_weight = [False] * (capacity + 1)  # the weight, which we count and finally find the maximum (BY INDEXES!!!)
counted_weight[0] = True  # we start from zero-mass, which can be collected 0 bars

usedBars = [[]] * (capacity + 1)  # counting of necessary bars for the results
for i in range(len(all_bars)):
    for k in range(capacity, all_bars[i] - 1, -1):
        if counted_weight[k - all_bars[i]]:
            counted_weight[k] = True
            if usedBars[k] != [] and usedBars[k][-1] != all_bars[i] or usedBars[k] == []:
                usedBars[k].append(all_bars[i])

count = capacity
while counted_weight[count] == 0:
    count -= 1

print("The maximum weight = ", count)  # the maximum of weight of bars
print("Used bars fo this (their weights)",
      usedBars[count].sorted())  # the necessary bars, used for maximum (their weights)
