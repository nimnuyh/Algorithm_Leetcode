class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 :
            return n
        else :
            return self.fib(n - 2) + self.fib(n - 1)