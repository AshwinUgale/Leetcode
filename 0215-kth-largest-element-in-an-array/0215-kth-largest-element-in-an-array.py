class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #max heap
        # nums = [ -n for n in nums]
        # heapq.heapify(nums)
        # for i in range(k-1):
        #     heapq.heappop(nums)
        # return -nums[0]

        #min heap
        minHeap=[]
        for i in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap,i)
            else:
                heapq.heappushpop(minHeap,i)
        return minHeap[0]


