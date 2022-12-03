# Implementasi Queue
class Queue:
    def __init__(self):
        self.queue = list()

    def insert(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop()
            return 
        print("Tidak ada queue saat ini")
        
    
    def size(self):
        print(len(self.queue))

    def print(self):
        print(self.queue)

queue_list = Queue()
queue_list.insert("Person1")
queue_list.insert("Person2")
queue_list.insert("Person3")
print("== list queue ==")
queue_list.print()
print("== list queue after remove ==")
queue_list.remove()
queue_list.print()
