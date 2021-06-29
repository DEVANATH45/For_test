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

# s = raw_input().strip()
# k = int(raw_input())
# i = 0
# while i < len(s):
#     a = s[i:i+k]
#     output = ""
#     for x in a:
#         if x not in output:
#             output += x
#     print output
#     i += k

if __name__ == '__main__':
    # string, k = input(), int(input())
    merge_the_tools('AABCAAADA', 3)