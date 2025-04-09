class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(total,i):
            if i == len(nums):
                return total
            return backtrack(total^nums[i],i+1)+backtrack(total,i+1)
        
        return backtrack(0,0)


