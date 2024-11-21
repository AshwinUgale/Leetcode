class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mo=0
        m=0
        for i in nums:
            
            if i==1:
                m+=1
                if m>mo:
                    mo=m
            else:
                m=0
        return mo
