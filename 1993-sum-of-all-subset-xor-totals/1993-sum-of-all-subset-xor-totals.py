class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total=0
        self.sum=0
        def backtrack(total,i):
            if i == len(nums):
                self.sum+=total
                return total
            total^=nums[i]
            backtrack(total,i+1)
            total^=nums[i]
            backtrack(total,i+1)
        backtrack(0,0)
        return self.sum


