def check_parenthesis(parenthesis):
    stack = []
    for s in parenthesis:
        if s == "}" and len(stack) > 0 and stack[-1] == "{":
            stack.pop()
        elif s == "]" and len(stack) > 0 and stack[-1] == "[":
            stack.pop()
        elif s == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(s)

    return len(stack) == 0


paren = "()()(){()}{()}[][]"
print(check_parenthesis(paren))
