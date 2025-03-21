class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        a=set()
        a.add(s[0])
        maxL=0
        l=0
        r=1
        while r<len(s):
            if s[r] in a:
                while s[r] in a:
                    a.remove(s[l])
                    l+=1
            a.add(s[r])
            maxL = max(maxL,r-l)
            r+=1
        return maxL+1


            
