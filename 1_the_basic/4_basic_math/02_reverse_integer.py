class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #condition to check whether x is negative
        negative = False
        if x < 0:
            negative = True
            x = abs(x)

        #loop to remove the last zeroes
        while(x != 0 and x % 10 == 0):
            x = x//10

        #reversing the number
        def reverse_number(x):
            rev_num = 0
            while x != 0:
                digit = x % 10
                rev_num = (rev_num * 10) + digit
                x = x//10
            return rev_num

        result = reverse_number(x)

        #checking the integer constraints
        if result < -2**31 or result > 2**31 -1:
            return 0
        
        if(negative):
            return -1 * result
        else:
            return result