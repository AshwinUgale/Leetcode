class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lp = [1]*len(nums)
        # rp = [1]*len(nums)
        # c=1
        # arr=[1]*len(nums)
        # for i in range(len(nums)):
        #     lp[i]=c
        #     c=c*nums[i]
        # c=1
        # for i in range(len(nums)-1,-1,-1):
        #     rp[i]=c
        #     c=c*nums[i]
        # for i in range(len(nums)):
        #     arr[i]=lp[i]*rp[i]
        # return arr
        res=[]
        c=1
        for i in range(len(nums)):
            res.append(c)
            c=c*nums[i]
        c=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*c
            c=c*nums[i]
        return res