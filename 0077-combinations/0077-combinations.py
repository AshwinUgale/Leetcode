class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
      
        def backtrack(arr,i):
           
            if len(arr)==k:
                res.append(arr.copy())
                return 
            for j in range(i,n+1):
                arr.append(j)
                backtrack(arr,j+1)
                arr.pop()
       

        backtrack([],1)

        return res
