class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k:
            return -1
        hashm=set()
        for n in nums:
            if n in hashm:
                continue
            else:
                hashm.add(n)
        if k not in  hashm:
            hashm.add(k)
        return len(hashm)-1