# problem link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# status: solved

# num = [2, 3, 6, 6, 5]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    num = list(arr)

    for j in range(len(num)):
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                temp = num[i + 1]
                num[i + 1] = num[i]
                num[i] = temp

    top = num[-1]
    num = [item for item in num if item != top]
    print(num[-1])

