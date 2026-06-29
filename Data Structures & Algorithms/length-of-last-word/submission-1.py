class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,j = 0,0
        res = 1
        for i in range(len(s)):
            if s[i] != ' ':
                i+=1
                j+=1
                res=j
            else:
                i+=1
                j=0
                
        return res