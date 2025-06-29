class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        l=0
        while l<len(nums)-2:
            if l>0 and nums[l]==nums[l-1]:
                l+=1
                continue
            f=l+1
            s=len(nums)-1
            while f<s:
                if nums[l]+nums[f]+nums[s]==0:
                    res.append([nums[l],nums[f],nums[s]])
                    f+=1
                    while f<s and nums[f]==nums[f-1]:
                        f+=1
                elif nums[l]+nums[f]+nums[s]>0:
                    s-=1
                else:
                    f+=1
            l+=1
        return res
