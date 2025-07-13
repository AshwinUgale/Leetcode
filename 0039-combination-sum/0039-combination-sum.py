class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(i,arr,s):
            if i==len(candidates) or s>target:
                return 
            if s==target:
                res.append(arr.copy())
                return
            arr.append(candidates[i])
            backtrack(i,arr,s+candidates[i])
            arr.pop()
            backtrack(i+1,arr,s)
        backtrack(0,[],0)
        return res