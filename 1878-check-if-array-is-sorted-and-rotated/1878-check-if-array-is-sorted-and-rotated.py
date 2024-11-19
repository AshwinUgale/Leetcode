class Solution(object):
    def check(self, nums):
        sort=sorted(nums)
        for i in range(len(nums)):
            if nums[i:]+nums[:i]==sort:
                return True
        return False
        