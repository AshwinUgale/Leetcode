class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inc=[0]*n
        
        for src,des in edges:
            inc[des]+=1
        
        champs=[]
        for i,inc_cnt in enumerate(inc):
            if not inc_cnt:
                champs.append(i)
        if len(champs)>1:
            return -1
        else:
            return champs[0]