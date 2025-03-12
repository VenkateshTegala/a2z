class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        number = x
        rev_num = 0
        while(number > 0):
            digit = number % 10
            #the below line also deals with the last zeroes
            rev_num = (rev_num * 10) + digit
            number = number // 10
        return x == rev_num
        