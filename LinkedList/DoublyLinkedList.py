from abc import ABC, abstractmethod

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_doubly_linked_list(self) -> None:
        tem = self.head
        while tem is not None:
            print(tem.data, end=" <-> ")
            tem = tem.next
        print("None")

    def print_doubly_linked_list_in_reverse(self) -> None:
        tem = self.head
        if tem is None:
            print("List is empty")
            return
        # Move to tail
        while tem.next is not None:
            tem = tem.next
        # Print in reverse
        while tem is not None:
            print(tem.data, end=" <-> ")
            tem = tem.prev
        print("None")

# Abstract base class for adding nodes
class ADD_NODE(ABC):
    def __init__(self, linked_list):
        self.linked_list = linked_list

    @abstractmethod
    def add_node(self, *args, **kwargs):
        pass

class ADD_NODE_BEGIN(ADD_NODE):
    def add_node(self, data) -> None:
        new_node = Node(data)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
        else:
            new_node.next = self.linked_list.head
            self.linked_list.head.prev = new_node
            self.linked_list.head = new_node

class ADD_NODE_END(ADD_NODE):
    def add_node(self, data) -> None:
        new_node = Node(data)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            return
        tem = self.linked_list.head
        while tem.next is not None:
            tem = tem.next
        tem.next = new_node
        new_node.prev = tem

class ADD_NODE_AFTER_X(ADD_NODE):
    def add_node(self, x, data) -> None:
        new_node = Node(data)
        tem = self.linked_list.head
        while tem is not None:
            if tem.data == x:
                break
            tem = tem.next
        if tem is None:
            print("Value not found")
            return
        new_node.next = tem.next
        new_node.prev = tem
        tem.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node

class ADD_NODE_BEFORE_X(ADD_NODE):
    def add_node(self, x, data) -> None:
        new_node = Node(data)
        tem = self.linked_list.head
        if tem is None:
            print("The list is empty")
            return
        if tem.data == x:
            new_node.next = tem
            tem.prev = new_node
            self.linked_list.head = new_node
            return
        while tem is not None:
            if tem.data == x:
                break
            tem = tem.next
        if tem is None:
            print("Value not found in the list")
            return
        new_node.prev = tem.prev
        new_node.next = tem
        tem.prev.next = new_node
        tem.prev = new_node

# Abstract base class for deleting nodes
class DELETE_NODE(ABC):
    def __init__(self, linked_list):
        self.linked_list = linked_list

    @abstractmethod
    def delete_node(self, *args, **kwargs):
        pass

class DELETE_NODE_BEGIN(DELETE_NODE):
    def delete_node(self, *args, **kwargs) -> None:
        head = self.linked_list.head
        if head is None:
            print("The list is empty")
            return
        if head.next is None:
            self.linked_list.head = None
            return
        self.linked_list.head = head.next
        self.linked_list.head.prev = None

class DELETE_NODE_END(DELETE_NODE):
    def delete_node(self, *args, **kwargs) -> None:
        head = self.linked_list.head
        if head is None:
            print("There is nothing to delete")
            return
        if head.next is None:
            self.linked_list.head = None
            return
        while head.next is not None:
            head = head.next
        head.prev.next = None

class DELETE_NODE_AFTER_X(DELETE_NODE):
    def delete_node(self, x) -> None:
        head = self.linked_list.head
        if head is None:
            print("There is nothing to delete")
            return
        current = head
        while current is not None:
            if current.data == x:
                break
            current = current.next
        if current is None:
            print(f"Node with value {x} not found")
            return
        if current.next is None:
            print(f"There is no node after {x} to delete")
            return
        node_to_delete = current.next
        current.next = node_to_delete.next
        if node_to_delete.next is not None:
            node_to_delete.next.prev = current
        print(f"Deleted node after {x}")

class DELETE_NODE_BEFORE_X(DELETE_NODE):
    def delete_node(self, x) -> None:
        head = self.linked_list.head
        if head is None:
            print("There is nothing to delete")
            return
        if head.data == x:
            print("No node exists before the head to delete")
            return
        elif head.next and head.next.data == x:
            self.linked_list.head = head.next
            self.linked_list.head.prev = None
            print(f"Deleted node before {x} (was head)")
            return
        current = head
        while current.next and current.next.next:
            if current.next.next.data == x:
                to_delete = current.next
                current.next = to_delete.next
                if to_delete.next:
                    to_delete.next.prev = current
                print(f"Deleted node before {x}")
                return
            current = current.next
        print(f"No node found before {x} to delete")

class DELETE_NODE_X(DELETE_NODE):
    def delete_node(self, x) -> None:
        head = self.linked_list.head
        if head is None:
            print("The list is empty")
            return
        if head.data == x:
            self.linked_list.head = head.next
            if self.linked_list.head:
                self.linked_list.head.prev = None
            print(f"Deleted node with value {x} (was head)")
            return
        while head is not None:
            if head.data == x:
                break
            head = head.next
        if head is None:
            print(f"No node found with value {x}")
            return
        if head.prev:
            head.prev.next = head.next
        if head.next:
            head.next.prev = head.prev
        print(f"Deleted node with value {x}")


LL=DoublyLinkedList()

add_node_begin=ADD_NODE_BEGIN(LL)
add_node_end=ADD_NODE_END(LL)
add_node_after_x=ADD_NODE_AFTER_X(LL)
add_node_before_x=ADD_NODE_BEFORE_X(LL)

add_node_begin.add_node(40)
add_node_begin.add_node(30)
add_node_begin.add_node(20)
add_node_begin.add_node(10)

add_node_end.add_node(50)
add_node_end.add_node(60)
add_node_end.add_node(70)
add_node_end.add_node(80)

add_node_after_x.add_node(80,90)
add_node_after_x.add_node(90,100)
add_node_after_x.add_node(100,110)
add_node_after_x.add_node(110,120)

LL.print_doubly_linked_list()
LL.print_doubly_linked_list_in_reverse()