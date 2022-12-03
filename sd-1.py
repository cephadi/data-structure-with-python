# Implementasi Linked List - Single Node

class LKNode:
    def __init__(self, data=None):
        self.data = data
        self.nextaddress = None

class ListNode:
    def __init__(self):
        self.head = None

    def print(self):
        node_value = self.head
        while node_value is not None:
            print(node_value.data)
            node_value = node_value.nextaddress
    
    def insertInHead(self, new_data):
        tmp_data = LKNode(new_data)
        tmp_data.nextaddress = self.head
        self.head = tmp_data
    
    def insertInTail(self, new_data):
        tmp_data = LKNode(new_data)
        if self.head is None:
            self.head = tmp_data
            return
        
        last_node = self.head
        while (last_node.nextaddress):
            last_node = last_node.nextaddress
        last_node.nextaddress = tmp_data

    def insertBetween(self, mid_node, new_data):
        if mid_node is None:
            print("Node tidak ditemukan")
            return

        tmp_data = LKNode(new_data)
        tmp_data.nextaddress = mid_node.nextaddress
        mid_node.nextaddress = tmp_data

    def remove(self, key_data):
        tmp_head = self.head

        if tmp_head is not None:
            if tmp_head.data == key_data:
                self.head = tmp_head.nextaddress
                tmp_head = None
                return
        
        while tmp_head is not None:
            if tmp_head.data == key_data:
                break
            prev_node = tmp_head
            tmp_head = tmp_head.nextaddress
        
        if tmp_head == None:
            return
        
        prev_node.nextaddress = tmp_head.nextaddress
        tmp_head = None

linked_list = ListNode()
linked_list.head = LKNode("Gerbong 1")

grb2 = LKNode("Gerbong 2")
grb3 = LKNode("Gerbong 3")

# sambungkan G1 dengan G2
linked_list.head.nextaddress = grb2

# sambungkan G2 dengan G3
grb2.nextaddress = grb3

linked_list.print()
print("== after insert in head ==")
linked_list.insertInHead("Gerbong 4")
linked_list.print()
print("== after insert in tail ==")
linked_list.insertInTail("Gerbong 5")
linked_list.insertInTail("Gerbong 6")
linked_list.print()
print("== after insert in between G3 ==")
linked_list.insertBetween(linked_list.head.nextaddress.nextaddress.nextaddress, "Gerbong 7")
linked_list.print()
print("== after remove G3 ==")
linked_list.remove("Gerbong 3")
linked_list.print()