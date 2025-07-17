class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        arr=[]
        
        def ispalindrome(start,end):
            return s[start:end+1]==s[start:end+1][::-1]

        def backtrack(start):
            if start==len(s):
                res.append(arr.copy())
                return
            for end in range(start,len(s)):
                if ispalindrome(start,end):
                    arr.append(s[start:end+1])
                    backtrack(end+1)
                    arr.pop()
        backtrack(0)
        return res
            

        
                