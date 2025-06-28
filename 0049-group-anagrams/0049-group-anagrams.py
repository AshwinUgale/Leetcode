class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            arr=[0]*26
            for c in s:
                arr[ord(c)-ord('a')]+=1
            result[tuple(arr)].append(s)
            
        return list(result.values())
