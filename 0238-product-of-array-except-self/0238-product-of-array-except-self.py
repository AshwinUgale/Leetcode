class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=1
        post=1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*=post
            post*=nums[i]
        return res
