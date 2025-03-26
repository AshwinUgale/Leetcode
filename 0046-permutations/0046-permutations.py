class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []
        def backtrack():
            if len(arr)==len(nums):
                res.append(arr.copy())
                return
            for i in nums:
                if i not in arr:
                    arr.append(i)
                    backtrack()
                    arr.pop()
        backtrack()
        return res