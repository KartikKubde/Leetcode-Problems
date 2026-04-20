class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue

            if s[i] == stack[-1]:
                stack.pop()
                continue

            stack.append(s[i])

        return "".join(stack)
