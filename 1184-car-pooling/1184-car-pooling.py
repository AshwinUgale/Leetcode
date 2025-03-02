class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # O(n) solution, for the case when we know the trip length as given in this question

        # passChange = [0] * 1001
        # for t in trips:
        #     numPass,start,end = t
        #     passChange[start] += numPass
        #     passChange[end] -= numPass
        # curPass=0
        # for i in range(1001):
        #     curPass += passChange[i]
        #     if curPass > capacity :
        #         return False
        # return True


        
        
        # O(nlogn) solution


        trips.sort(key = lambda t: t[1])

        minHeap = []
        curPass = 0
        for t in trips:
            numPass,start,end=t
            while minHeap and minHeap[0][0] <= start:
                curPass-=minHeap[0][1]
                heapq.heappop(minHeap)
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap,[end,numPass])
        return True