class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = []
        a = 0
        x = len(word1)
        y = len(word2)
        if x<y: 
            z =x
            b = word2
        else: 
            z = y
            b = word1


        while a <z:
            m.append(word1[a])
            m.append(word2[a])
            a+=1
        m.append(b[z:])
        merged= "".join(m)
        return merged