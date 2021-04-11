class balanced_tree :
    def insertTree(self,elements , lim):
        if not elements:
            return None

        root = balanced_tree(elements[0])

        for idx in range (1,len(elements)):
            root = self.insert(root,elements,lim)
        return self._move(root)

    def insert(self,node,key,lim):
        if not node:
            return Node(key)
        if (key < node.data):
            node.left = self.insert(node.left,key,lim)
        else: # key >data
            node.right = self.insert(node.right,key,lim)

        node.height = 1+max(self._height(node.left),self._height(node.right))
        balance = self._balance(node)

        if balance > lim:
            if self._balance(node.left) >= 0:
                node = self.right_rotate(node)
            else:
                node = self.left_right_rotate(node)
        elif balance < -lim:
            if self._balance(node.right):
                node = self.left_rotate(node)
            else:
                node = self.right_left_rotate(node)
        return node


    def right_rotate(self,node):
        left_temp = node.left

        node.left = left_temp.right
        left_temp.right = node

        node.height = 1 + max(self._height(node.left),self._height(node.right))
        left_temp.height = 1 + max(self._height(left_temp.left),self._height(left_temp.right))

        return left_temp

    def left_rotate(self,node):
        right_temp = node.right

        node.right = right_temp.left
        right_temp.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        right_temp.height = 1 + max(self._height(right_temp.left), self._height(right_temp.right))

        return right_temp

    def left_right_rotate(self,node):
        node.left = self.left_rotate(node.left)

        return self.right_rotate(node)

    def right_left_rotate(self,node):
        node.right = self.right_rotate(node.right)

        return self.left_rotate(node)

    def _balance(self,node):
        if not node:
            return 0

    def _height(self,node):
        if not node:
            return -1

        return node.height

    def _move(self,tree_node):
        if not tree_node:
            return None

        root = Tree_Node(tree_node.data)

        root.left = self._move(tree_node.left)
        root.right = self._move(tree_node.right)

        return root


class Node :
    def __init__(self,data):
        self.data = data
        self.height = 0
        self.right = None
        self.left = None


class Tree_Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left  = None






