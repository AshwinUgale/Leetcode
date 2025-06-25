class Solution:
    def reverseWords(self, s: str) -> str:
        newS=s[::-1]
        ansS=""
        tmp=""
        for c in newS:
            if c!=" ":
                tmp+=c
                print(tmp)
            elif c==" " and tmp:
                ansS+=tmp[::-1]+" "
                tmp=""
        if tmp:
            ansS+=tmp[::-1]
        return ansS.strip()