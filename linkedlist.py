#node in linked list consists of:
# 1-value of the node
# 2-pointer to the next node

class LinkedListNode:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode
        
        
node1=LinkedListNode("3")
node2=LinkedListNode("7")
node3=LinkedListNode("10")

node1.nextNode=node2 #node1 --> node2, "3" --> "7"
node2.nextNode=node3 #node2 --> node3, "7" --> "10"
#node1 --> node2 -->node3

currentNode=node1
while True:
    print(currentNode.value,"-->",end=" ")
    if currentNode.nextNode is None:
        print("None, end of the linked list")
        break
    currentNode=currentNode.nextNode
    
