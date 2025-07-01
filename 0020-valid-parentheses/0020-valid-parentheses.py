class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for c in s:
            if c =="(" or c =="{" or c =="[":
                arr.append(c)
            elif c == ")" and arr and arr[-1]=="(":
                arr.pop(-1)
            elif c == "}" and arr and arr[-1]=="{":
                arr.pop(-1)
            elif c == "]" and arr and arr[-1]=="[":
                arr.pop(-1)
            else:
                return False
        if len(arr)==0 :
            return True
        else:
            return False