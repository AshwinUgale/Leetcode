class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hset=set()
        uCount=0
        l=0
        for r in range(len(nums)):
            if nums[r] not in hset:
                hset.add(nums[r])
                nums[l],nums[r] = nums[r],nums[l]
                uCount+=1
                l+=1
        
        return uCount