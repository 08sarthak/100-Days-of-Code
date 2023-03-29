class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.split()
        p=""
        for i in range(len(k)-1,-1,-1):
            p=p+k[i]+" "
        return p.strip()
