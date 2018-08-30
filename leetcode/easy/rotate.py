# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
def rotare(nums,k):
     nums1 = nums[:len(nums)-k]
     nums2 = nums[len(nums)-k:]+nums1
     return nums2

nums = [1,2,3,4,5,6,7]
nn=rotare(nums,3)
print(nn)