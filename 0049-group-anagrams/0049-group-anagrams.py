class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            arr={}
            for c in s:
                arr[c]=arr.get(c,0)+1
            result[tuple(sorted(arr.items()))].append(s)
            
        return list(result.values())
