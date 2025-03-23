class Solution:
    def maxSum(self, nums: List[int]) -> int:
        set1=set()
        sum=0
        
        for r in range(len(nums)):
            if nums[r] in set1:
                continue
            set1.add(nums[r])
            if nums[r]>0:
                sum+=nums[r]

        if sum>0:
            return sum
        nums.sort()
        return nums[-1]