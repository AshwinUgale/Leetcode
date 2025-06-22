class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        def isPrime(n):
            if n<2:
                return False
            div=0
            for i in range(1,n+1):
                if n%i==0:
                    div+=1
            if div==2:
                return True
            else:
                return False
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for key,value in freq.items():
            if isPrime(value):
                return True
        return False
        

       