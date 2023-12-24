class Solution:
    def isValid(self, s):
        stack = []

        for i in s:
            if i in "{([":
                stack.append(i)

            elif i == "}":
                if not stack and stack[-1] == "{":
                    stack.pop()

            elif i == ")":
                if not stack and stack[-1] == "(":
                    stack.pop()
            
            elif i == "]":
                if not stack and stack[-1] == "[":
                    stack.pop()

        if stack:
            return "false"
        else:
            return "True"


S = Solution()
s = "()"
print(S.isValid(s))