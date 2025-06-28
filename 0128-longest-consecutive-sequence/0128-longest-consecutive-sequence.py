class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashs=set()
        for n in nums:
            hashs.add(n)
        
        lcount=0
        for n in hashs:
            if n-1 not in hashs:
                cur=n
                count=1
                while cur+1 in hashs:
                    cur=cur+1
                    count+=1
                lcount=max(count,lcount)
        return lcount
