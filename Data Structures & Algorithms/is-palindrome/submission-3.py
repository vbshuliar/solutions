class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = "abcdefghijklmnopqrstuvwxyz0123456789"
        b, e = 0, len(s) - 1

        while b <= e:
            if s[b] not in a:
                b += 1
                continue
            if s[e] not in a:
                e -= 1
                continue
            if s[e] != s[b]:
                return False
            if s[e] == s[b]:
                b += 1
                e -= 1
        return True
            
                
            
        
        