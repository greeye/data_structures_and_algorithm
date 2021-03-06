
# coding: utf-8

# ## 双向链表

# - 每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；
# - 而另一个指向下一个节点，当此节点为最后一个节点时，指向空值。

# In[2]:


class Node(object):
    """双向链表节点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    """双向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表的长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item,end='')
            cur = cur.next

    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self.__head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self.__head
            # 将_head的头节点的prev指向node
            self.__head.prev = node
            # 将_head 指向node
            self.__head = node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self.__head = node
        else:
            # 移动到链表尾部
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def search(self, item):
        """查找元素是否存在"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


# In[ ]:


ll = SinCycLinkedlist()
ll.add(1)
ll.add(2)
ll.append(3)
ll.insert(2, 4)
ll.insert(4, 5)
ll.insert(0, 6)
ll.travel()
ll.remove(1)
print "length:",ll.length()
ll.travel()

