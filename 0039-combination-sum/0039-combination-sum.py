class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        arr = []
        def backtrack(i,rem):
            if rem  == 0 :
                res.append(arr.copy())
                return 
            if i == len(candidates) or rem < 0 :
                return 
            
            arr.append(candidates[i])
            backtrack(i,rem-candidates[i])
            arr.pop()
            backtrack(i+1,rem)
        backtrack(0,target)
        return res
