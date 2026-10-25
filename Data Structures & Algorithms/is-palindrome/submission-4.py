class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        point_1 = ""
        point_2 = ""
        for word in s:
            if word.isalnum():
                point_1 += word.lower()

        for word2 in s[::-1]:
            if word2.isalnum():
                point_2 += word2.lower()

        if point_1 == point_2:
            return True
        else:
            return False