class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #O(n)
        changePass= [0] * 1001
        for t in trips:
            numpass,s,e=t
            changePass[s]+=numpass
            changePass[e]-=numpass
        curPass=0
        for i in range(1001):
            curPass+=changePass[i]
            if curPass>capacity:
                return False
        return True

        
        
        #O(nlogn)
        # trips.sort(key = lambda t:t[1])
        # minHeap = []
        # curPass = 0
        # for t in trips:
        #     numPass,start,end = t
        #     while minHeap and minHeap[0][0] <= start:
        #         curPass-=minHeap[0][1]
        #         heapq.heappop(minHeap)
        #     curPass+=numPass
        #     if curPass > capacity:
        #         return False
        #     heapq.heappush(minHeap,[end,curPass])
        # return True
       