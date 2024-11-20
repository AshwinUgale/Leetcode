class Solution(object):
    def moveZeroes(self, nums):
    
        # arr = []
        # k=0
        # for i in nums:
        #     if i != 0:
        #         arr.append(i)
        #     else:
        #         k+=1
        # while k >0:
        #     arr.append(0)
        #     k-=1
        # for i in range(len(arr)):
        #     nums[i]=arr[i]
             
        l=0
        r=0
        while r < len(nums):
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r+=1
            else:
                r+=1
                