class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        maxL=0
        l=0
        r=0
        while r<len(s):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.add(s[r])
            maxL = max(maxL,r-l+1)
            r+=1
        return maxL


            
