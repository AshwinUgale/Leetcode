class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP=0
        l=0
        for r in range(1,len(prices)):
            mP=max(mP,prices[r]-prices[l])
            if prices[r]<prices[l]:
                l=r
        return mP
