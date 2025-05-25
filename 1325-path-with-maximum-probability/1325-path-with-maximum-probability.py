class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src,dst=edges[i]
            adj[src].append([dst,succProb[i]])
            adj[dst].append([src,succProb[i]])
        
        pq = [(-1,start_node)]
        visited = set()
        while pq:
            prob,cur = heapq.heappop(pq)
            visited.add(cur)
            if cur == end_node:
                return (prob*-1)
            for nei,ep in adj[cur]:
                if nei not in visited:
                    heapq.heappush(pq,(prob*ep,nei))
        return 0