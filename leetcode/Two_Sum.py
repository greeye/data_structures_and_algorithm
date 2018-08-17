'''

题目：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数
  例子：nums [2,7,11,15],target = 9
    因为： nums[0] + nums[1] = 2+7 =9
    返回 [0,1]
'''

# 解一
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if isinstance(nums, list):
            for x in range(0, len(nums)):
                for y in range(x, len(nums)):
                    if (nums[x]+nums[y] == target)and x < y:
                        return [x, y]




   #改进
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x]+nums[y] == target:
                    return [x, y]

solution = Solution()
list1 = solution.twoSum([2, 7, 11, 15], 9)
print(list1)
