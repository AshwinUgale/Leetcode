class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP=0
        l=0
        for r in range(1,len(prices)):
            if prices[r]-prices[l]>0:
                mP+=prices[r]-prices[l]
            l=r
        return mP