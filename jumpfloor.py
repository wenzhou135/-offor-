from time import perf_counter as pc


class Solution:
    def jumpfloor(self, number):
        if number <= 3:
            return number
        a = 2
        b = 1
        for i in range(number-2):
            a, b = a + b, a
        return a


solution = Solution()
start = pc()
for i in range(10000):
    a = solution.jumpfloor(4)
print(a, pc() - start)
