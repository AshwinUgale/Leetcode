class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxW=0
        l,r = 0,len(height)-1
        while l<r:
            curW = (r-l) * min(height[l],height[r])
            maxW= max(curW,maxW)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxW