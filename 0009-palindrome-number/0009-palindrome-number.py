class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        x_dao = x[::-1]
        if x == x_dao:
            return True
        else:
            return False
        