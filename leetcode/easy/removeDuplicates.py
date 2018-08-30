# 删除 排序数组重复项
# eg：给定 nums = [0,0,1,1,1,2,2,3,3,4],
#函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
def removeDuplicates(nums):
    i=0
    while i <len(nums)-1:
        if nums[i]==nums[i+1]:
            nums.remove(nums[i])
        else:
            i=i+1
    return len(nums)


nums=[1,1,2,3,3,3]
nn=removeDuplicates(nums)
print(nn)