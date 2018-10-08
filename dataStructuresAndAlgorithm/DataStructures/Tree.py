
# coding: utf-8

# In[5]:


class Node(object):
    '''节点类'''
    def __init__(self,elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


# In[51]:


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = None
    
    def add(self,elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            # 对已有的节点进行层次遍历
        while queue:
            cur = queue.pop(0)
            if cur.lchild ==None:
                cur.lchild = node
                return
            elif cur.rchild == None:
                cur.rchild = node
                return
            else:
                # 如果左右子树都不为空，加入队列继续判断
                queue.append(cur.lchild)
                queue.append(cur.rchild)
    def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return
        print(root.elem,end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)
    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
             return
        self.inorder(root.lchild)
        print(root.elem,end= ' ')
        self.inorder(root.rchild)
    def outorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.outorder(root.lchild)
        self.outorder(root.rchild)
        print(root.elem,end= ' ')
    #  广度优先遍历（层次遍历）

    def breadth_travel(self):
    """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem,end=' ')
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)


# In[38]:


tree = Tree()


# In[48]:


tree.add(4)


# In[49]:


tree.preorder(tree.root)

