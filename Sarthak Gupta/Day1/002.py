class Solution(object):
    def fizzBuzz(self, n):
        L=[]
        for i in range(1,n+1):
            if(i%15==0):
                L.append("FizzBuzz")
            elif(i%3==0):
                L.append("Fizz")
            elif(i%5==0):
                L.append("Buzz")
            else:
                L.append(str(i))
        return L
        """
        :type n: int
        :rtype: List[str]
        """
