class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        arr=[]
        def backtrack(i,s):
            if i==len(candidates) or s>target:
                return 
            if s==target:
                if arr in res:
                    return
                res.append(arr.copy())
            arr.append(candidates[i])
            backtrack(i,s+candidates[i])
            arr.pop()
            backtrack(i+1,s)
        backtrack(0,0)
        return res