class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        arr = []
        def backtrack(i):
            if i == len(s):
                res.append(arr.copy())
                return
            for j in range(i,len(s)):
                if self.ispalin(s[i:j+1]):
                    arr.append(s[i:j+1])
                    backtrack(j+1)
                    arr.pop()
        backtrack(0)
        return res
    def ispalin(self,s):
        l=0
        r=len(s)-1
        while l<=r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True