class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_index = [0]*26
        seen = set()

        for i in range(len(s)):                     # Here we are creating last_index array
            ch = s[i]
            last_index[ord(ch) - ord('a')] = i

        for i in range(len(s)):
            if s[i] not in seen:
                while(stack and ord(stack[-1]) > ord(s[i]) and i < last_index[ord(stack[-1]) - ord('a')]):
                    seen.remove(stack.pop())
                stack.append(s[i])
                seen.add(s[i])

        return "".join(stack)

Time Complexity = O(n)
Space complexity = O(n)       # as Stack ki complexity O(n) 
