class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        st = []
        st.append(n-1)
        ans = [0]*n
        ans[n-1] = prices[n-1]

        for i in range(n-2,-1,-1):

            while(len(st) != 0 and prices[st[-1]] > prices[i]):
                st.pop()

            if(len(st) == 0):
                ans[i] = prices[i]
            else:
                ans[i] = prices[i] - prices[st[-1]]
            
            st.append(i)

        return ans