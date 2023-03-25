class Solution(object):
    def isPalindrome(self, x):
        num=0
        y=x
        while(x>0):
            n=x%10
            num=(num*10)+n
            x=x//10
        if num!=y:
            print('false')
        else:
            print("true")
