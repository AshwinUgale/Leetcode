class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        arr1=[0]*26
        
        for i in range(len(s1)):
            arr1[ord(s1[i])-ord('a')]+=1
        
        l=0
        r=len(s1)-1
        while r<len(s2):
            arr2=[0]*26
            for i in range(l,r+1):
                arr2[ord(s2[i])-ord('a')]+=1
      
            if arr1==arr2:
                return True
            l+=1
            r+=1
        return False
            
        

        