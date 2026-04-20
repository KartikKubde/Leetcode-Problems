class Solution:
    def makeGood(self, s: str) -> str:
      st = []
      st.append(s[0])

      for i in range(1,len(s)):
        if st and abs( ord(st[-1]) - ord(s[i]) ) == 32:
            st.pop()
        else:
            st.append(s[i])

      return "".join(st)
