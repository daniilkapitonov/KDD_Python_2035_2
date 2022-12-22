import random

mass = [[1,2,3],[4,5,6],[7,8,9]]
# print(mass[1][0])
for i in range(3):
    for j in range(3):
        mass[i][j] = random.randint(0,100)
        print(mass[i][j], end = " ")
    print()
print(random.randint(-100,100))
print(random.randrange(-100,100,2))
print(random.random())
print(random.triangular(-100,100))