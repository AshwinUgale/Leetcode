class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def minCoin(amt):
            if amt in memo:
                return memo[amt]
            cur = float('inf')
            for c in coins:
                diff = amt - c
                if diff < 0:
                    break
                cur = min(cur,1+minCoin(diff))
            memo[amt]= cur
            return cur
        result = minCoin(amount)
        if result < float('inf'):
            return result
        else:
            return -1