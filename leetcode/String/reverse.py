'''
Given a 32-bit signed integer, reverse digits of an integer.
'''
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            x = x[::-1]
            x = '-' + x
        elif x == '0':
            return 0
        elif x[len(x) - 1] == '0':
            x = x[:len(x) - 1]
            x = x[::-1]
        elif len(x) >= 2:
            x = x[::-1]
        else:
            return int(x)
        return int(x) if -2147483648 < int(x) < 2147483647 else 0
