import random

N = int(input("Введите количество списков:"))
bigList = []
for i in range (1, N+1):
    n = random.randint(1, 10)
    smallList = [random.randint(1, 10) for smallList in range (0, n)]
    bigList.append(smallList)

print("Сформированные списки:")
print(bigList)

for i in range(N):
    count = 0
    max = -1
    for j in range(len(bigList[i])):
        count = bigList[i].count(bigList[i][j])
        if (max < count):
            max = count
    print("В списке " + str(i+1) + " находится " + str(max) + " одинаковых элементов.")
