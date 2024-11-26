class Solution(object):
    def containsDuplicate(self, nums):
        hashm = set()
        for i in nums:
            if i in hashm:
                return True
            else:
                hashm.add(i)
        return False