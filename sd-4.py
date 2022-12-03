# Implementasi Tree
class TNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, new_data):
        if self.data:
            if new_data < self.data:
                if self.left is None:
                    self.left = TNode(new_data)
                else:
                    self.left.insert(new_data)
                
            elif new_data > self.data:
                if self.right is None:
                    self.right = TNode(new_data)
                else:
                    self.right.insert(new_data)
        else:
            self.data = new_data

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

root_tree = TNode(14)
root_tree.insert(9)
root_tree.insert(7)
root_tree.insert(16)
root_tree.print()