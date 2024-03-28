class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative numbers are not palindromes
    
        original_x = x
        reversed_x = 0
    
        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
    
    # Compare the reversed number with the original number
        return original_x == reversed_x