
# coding: utf-8

# In[15]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# In[8]:


'''
单链表
  1、节点实现
  2、单链表的实现
  
     2.1 添加元素
        头部添加
        尾部添加
        指定位置添加元素
     2.2 删除节点
     2.3 查找节点是否存在
     2.4 查看链表长度
     2.5 链表是否为空
     2.6 遍历链表
'''
class SingleNode(object):
    '''单链表的节点'''
    def __init__ (self,item):
        # item 存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None
        
class SingleLinkList(object):
    '''单链表'''
    def __init__(self):
        self.__head = None   # 链接域
    
    # 头部添加元素
    def add(self,item):
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self.__head
         # 将链表的头_head指向新节点
        self.__head = node


# In[9]:


sg = SingleLinkList


# In[10]:


sg.add('1')


# In[59]:


class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


# In[60]:


class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        # head 可见的 属性
        self.head = None
        # __tail 不可见的属性__
        self.__tail = 1
    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self.head
        # 将链表的头_head指向新节点
        self.head = node


# In[61]:


si =SingleLinkList()


# In[62]:


si.add(1)


# In[64]:


si.add(1)


# In[20]:


class SingleNode(object):
    '''单链表的节点'''
    def __init__ (self,item):
        # item 存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


# In[47]:


class SingleLinkList(object):
    '''单链表'''
    def __init__(self):
        self.head = None   # 链接域
    def is_empty(self):
        return self.head == None
    # 头部添加元素
    def add(self,item):
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self.head
         # 将链表的头_head指向新节点
        self.head = node
    # 尾部添加
    def append(self,item):
        '''尾部添加元素'''
        node =SingleNode(item)
        # 先判断链表是否为空
        if self.is_empty():
            self.head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.head
            while cur.next !=None:
                cur =cur.next
            cur.next = node
    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur != None:
            print(cur.item)
            cur = cur.next
            
    


# In[48]:


sn =SingleLinkList()


# In[50]:


sn.add(1)


# In[52]:


sn.travel()


# In[51]:


sn.append(2)


# In[26]:


sn.head


# In[27]:


sn.add(2)


# In[28]:


sn.head


# In[29]:


sn.travel()


# In[31]:


sn.head

