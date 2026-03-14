class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        n = len(s)

        for i in range(n):
            count[s[i]] += 1
        
        for i in range(n):
            if(count[s[i]] == 1):
                return i
        
        return -1

        
