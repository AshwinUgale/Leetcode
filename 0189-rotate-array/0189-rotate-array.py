class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
     
        # ans=[0]*len(nums)
        # for i in range(len(nums)):
        #     ans[(i+k)%len(nums)]=nums[i]
        # for i in range(len(nums)):
        #     nums[i]=ans[i]

        k=k% len(nums)

        l,r=0,len(nums)-1
        while l<r:
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l+=1
            r-=1

        l,r=0,k-1
        while l<r:
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l+=1
            r-=1
        l,r=k,len(nums)-1
        while l<r:
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l+=1
            r-=1
      
        