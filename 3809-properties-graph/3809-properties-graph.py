class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(a,b):
            seta= set()
            for i in a:
                if i in seta:
                    continue
                else:
                    seta.add(i)
            count=0
            uset=set()
            for j in b:
                if j in seta:
                    if j not in uset:
                        count+=1
                        uset.add(j)
            return count
        
        adj = { i:[] for i in range(len(properties))}


        for i in range(len(properties)-1):
            for j in range(i+1,len(properties)):
                if intersect(properties[i],properties[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)
        

        visited= set()
        def dfs(i):
            for neighbor in adj[i]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        components=0
        for i in adj:
            if i in visited:
                continue
            else:
                visited.add(i)
                components+=1
                dfs(i)

        return components
