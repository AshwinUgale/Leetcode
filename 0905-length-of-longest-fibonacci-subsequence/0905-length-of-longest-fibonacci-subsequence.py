class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hset = set(arr)
        l=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev = arr[i]
                cur = arr[j]
                nex = prev+cur
                cl=2
                while nex in hset:
                    cl+=1
                    prev,cur=cur,nex
                    nex = prev+cur
                    l=max(l,cl)
        return l

