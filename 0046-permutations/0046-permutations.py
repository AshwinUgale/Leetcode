class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        def backtrack():
            if len(cur) == len(nums):
                result.append(cur.copy())
                return
            
            for n in nums:
                if n not in cur:
                    cur.append(n)
                    backtrack()
                    cur.pop()
        backtrack()
        return result