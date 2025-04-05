class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm={}
        countn=[[] for i in range(len(nums)+1)]
        for n in nums:
            hashm[n]=1+hashm.get(n,0)
        for n,c in hashm.items():
            countn[c].append(n)
        
        res=[]
        for i in range(len(countn)-1,0,-1):
            for n in countn[i]:
                res.append(n)
                if len(res) == k:
                    return res
                