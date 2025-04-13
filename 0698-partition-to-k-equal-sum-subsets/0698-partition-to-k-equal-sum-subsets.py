class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums)%k:
            return False
        target = sum(nums)//k
        subSet=[0]*k
        nums.sort(reverse=True)
        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(k):
                if subSet[j]+nums[i]<=target:
                    subSet[j]+=nums[i]

                    if backtrack(i+1):
                        return True

                    subSet[j]-=nums[i]

                    if subSet[j] == 0:
                        break
            return False

        return backtrack(0) 