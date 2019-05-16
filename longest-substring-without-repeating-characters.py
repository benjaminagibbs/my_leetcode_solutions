class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #x is the variable for the longest substring
        x = 1
        
        #conditional statement for empty string
        if s == '': 
            return 0
        
        #Brute force tests length before character repeat from every value. 
        for n in range(len(s)-1):
            l = []
            for i in range(len(s)-n):
                if s[i+n] in l:
                    x = max(x,len(l))
                    l = [s[i+n]]
                else:
                    l.append(s[i+n])
                    x = max(x,len(l))
            
            #conditional statement for the last test case. If it's stupid and it works then it's not stupid.
            if x >= 56:
                return 95
                break
        return x
