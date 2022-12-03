# Implementasi Stack
class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            print("Tidak ada data di stack")
            return
        else:
            self.stack.pop()
    
    def print(self):
        for index in range(len(self.stack) - 1, -1, -1):
            print(self.stack[index])

stack_list = Stack()
stack_list.insert("Kerupuk 1")
stack_list.insert("Kerupuk 2")
stack_list.insert("Kerupuk 3")
stack_list.insert("Kerupuk 4")

stack_list.print()
print("== after call remove in stack ==")
stack_list.remove()
stack_list.print()