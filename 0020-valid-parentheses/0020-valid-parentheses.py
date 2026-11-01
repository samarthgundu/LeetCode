class Solution(object):
    def isValid(self, s):
        stack = []
        top = -1

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
                top += 1

            else:
                if top != -1 and (
                    (stack[top] == "(" and i == ")") or
                    (stack[top] == "{" and i == "}") or
                    (stack[top] == "[" and i == "]")
                ):
                    stack.pop()
                    top -= 1
                else:
                    return False

        return top == -1