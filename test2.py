#balance ques

def ans(number):
    if number == 1000 or number == 0:
        return 0
    else:
        return number
t = int(input())
arr = []
while t > 0:

    num = int(input())
    num = num % 1000
    arr.append(ans(abs(num - 1000)))
    t-=1
for i in arr:
    print(i)