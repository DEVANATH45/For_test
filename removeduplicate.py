def merge_the_tools(stringi, k):
    empt = ""
    for i in range(0,len(stringi),k):
        a = stringi[i:i+k]
        # print(a)
        for j in a:
            if j not in empt:
                empt += j
        print(empt)
        empt = ""

if __name__ == '__main__':
    # string, k = input(), int(input())
    merge_the_tools('AABCAAADA', 3)