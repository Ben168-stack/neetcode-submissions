class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for word in s:
            if word.isalnum():
                new_s += word.lower()


        return new_s == new_s[::-1]