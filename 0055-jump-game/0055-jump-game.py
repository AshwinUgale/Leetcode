class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end=len(nums)-1
        for j  in range(len(nums)-1,-1,-1):
            if j + nums[j] >= end:
                end = j
        if end == 0:
            return True
        else:
            return False