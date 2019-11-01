from collections import deque

class TreeNode:
    '''树的结点'''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Traversal:
    '''二叉树的DFS,BFS遍历'''

    def __init__(self):
        self.res = list()

    def preorder_recur(self, root):
        '''DFS前序遍历，递归'''
        if root:
            self.res.append(root.val)
            self.preorder_recur(root.left)
            self.preorder_recur(root.right)
        return self.res

    def preorder(self, root):
        '''DFS前序遍历，非递归'''
        stack = []
        output = []
        stack.append(root)
        while stack:
            r = stack.pop()
            if r is not None:
                output.append(r.val)
                if r.right is not None:
                    stack.append(r.right)
                if r.left is not None:
                    stack.append(r.left)
        return output

    def inorder_recur(self, root):
        '''DFS中序遍历，递归'''
        if root:
            self.inorder_recur(root.left)
            self.res.append(root.val)
            self.inorder_recur(root.right)
        return self.res

    def inorder(self, root):
        '''DFS中序遍历，非递归'''
        stack = []
        output = []
        p = root  # 指针
        while stack or p:
            while p:  # 左子树压栈
                stack.append(p)
                p = p.left
            p = stack.pop()
            output.append(p.val)  # 输出栈顶元素
            p = p.right  # 右子树
        return output

    def postorder_recur(self, root):
        '''DFS后序遍历，递归'''
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        return self.res

    def postorder(self, root):
        '''DFS后序遍历，非递归'''
        if root is None:
            return []
        stack = []
        output = []
        stack.append(root)
        while stack: #从上至下，从左至右压栈然后倒序输出
            r = stack.pop()
            output.append(r.val)
            if r.left is not None:
                stack.append(r.left)
            if r.right is not None:
                stack.append(r.right)
        return output[::-1] # 倒序输出

    def levelorder(self, root):
        '''BFS层序遍历非递归实现'''
        levels = []
        if not root:
            return levels
        level = 0  # 当前层
        queue = deque([root])  # 队列
        while queue:
            levels.append([])  # 当前层
            level_length = len(queue)  # 当前层的大小
            for i in range(level_length): # 遍历当前层的所有元素
                node = queue.popleft() # 出队
                levels[level].append(node.val)
                # 子节点入队
                if node.left:
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)
            level += 1
        return levels


