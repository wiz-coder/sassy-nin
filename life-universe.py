'''
Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely… rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.

Sample Input:
1
2
88
42
99
Sample Output:
1
2
88
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self,val):
        temp_node = Node(val)
        if self.head == None:
            self.head = temp_node
            self.tail = temp_node
        else:
           
           tail = self.tail
           tail.next = temp_node
           self.tail = temp_node
    def listTraversal(self):
        current_node = self.head
        while current_node:
            if current_node.data != 42:
                print(current_node.data)
                current_node = current_node.next
            else: break
            
def numList():
    s = SinglyLinkedList()
    while True:
        temp = input()
        if temp == "": break
        else: 
            s.addNode(int(temp))
    s.listTraversal()

numList()



