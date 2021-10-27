class Node :
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None

    def insert(self, node):
        if self.key > node.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif self.key <= node.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.inorder()

class Tree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root is not None:
            self.root.inorder()

    def add(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

tree = Tree()

input_list = input('Enter the list of numbers: ').split()
input_list = [int(x) for x in input_list]
for x in input_list:
    tree.add(x)
print('Sorted list: ', end='')
tree.inorder()