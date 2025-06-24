class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        post=1
        arr=[0]*(len(nums))
        for i in range(len(nums)):
            arr[i]=pre
            pre=pre*nums[i]
        for i in range(len(nums)-1,-1,-1):
            tmp = nums[i]
            nums[i] = post*arr[i]
            post = post*tmp
        return nums