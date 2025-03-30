class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        r1,r2=0,0
        for i in range(0,len(nums)-1):
            tmp=max(nums[i]+r1,r2)
            r1 = r2
            r2 = tmp
        R1,R2=0,0
        for i in range(1,len(nums)):
            tmp=max(nums[i]+R1,R2)
            R1 = R2
            R2 = tmp
        return max(r2,R2)
