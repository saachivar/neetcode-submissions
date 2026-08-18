class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        starting = ["[", "(", "{"]
        stack = []
        for char in s:
            if char in starting:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
        return len(stack) == 0

        