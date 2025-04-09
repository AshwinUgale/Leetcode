class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(arr,i):    
            if len(arr)==k:
                res.append(arr.copy())
                return 
            if i >n:
                return
    
            arr.append(i)
            backtrack(arr,i+1)
            arr.pop()
            backtrack(arr,i+1)
        backtrack([],1)
        return res
