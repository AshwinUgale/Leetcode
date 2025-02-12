class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(cur, p , target):
            if target == 0:
                result.append(cur.copy())
                return 
            if target <= 0:
                return 
            prev = -1
            for i in range(p,len(candidates)):
                if candidates[i] == prev:
                    continue 
                cur.append(candidates[i])
                backtrack(cur,i+1,target-candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([],0, target)
        return result
       