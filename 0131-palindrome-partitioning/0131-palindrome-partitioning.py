class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        cur = []
        def backtrack(i):
            if i >=len(s):
                result.append(cur.copy())
                return
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    cur.append(s[i:j+1])
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return result

    def isPalindrome(self,s,l,r):
        while l <r:
            if s[l] != s[r]:
                return False
            l=l+1
            r=r-1
        return True
            
            