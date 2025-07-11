class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minh=[]
        res=[]
        for x,y in points:
            dist=x**2+y**2
            heapq.heappush(minh,(-dist,[x,y]))
            if len(minh)>k:
                heapq.heappop(minh)
        for d,p in minh:
            res.append(p)
        return res