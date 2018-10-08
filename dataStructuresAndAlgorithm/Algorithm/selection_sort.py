
# coding: utf-8

# # 选择排序
# 

# **工作原理**
# 首先在**未排序列中找到最小(大)元素**，存**放**到排序序列的**起始位置**，然后，再**从剩余未排元素中继续寻找最小(大)元素**,然后放到**已排序序列的末尾**。以此类推，直到所有的元素均排序完毕

# In[11]:


def selection_sort(alist):
    n = len(alist)
    # 需要进行n-1次选择操作
    for i in range(n-1):
        # 记录最小位置
        min_index = i
        # 从 i+1 位置到 末尾选择 出最小数据
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]


# In[10]:


alist = [54,226,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)


# In[9]:


for i in range(len(alist)):
    print(alist[i],end=' ')


# ## 时间复杂度
# - 最优时间复杂度O(n^2)
# - 最坏时间复杂度O(n^2)
