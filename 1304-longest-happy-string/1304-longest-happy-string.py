class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        char = []
        for cnt,s in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if cnt!=0:
                heapq.heappush(char,(cnt,s))
        res=""
        while char:
            cnt,s=heapq.heappop(char)
            if len(res) > 1 and (res[-1] == res[-2] == s):
                if not char:
                    break
                cnt2,s2= heapq.heappop(char)
                res+=s2
                if cnt2+1!=0:
                    heapq.heappush(char,(cnt2+1,s2))
            else:
                res+=s
                cnt+=1
            if cnt!=0:
                heapq.heappush(char,(cnt,s))
        return res