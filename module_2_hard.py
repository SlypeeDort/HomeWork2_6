import random
# stone_1 = random.randint(3,20)
stone_2 = []
stone_1 = int(input('Введите число '))

for i in range(1, stone_1):
    for j in range(1, stone_1):
        if stone_1 % (i + j) == 0 and i != j:
            stone_2.append((i, j))



for i in range(len(stone_2)):
    for j in range(len(stone_2)):
        if stone_2[i][0] == stone_2[j][1]:
            for k in range(len(stone_2)):
                if stone_2[i][1] == stone_2[k][0]:
                    stone_2[k] = 'None'

for i in stone_2.copy():
    if i == 'None':
        stone_2.remove(i)
print(stone_2)
