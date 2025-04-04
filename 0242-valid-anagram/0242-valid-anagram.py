class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        dict1={}
        dict2={}
        for i in range(len(s)):
            dict1[s[i]]=1+dict1.get(s[i],0)
            dict2[t[i]]=1+dict2.get(t[i],0)
        for n in dict1:
            n1=dict2.get(n)
            if n1!=dict1[n]:
                return False
        return True
        n= dict2.get('z')
        print(n)
        print(dict1)
        print(dict2)