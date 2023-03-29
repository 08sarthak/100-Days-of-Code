class Solution:
    def isUgly(self, n: int) -> bool:
        fac=[1,2,3,5]
        fact=[]
        for i in range(1,n):
            if n%i==0:
                fact.append(i)
        if (set(fact).issubset(set(fac))):
            return True
        else:
            return False
