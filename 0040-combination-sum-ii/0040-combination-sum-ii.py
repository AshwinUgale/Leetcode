class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        arr = []
        def backtrack(i,rem):
            if rem == 0:
                res.append(arr.copy())
                return
            if i == len(candidates) or rem < 0 :
                return
            arr.append(candidates[i])
            backtrack(i+1,rem-candidates[i])
            arr.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1,rem)
        backtrack(0,target)
        return res