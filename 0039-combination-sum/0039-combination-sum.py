class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        arr=[]
        def backtrack(i,t):
            if t==0:
                res.append(arr.copy())
                return
            if i==len(candidates) or t<0:
                return
            arr.append(candidates[i])
            backtrack(i,t-candidates[i])
            arr.pop()
            backtrack(i+1,t)
        backtrack(0,target)
        return res