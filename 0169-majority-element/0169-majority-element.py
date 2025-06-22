class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n=len(nums)
        # freq={}
        # for i in nums:
        #     freq[i]=freq.get(i,0)+1
        #     if freq[i]>=ceil(n/2):
        #         return i

        count = 0 
        cur=0
        for i in nums:
            if count==0:
                cur = i
            if i == cur :
                count+=1
            else:
                count-=1
        return cur
            
        