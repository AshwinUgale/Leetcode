class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]>=ceil(n/2):
                return i
        