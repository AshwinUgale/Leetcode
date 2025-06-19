class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return False
        sumA= sum(nums)
        if sumA%2!=0:
            return False
        dp=set()
        dp.add(0)
        target=sumA//2
        for i in range(len(nums)):
            curdp=set()
            for t in dp:
                if (t+nums[i] ==target):
                    return True
                curdp.add(t+nums[i])
                curdp.add(t)
            dp=curdp
        return True if target in dp else False

        