class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        m = max(nums)
        while l<=r:
            if nums[l] < nums[r]:
                m = min(nums[l],m)
                break
            mid = (l+r)//2
            m=min(m,nums[mid])
            if nums[mid] >= nums[l] :
                l = mid+1
            else:
                r = mid -1
        return m
