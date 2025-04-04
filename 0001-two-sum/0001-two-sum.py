class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,n in enumerate(nums):
            v = target - n
            if v in dict1:
                return [dict1[v],i]
            else:
                dict1[n]=i
