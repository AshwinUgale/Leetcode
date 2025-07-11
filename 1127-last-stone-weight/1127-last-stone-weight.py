class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxh=[]
        for s in stones:
            heapq.heappush(maxh,-s)
        while len(maxh)>1:
            f=heapq.heappop(maxh)
            s=heapq.heappop(maxh)
            if f!=s:
                heapq.heappush(maxh,f-s)
        if len(maxh)==0:
            return 0 
        else:
            return -maxh[0]