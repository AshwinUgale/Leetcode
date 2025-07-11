class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxh=[]
        counts=Counter(tasks)
        for task,count in counts.items():
            heapq.heappush(maxh,(-count,task))
        curT=0
        queue=deque()
        while queue or maxh:
            if queue and queue[0][0]<=curT:
                x,y=queue.popleft()
                heapq.heappush(maxh,y)
            if maxh:
                c,t=heapq.heappop(maxh)
                if c+1<0:
                    queue.append([curT+n+1,(c+1,t)])
            
            curT+=1
        return curT
                
