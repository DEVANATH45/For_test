def revno(num):
    arr = []

    while num > 0:
        rem = num % 10

        num = num // 10
        arr.append(rem)
    # print(arr)
    return max(arr)


n = int(input())
count = 0
while n > 0:
    l = revno(n)
    n = n - l
    count += 1
    # print(n)
print(count)










