'''

 给定一个整数，编写一个函数判断它是否是2的幂次方

'''

# 错误：没有限定好n的范围
class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        #  n & (n-1) 位运算
        elif (n & (n - 1)) == 0:
            return True

solution = Solution()
solution.isPowerOfTwo(5)


# 正确编程
class Solution1:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        #  n & (n-1) 位运算
        elif (n & (n - 1)) == 0:
            return True
        else:
            return False

solution = Solution()
solution.isPowerOfTwo(5)
