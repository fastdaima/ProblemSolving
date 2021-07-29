class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

    # converting from recursive to iterative always use stack
    def fibIterative(self,n):
        sum = 0
        stack = []
        stack.append(n)
        while(len(stack) > 0):
            n = stack.pop()
            if n == 0:
                sum += 0
            elif n == 1:
                sum += 1
            else:
                stack.append(n-1)
                stack.append(n-2)
        return sum 





s = Solution()
# print (s.fib(3))
print (s.fibIterative(3))
print (s.fibIterative(9))