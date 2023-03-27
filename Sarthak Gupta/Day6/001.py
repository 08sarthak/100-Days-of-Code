class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=[]
        l2=[]
        for i in s:
            l1.append(i)
        for j in t:
            l2.append(j)
        l1.sort()
        l2.sort()
        if l1==l2:
            return True
        else:
            return False
