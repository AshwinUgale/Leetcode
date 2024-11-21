class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        for i in range(len(nums)+1):
            sum=sum+i
        for i in nums:
            sum=sum-i
        return sum