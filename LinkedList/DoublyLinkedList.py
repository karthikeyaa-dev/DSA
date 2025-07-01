from abc import ABC, abstractmethod

class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def print_doubly_linked_list(self)->None:
        tem=self.head
        while tem.data!=None:
            print(tem.data, end="->")
        tem=tem.next
    
    def print_doubly_linked_list_in_reverse(self)->None:
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
    def add_node(self, data)->None:
        tem=self.linked_list.head
        while tem.next!=None:
            tem=tem.next
        new_node=Node(data)
        tem.next=new_node
        new_node.prev=tem

class ADD_NODE_BEGIN(ADD_NODE):
    def add_node(self, data)->None:
        new_node=Node(data)
        if self.linked_list.head==None:
            self.linked_list.head=new_node
        else:
            new_node.next=self.linked_list.head
            self.linked_list.head.prev=new_node
            self.linked_list.head=new_node


class ADD_NODE_AFTER_X(ADD_NODE):
    def add_node(self,x, data) ->None:
        new_node=Node(data)
        tem=self.linked_list.head
        while tem!=None:
            if tem.data==x:
                break
            tem=tem.next
        if tem==None:
            return "we cannot add any node"
        new_node.next=tem.next
        new_node.prev=tem
        tem.next=new_node

        if new_node!=None:
            new_node.next.prev=new_node

class ADD_NODE_BEFORE_X(ADD_NODE):
    def add_node(self,x, data)->None:
        new_node=Node(data)
        tem=self.linked_list.head
        if tem==None:
            return "That the list is empty"
        if tem.data==x:
            new_node.next=tem
            tem.prev=new_node
            self.linked_list.head=new_node
        while tem.next!=None:
            if tem.data==x:
                break
            tem=tem.next
        if tem is None:
            return "Value not found in the list"
        new_node.prev=tem.prev
        new_node.next=tem
        tem.prev.next=new_node
        tem.prev=new_node

class DELETE_NODE(ABC):
    def __init__(self, linked_list):
        self.linked_list=linked_list
    
    def delete_node(self, *args, **kwargs):
        pass

class DELETE_NODE_BEGIN(DELETE_NODE):
    def delete_node(self, *args, **kwargs)->None:
        head = self.linked_list.head
        if head is None:
            return "The list is empty"
        if head.next is None:
            self.linked_list.head = None
            return
        self.linked_list.head = head.next
        self.linked_list.head.prev = None

        