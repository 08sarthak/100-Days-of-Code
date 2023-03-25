class Solution(object):
    def fib(self, n):
        n1=0
        n2=1
        count=0
        while(count<n):
            n3=n1+n2
            n1=n2
            n2=n3
            count+=1
        return n1
        """
        :type n: int
        :rtype: int
        """
