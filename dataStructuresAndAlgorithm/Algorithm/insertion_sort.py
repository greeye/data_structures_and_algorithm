
# coding: utf-8

# ## 插入排序
# **工作原理**
# 
# - 是通过**构建有序序列**，对于未排序数据，在已经排序序列中**从后向前扫描**，找打相应位置并插入。
# - 需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间

# In[1]:


def insert_sort(alist):
    # 从第二个位置，即下标为1 的元素开始向前插入
    for i in range(1,len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


# In[25]:


alist = [1, 2, 0, 3]
for j in range(2,0,-1):
    if alist[j] < alist[j-1]:
        alist[j], alist[j-1] = alist[j-1], alist[j]        


# In[26]:




