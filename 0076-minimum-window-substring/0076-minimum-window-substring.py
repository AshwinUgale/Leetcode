class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount={}
        for c in t:
            tcount[c]=1+tcount.get(c,0)
        scount={}
        l=0
        need=len(tcount)
        have=0
        res=[0,float("inf")]
        for r in range(len(s)):
            scount[s[r]]=1+scount.get(s[r],0)
            if s[r] in tcount and scount[s[r]]==tcount[s[r]]:
                have+=1
            while need==have:
                if (r-l+1)<res[1]-res[0]:
                    res=[l,r+1]
                scount[s[l]]=scount.get(s[l])-1
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]] if res[1]!=float("inf") else ""

