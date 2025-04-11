class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            if len(str(i))%2!=0:
                continue
            elif len(str(i))==2:
                fh=str(i//10)
                sh=str(i%10)
                sum1=0
                sum2=0
                for i in range(len(str(fh))):
                    sum1+=int(fh[i])
                    sum2+=int(sh[i])
                if sum1==sum2:
                    count+=1
            elif len(str(i))==4:
                fh=str(i//100)
                sh=str(i%100)
                if len(sh)==1:
                    sh="0"+sh
                
                sum1=0
                sum2=0
                for i in range(len(str(fh))):
                    sum1+=int(fh[i])
                    sum2+=int(sh[i])
                if sum1==sum2:
                    count+=1
        return count
        
        
