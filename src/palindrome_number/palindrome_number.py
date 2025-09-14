class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        left: int = 0
        right: int = len(num_str)-1
        if len(num_str) <= 1:
            return True
        while left < right:
            if num_str[left] == num_str[right]:
                if right - left <= 2:
                    return True
                left += 1
                right -= 1
                continue
            else:
                return False
            
    def isAltPalindrome(self, x: int) -> bool:
        divisor: int = 1
        while x // divisor >= 10:
            divisor *= 10
        while divisor >= 1:
            left = x // divisor
            right = x % 10
            if left != right:
                return False
            x = x - (left * divisor)
            x = x // 10
            divisor = divisor // 100
        return True
            