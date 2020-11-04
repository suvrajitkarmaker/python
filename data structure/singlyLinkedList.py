class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert(self, nodeAddress):
        if(self.head == None):
            self.head = nodeAddress
            self.tail = nodeAddress
        else:
            self.tail.next = nodeAddress
            self.tail = self.tail.next 
        
        self.length = self.length + 1

    def insertAtAnyPosition(self, nodeAddress, position):
        if(position == 0):
            nodeAddress.next = self.head
            self.head = nodeAddress
        else:
            current = self.head
            previous = None
            count =0
            while(count<position and count<self.length):
                previous = current
                current = current.next
                count+=1
            
            previous.next = nodeAddress
            nodeAddress.next = current
        
        self.length = self.length + 1


    def search(self, value):
        current = self.head
        while(current != None):
            if(current.data == value):
                return True
            current = current.next
        return False
    def deleteByPosition(self, position):
        if(position>self.length):
            print("Invalid position")
            return

        current = self.head
        previous = None

        if(position==0 and self.length>0):
            self.head = self.head.next
        else:
            index = 0
            while(index < self.length):
                if(index == position):
                    previous.next = current.next
                    break
                
                previous = current
                current = current.next
                index+=1

    def printList(self):
        current = self.head
        while(current != None):
            print(current.data)
            current = current.next
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

li = LinkedList()
li.insert(Node(30))
li.insert(Node(56))
li.insert(Node(20))
li.insert(Node(565))
li.insert(Node(205))

li.printList()
#0 based position
li.insertAtAnyPosition(Node(55), 1)
print("****************--------------************")
li.printList()
