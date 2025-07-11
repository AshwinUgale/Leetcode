class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxh=[]
        for n in nums:
            heapq.heappush(maxh,n)
            if len(maxh)>k:
                heapq.heappop(maxh)
        print(maxh)
        return maxh[0]