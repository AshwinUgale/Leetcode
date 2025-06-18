class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)

        nums = sorted(list(set(nums)))
        
        one = 0 
        two = 0
        for i in range(len(nums)):
            cur=nums[i]*count[nums[i]]
            if i>0 and nums[i] == nums[i-1]+1:
                temp = two
                two = max(cur+one,two)
                one = temp
            else:
                temp = two
                two = cur+two
                one = temp

        return two