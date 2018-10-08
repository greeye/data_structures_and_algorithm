
# coding: utf-8

# In[5]:


'''
二分法搜索：
      递归查找
      非递归查找
'''
# 递归查找
def binary_search(alist,item):
    n= len(alist)
    if n>0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
        
    return False


# In[9]:


# 非递归查找
def binary_search_2(alist,item):

    n = len(alist)
    first = 0
    last =n-1
    while first <= last:
        mid = (first+last)//2
        if alist[mid]==item:
            return True
        elif item <alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


# In[14]:


li = [2,3,4,5,7,8,9,13,15,17]
print(binary_search(li,9))
print(binary_search(li,10))

print(binary_search_2(li,9))
print(binary_search_2(li,10))

