class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = []
        y = 0
        for i in range(len(s)):
            if s[i].isalpha():
                x.append(s[i])
            if s[i].isdigit():
                x.append(s[i])
                y = y+1
        if len(x)==0:
            if len(s)==0:
                return False
            else:
                return True
        if len(x)==1:
            if len(s)==1:
                return True
            elif y==0:
                return True
        if x==x[::-1]:
            return True
        else:
            return False 