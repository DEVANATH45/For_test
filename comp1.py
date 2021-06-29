m = int(input())
arr = []
for i in range (m):
    a, b = map(int, input().split())
    arr.append((a, b))
for j in arr:
    temp = 0
    # print(j,end=" ")
    for k in j:
        print(k - temp)
        temp = k
