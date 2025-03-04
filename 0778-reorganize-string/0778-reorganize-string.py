class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt,s] for [s,cnt] in count.items()]
        heapq.heapify(maxHeap)
        prev = None
        res=""
        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            cnt,s = heapq.heappop(maxHeap)
            res+=s
            cnt+=1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None

            if cnt!=0:
                prev = [cnt,s]
        return res