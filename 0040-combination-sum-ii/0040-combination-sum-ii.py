class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(i,arr,s):
            if s==target:
                res.append(arr.copy())
                return
            for n in range(i,len(candidates)):
                if n>i and candidates[n]==candidates[n-1]:
                    continue
                if s>target:
                    break
                arr.append(candidates[n])
                backtrack(n+1,arr,s+candidates[n])
                arr.pop()
               
        backtrack(0,[],0)
        return res