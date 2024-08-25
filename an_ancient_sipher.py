import random
rock = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rand_rock = random.choice(rock)
result = []
print(rand_rock)
for i in range(1, 20):
    for j in range(1, 20):
        if rand_rock % (i + j) == 0 and i != j and i < j:
            result.append(i)
            result.append(j)
print(''.join(map(str, result)))
