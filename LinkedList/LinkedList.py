from abc import ABC, abstractmethod

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_linked_list(self):
        tem=self.head
        while tem!=None:
            print(tem.data, end="->")
            tem=tem.next
        print("None")

#This is an abstract class to add the node 
class ADD_NODE(ABC):
    def __init__(self, linked_list):
        self.linked_list=linked_list
    
    @abstractmethod
    def add_node(self,*args, **kwargs):
        pass

#This adds node at the begin 
class ADD_NODE_BEGIN(ADD_NODE):
    def add_node(self, data):
        if self.linked_list.head==None:
            new_node=Node(data)
            self.linked_list.head=new_node
        else:
            new_node=Node(data)
            new_node.next=self.linked_list.head
            self.linked_list.head=new_node
        
#this adds node at the end
class ADD_NODE_END(ADD_NODE):
    def add_node(self, data):
        if self.linked_list.head==None:
            new_node=Node(data)
            self.linked_list.head=new_node  
        else:
            tem=self.linked_list.head
            while tem.next!=None:
                tem=tem.next
            new_node=Node(data)
            tem.next=new_node         

#Adding Node after given X
class ADD_NODE_AFTER_X(ADD_NODE):
    def add_node(self, data, x):
        tem = self.linked_list.head
        while tem is not None:
            if tem.data == x:
                new_node = Node(data)
                new_node.next = tem.next
                tem.next = new_node
                return 
            tem = tem.next

#Adding node before given x
class ADD_NODE_BEFORE_X(ADD_NODE):
    def add_node(self, data, x):
        if self.linked_list.head==None:
            return "List is empty you cannot insert"
        if self.linked_list.head.data==x:
            new_node=Node(data)
            new_node.next=self.linked_list.head
            self.linked_list.head=new_node
            return
        tem=self.linked_list.head
        while tem.next != None:
            if tem.next.data==x:
                new_node = Node(data)
                new_node.next = tem.next
                tem.next = new_node
                return
            tem=tem.next

#This is an abstract class to delete the node 
class DELETE_NODE(ABC):
    def __init__(self, linked_list):
        self.linked_list=linked_list
    @abstractmethod
    def delete_node(self, *args, **kwargs):
        pass

#This delets the node at the begin 
class DELETE_NODE_AT_BEGIN(DELETE_NODE):
    def delete_node(self):
        if self.linked_list.head==None:
            return "The LinkedList is empty"
        elif self.linked_list.head.next==None:
            self.linked_list.head=None
        else:
            tem=self.linked_list.head
            self.linked_list.head=tem.next
            tem=None

#this deletes node at the end
class DELETE_NODE_AT_END(DELETE_NODE):
    def delete_node(self, *args, **kwargs):
        if self.linked_list.head==None:
            return "The LinkedList is empty"
        elif self.linked_list.head.next==None:
            self.linked_list.head=None
        else:
            tem=self.linked_list.head
            while tem.next.next!=None:
                tem=tem.next
            tem.next=None

#this delete the node at the x position
class DELETE_NODE_AT_X(DELETE_NODE):
    def delete_node(self, x):
        if self.linked_list.head==None:
            return "List is empty to delete"
        elif self.linked_list.head.data==x:
            self.linked_list.head=self.linked_list.head.next
        else:
            tem=self.linked_list.head
            while tem.next!=None:
                if tem.next.data==x:
                    tem.next=tem.next.next
                tem=tem.next


LL=LinkedList()

add_begin=ADD_NODE_BEGIN(LL)
add_end=ADD_NODE_END(LL)
add_after_x=ADD_NODE_AFTER_X(LL)
add_before_x=ADD_NODE_BEFORE_X(LL)

delete_begin=DELETE_NODE_AT_BEGIN(LL)
delete_end=DELETE_NODE_AT_END(LL)
delete_node_at_x=DELETE_NODE_AT_X(LL)

add_begin.add_node(30)
add_begin.add_node(20)
add_begin.add_node(10)

add_end.add_node(40)
add_end.add_node(50)
add_end.add_node(60)

add_after_x.add_node(70,60)
add_after_x.add_node(90,70)

add_before_x.add_node(80,90)

LL.print_linked_list()