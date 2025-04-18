class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)):
            temp=set()
            for t in dp:
                temp.add(t+nums[i])
                temp.add(t)
            dp = temp
        return True if target in dp else False