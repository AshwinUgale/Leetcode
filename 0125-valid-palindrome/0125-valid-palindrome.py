class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS=""
        for c in s:
            if c.isalnum():
                newS+=c.lower() 
        return newS[::-1]==newS







        #solution 1 
        # l,r= 0,len(s)-1
        # while l<=r:
        #     if s[l].isalnum() and s[r].isalnum():
        #         if s[l].lower() == s[r].lower():
        #             l+=1
        #             r-=1
        #         else:
        #             return False
        #     else:
        #         if s[l].isalnum():
        #             r-=1
        #         else:
        #             l+=1
        # return True
    #solution 2
    #     l,r= 0,len(s)-1
    #     while l<r:
    #         while l<r and not self.alphaNum(s[l]):
    #             l+=1
    #         while r>l and not self.alphaNum(s[r]):
    #             r-=1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l+=1
    #         r-=1
    #     return True
    # def alphaNum(self,c):
    #     return (ord('A')<=ord(c)<=ord('Z') or
    #             ord('a')<=ord(c)<=ord('z') or
    #             ord('0')<=ord(c)<=ord('9'))

    #solution 3
        # newStr=""
        # for c in s:
        #     if c.isalnum():
        #         newStr+=c.lower()
        # return newStr == newStr[::-1]
      