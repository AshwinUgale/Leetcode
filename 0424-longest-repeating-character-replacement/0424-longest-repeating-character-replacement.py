class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ml=0
        l=0
        dic={}
        for r in range(len(s)):
            dic[s[r]]=1+dic.get(s[r],0)
            if r-l+1>max(dic.values()) + k:
                dic[s[l]]=dic.get(s[l])-1
                l+=1
                
            ml=max(ml,r-l+1)
        return ml