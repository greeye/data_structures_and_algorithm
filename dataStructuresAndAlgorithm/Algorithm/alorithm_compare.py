
# coding: utf-8

# ## 1 冒泡排序
# - 从 头[0] 两两对比，如果左边元素大于右边，调换位置，按照顺序一个一个进行对比，到最后一个元素
# - 排序忘一个就能选择出最小的那个元素排到相应的位置，将剩下的元素一一进行这种左右对比的方式进行排序，直至全部排序结束

# In[13]:


def maopaopaixun(alist):
    n = len(alist)
    for i in range(n-1,0,-1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                alist[j+1],alist[j] = alist[j],alist[j+1]


# In[14]:


alist = [10,12,14,9,3,2]
maopaopaixun(alist)
alist


# ##  2 选择排序
# - 每次遍历所有没有排序的序列，挑选最小(最大的值)，然后进行排序
# - 按照这种逻辑进行重复遍历未排序的序列，直到全都排序完

# In[27]:


def select_sort(alist):
    n = len(alist)
    for i in range(n-1):
        min_sort = i
        if alist[min_sort]>alist[i+1]:
            min_sort = i+1
            print(i+1)
        


# In[28]:


alist = [10,12,14,9,3,2]
select_sort(alist)
alist


# In[29]:


def select_sort(alist):
    n =len(alist)
    # 需要进行 n-1 次选择操作
    for i in range(n-1):
        # 记录最小位置
        min_index =i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1,n):
            if alist[j] <alist[min_index]:
                min_index =j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            # alist[min_index] 和 alist[i] 对调
            alist[i], alist[min_index] = alist[min_index], alist[i]


# In[30]:


alist = [10,12,14,9,3,2]
select_sort(alist)
alist


# ## 3.插入排序法

# - 通过**构建有序序列**，对于未排序数据，在已排序序列中**从后向前扫描**，找到相应位置并插入。

# In[35]:


def insert_sort(alist):
    for i in range(1,len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


# In[36]:


alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)

