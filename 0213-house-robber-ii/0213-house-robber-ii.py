class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper(self,nums):
        r1,r2=0,0
        for n in nums:
            tmp = max(r1+n,r2)
            r1= r2
            r2 = tmp
        return r2
       
