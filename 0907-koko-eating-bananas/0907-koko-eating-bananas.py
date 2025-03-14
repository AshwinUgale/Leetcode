class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        minS=r
        while l <= r:
            t=0
            m = (l+r)//2
            for i in range(len(piles)):
                t+= math.ceil(piles[i]/m)
            if t <= h :
                minS=min(minS,m)
                r = m -1
            elif t > h:
                l = m + 1
           
        return minS
