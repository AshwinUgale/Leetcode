class Solution:
    def climbStairs(self, n: int) -> int:
        one = 0
        two = 1
        for i in range(n):
            temp=two
            two = two + one
            one =temp
        return two