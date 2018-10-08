
# coding: utf-8

# # 队列 
# - 是一种线性表
# 
# ** 特点**
# - 1 先进先出
# - 2 不允许在中间部位进行操作

# In[2]:


class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)


# In[3]:


q = Queue()
q.enqueue("hello")
q.enqueue("world")
q.enqueue("itcast")


# In[5]:


q.size()


# In[16]:




