class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # Check 32-bit overflow before multiplying
            if result > (2**31 - 1 - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result