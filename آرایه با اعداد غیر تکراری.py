import random
numbers = []
def getUniqueRandom(start, end):
    while True:
        i = random.randrange(start, end)
        if i not in numbers:
            return i
for n in range(10):
    i = getUniqueRandom(1, 60)
    numbers.append(i)