class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary= bin(n)[2:]
        # sbc=0
        # for b in binary:
        #     if b=="1":
        #         sbc+=1
        # return sbc

        # sbc=0
        # while n:
        #     sbc+=n%2
        #     n=n>>1
        # return sbc

        sbc=0
        while n:
            n=n&(n-1)
            sbc+=1
        return sbc
