class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        def fibonacci(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return fibonacci(n - 1) + fibonacci(n - 2)
        sum = fibonacci(n)
        return sum
