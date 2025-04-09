class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashm={}
        lasti=0
        nodup=True
        for i in range(len(nums)):
            if nums[i] in hashm.keys():
                lasti=max(lasti,hashm[nums[i]])
                nodup=False
            hashm[nums[i]]=i
        if lasti==0 and nodup:
            return 0
        print(lasti)
        return (lasti // 3) + 1
