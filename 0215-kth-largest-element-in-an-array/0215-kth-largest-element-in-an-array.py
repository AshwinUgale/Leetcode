class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #max heap
        # for i in range(len(nums)):
        #     nums[i]=-nums[i]
        # heapq.heapify(nums)
        # for i in range(k-1):
        #     heapq.heappop(nums)
        # return - heapq.heappop(nums)

        minHeap=[]
        for num in nums:
            if len(minHeap)<k:
                heapq.heappush(minHeap,num)
            else:
                heapq.heappushpop(minHeap,num)
        return minHeap[0]


