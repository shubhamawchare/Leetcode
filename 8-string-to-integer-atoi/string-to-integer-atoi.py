class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Sign
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1
        
        # Convert digits
        result = 0
        
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # Check overflow before adding digit
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            result = result * 10 + digit
            i += 1
        
        return sign * result