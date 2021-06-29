#reversing number

num = int(input())

revno = 0
count = 0
while num > 0:
    rem = num % 10
    revno = (revno*10) + rem
    num = num // 10
    # if (revno == 0):
    #     count += 1

print(revno)