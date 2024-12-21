class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        mp=0
        while r<len(prices):
            if prices[r]-prices[l]>mp:
                mp=prices[r]-prices[l]
            if prices[l]>prices[r]:
                l=r
            r+=1
        return mp      