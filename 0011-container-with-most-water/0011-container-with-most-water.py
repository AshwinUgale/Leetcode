class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxW=0
        l=0
        r=len(height)-1
        while l<r:
            maxW=max(maxW,min(height[r],height[l])*(r-l))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxW

