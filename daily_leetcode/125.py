class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        start = 0
        end = len(s)-1

        while start <= end:
            if s[start].isalnum():
                if s[end].isalnum():
                    if s[start] == s[end]: 
                        start += 1
                        end -= 1
                    else:
                        return False
                else:
                    end -= 1
            else:
                start+=1                   
            
        return True
            
