class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #Top down memoization 
        
        # coins.sort()
        # memo = {0:0}

        # def minCoin(amt):
        #     if amt in memo:
        #         return memo[amt]
        #     cur = float('inf')
        #     for c in coins:
        #         diff = amt - c
        #         if diff < 0:
        #             break
        #         cur = min(cur,1+minCoin(diff))
        #     memo[amt]= cur
        #     return cur
        # result = minCoin(amount)
        # if result < float('inf'):
        #     return result
        # else:
        #     return -1


        #Bottom Up
        coins.sort()
        dp=[0]*(amount+1)
        for i in range(1,amount+1):
            cur = float('inf')
            for c in coins:
                diff = i - c
                if diff < 0:
                    break
                cur = min(cur,dp[diff]+1)
            dp[i]=cur
        
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1