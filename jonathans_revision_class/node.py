class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # new_node = Node()
    # print(new_node.value)

    # new_link = LinkedList()
    # print(new_link.head)
    # print(new_link.tail)
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


lst = LinkedList()
lst.prepend(9)
lst.prepend(5)
lst.prepend(6)
print(lst.head.value)


