class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        Cz=0
        for i in range(len(nums)):
            if nums[i] == 0:
                Cz+=1
            else:
                ans+=(Cz*(Cz+1)//2)
                Cz=0
        return ans+(Cz*(Cz+1)//2)