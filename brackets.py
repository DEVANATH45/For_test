def sestack(text):
    stack = []

    lookup = {
        "}": "{",
        "]": "[",
        ")": "(",
        ">": "<"
    }
    
    for i in text:
        if i in lookup.values():
            stack.append(i)
            continue
        elif stack and lookup[i] == stack[-1]:
            stack.pop()
        else:
            return False
    if stack:
        return False
    else:
        return True


if sestack("[{}]"):
    print("\nExpression is valid")
else:
    print("\nExpression is invalid")


