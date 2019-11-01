class TreeNode:
    '''树的结点'''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    '''二叉搜索树'''
    def __init__(self, node_list):
        self.root = TreeNode(node_list[0])
        for i in node_list[1:]:
            self.insert(i)

    def insert(self, ele):
        flag, node, parent = self.find(self.root, self.root, ele)
        if not flag: # 没查到
            tmp = TreeNode(ele)
            if ele < parent.val:
                parent.left = tmp
            else:
                parent.right = tmp

    def find(self, node, parent, ele):
        if node is None:
            return False, node, parent
        if ele == node.val:
            return True, node, parent
        if ele < node.val:
            # 向左子树查找
            return self.find(node.left, node, ele)
        else:
            # 向右子树查找
            return self.find(node.right, node, ele)

    def delete(self, ele):
        flag, node, parent = self.find(self.root, self.root, ele)
        if not flag:
            print('此节点不存在')
            return False
        if not node.left and not node.right: # 叶节点
            node = None
        if node.left is None: # 左节点为空
            if node == parent.left:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.right is None: # 右节点为空
            if node == parent.left:
                parent.left = node.left
            else:
                parent.right = node.left
        else: # 左右节点均不为空，用右子树的最小值代替此节点，并将该值从右子树删除
            right_child = node.right
            if right_child.left is None: #右子树根节点无左子树，则右子树的根节点即为右子树的最小值
                node.val = right_child.val
                node.right = right_child.right
                del right_child
            else: #右子树根节点有左子树
                p = right_child.left
                while p.left is not None:
                    right_child = p
                    p = p.left
                node.val = p.val
                right_child.left = p.right
                del p

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


a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
bst = BST(a)  # 创建二叉查找树
print(bst.inorder(bst.root))
bst.delete(65)
print(bst.inorder(bst.root))