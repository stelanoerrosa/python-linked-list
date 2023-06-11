class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self) :
        self.head = None

    # Menambahkan Elmen Linked List
    def add_to_front(self, data) :
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end (self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
            self.head = new_node        
        current = self.head
        while current.next :
            current = current.next
        current.next = new_node

    # Menghapus elmen LInked List
    def remove_front(self) :
        if self.head is None :
            return
        self.head = self.head.next

    def remove_end (self):
        if self.head is None:
            return

        current = self.head
        while current.next.next:
            current = current.next
        Current.next = None

    # Mencetak isi linked list
    def print_linked_list(self):
        current = self.head
        while current :
            print(current.data, end=" ")
            current = current.next
        print()

# Membuat dan mencetak Linked List
linked_list = LinkedList()

# Menambahkan elemen ke depan
linked_list.add_to_front(3)
linked_list.add_to_front(2)
linked_list.add_to_front(1)

# Menambahkan elemen ke akhir
linked_list.add_to_end(4)
linked_list.add_to_end(5)
linked_list.add_to_end(6)

linked_list.print_linked_list ( )