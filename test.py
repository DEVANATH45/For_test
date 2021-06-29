
#Nth term
t = int(input())
arr = []
for j in range(t):
    num = 0
    n = int(input())
    for i in range(1,n+1):
        num = num+i

    arr.append(num)
for i in arr:
    print(i)
