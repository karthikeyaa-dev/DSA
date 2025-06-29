from abc import ABC, abstractmethod

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

#This is an abstract class to add the node 
class ADD_NODE(ABC):
    def __init__(self, linked_list):
        self.linked_list=linked_list
    
    @abstractmethod
    def add_node(self, data):
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

LL=LinkedList()
LL.add_node_begin(10)
LL.add_node_begin(20)
LL.add_node_begin(30)
LL.add_node_begin(40)
LL.add_node_end(50)
LL.add_node_end(60)
LL.add_node_end(70)
LL.add_node_end(80)
LL.print_linked_list()
