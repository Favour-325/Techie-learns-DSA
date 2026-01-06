class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start of the list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, target_value, new_value):
        # Target found -> Rewire pointers
        # You don't know the target is missing until you fall off the list

        new_node = Node(new_value)
        
        # Empty list -> Do nothing
        if not self.head:
            return False
        
        current = self.head
        while current.data != target_value:
            current = current.next

            # Target not found -> Do nothing
            if not current:
                return False

        prev_next = current.next # Preserve the next reference
        current.next = new_node # Append the new node

        new_node.next = prev_next # Reconnect list

    def delete(self, value):
        if not self.head:
            return False
        
        current = self.head

        # Deleting the head node
        if current.data == value:
            self.head = current.next

            current = self.head
            return

        while current.next.data != value: 
            current = current.next

            # Target not found -> Do nothing
            if not current.next:
                return False
        
        target = current.next

        current.next = target.next

        # So ultimately, deleting a node from a linked list is just breaking the link between that node and the other ones in the list and reforming the chain with the rest.
        

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    link = LinkedList()

    link.append('a')
    link.append('b')
    link.append('d')
    link.display()

    link.insert_after('c', 'd')
    link.display()

    link.delete('e')

    link.display()

    

if __name__ == "__main__":
    main()