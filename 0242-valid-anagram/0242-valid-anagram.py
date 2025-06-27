class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hset={}
        for i in range(len(s)):
            hset[s[i]]=hset.get(s[i],0)+1
            hset[t[i]]=hset.get(t[i],0)-1
        for n in hset.values():
            if n != 0:
                return False
        return True
        