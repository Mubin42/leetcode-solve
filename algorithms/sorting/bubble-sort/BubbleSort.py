num = [-74, 0, -44, 100, 9]

for j in range(len(num)):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            temp = num[i + 1]
            num[i + 1] = num[i]
            num[i] = temp

print(num)
