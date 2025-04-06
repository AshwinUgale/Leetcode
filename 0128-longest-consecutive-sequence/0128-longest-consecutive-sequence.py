class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashm=set(nums)
        longest=0
        for n in hashm:
            if (n-1) not in hashm:
                length = 1
                while (n+1) in hashm:
                    length+=1
                    n+=1
                longest=max(longest,length)
        return longest
    