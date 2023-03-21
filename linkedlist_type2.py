#node in linked list consists of:
# 1-value of the node
# 2-pointer to the next node

class LinkedListNode:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode
    
#In the interview, they only will give you the head when they ask you about the linked list
class LinkefList:
    def __init__(self,head=None):
        self.head=head
        
    def insert(self,value):
        node=LinkedListNode(value)
        if self.head is None:
            self.head=node
            return
        
        currentNode=self.head
        
        while True:
            if currentNode.nextNode is None: #If there is no node after the current node that we are at
                currentNode.nextNode=node #if we are at the tail, we insert the element at the tail
                break
            currentNode=currentNode.nextNode 
            
    def printLinkedList(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.value," --> ",end="")
            currentNode=currentNode.nextNode
            
        print("None")
        
ll=LinkefList()
ll.printLinkedList()
ll.insert("3")
ll.insert("44")
ll.insert("12")
ll.printLinkedList()
