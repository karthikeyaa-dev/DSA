from abc import ABC, abstractmethod

class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def print_doubly_linked_list(self):
        tem=self.head
        while tem.data!=None:
            print(tem.data, end="->")
        tem=tem.next
    
    def print_doubly_linked_list_in_reverse(self):
        tem=self.head
        while tem.next!=None:
            tem=tem.next
        while tem.prev!=None:
            tem=tem.prev

class ADD_NODE(ABC):
    def __init__(self, linked_list):
        self.linked_list=linked_list

    @abstractmethod
    def add_node(self,data):
        pass

class ADD_NODE_END(ADD_NODE):
    def add_node(self, data):
        tem=self.linked_list.head
        while tem.next!=None:
            tem=tem.next
        new_node=Node(data)
        tem.next=new_node
        new_node.prev=tem

class ADD_NODE_BEGIN(ADD_NODE):
    def add_node(self, data):
        new_node=Node(data)
        if self.linked_list.head==None:
            self.linked_list.head=new_node
        else:
            new_node.next=self.linked_list.head
            self.linked_list.head.prev=new_node
            self.linked_list.head=new_node


