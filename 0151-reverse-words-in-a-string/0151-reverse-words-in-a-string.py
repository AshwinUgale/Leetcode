class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        ans=[]
        for i in range(len(words)-1,-1,-1):
            ans.append(words[i])
            if i != 0 :
                ans.append(" ")
        return "".join(ans)


        # newS=s[::-1]
        # ansS=""
        # tmp=""
        # for c in newS:
        #     if c!=" ":
        #         tmp+=c
        #         print(tmp)
        #     elif c==" " and tmp:
        #         ansS+=tmp[::-1]+" "
        #         tmp=""
        # if tmp:
        #     ansS+=tmp[::-1]
        # return ansS.strip()

