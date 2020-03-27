
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
    def AddNode(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = Node(val)

    def printNode(self):
        while self.head :
            print(self.head.val,end=" ")
            self.head=self.head.next

    def removeDuplicates(self):
        dummy=curr=Node(0)
        head1=self.head
        dummy.next=head1
        while self.head and self.head.next:
            if self.head and self.head.next.val:
                while self.head and self.head.next and self.head.val==self.head.next.val   :
                    self.head=self.head.next
                self.head = self.head.next
                curr.next=self.head
            else :
                curr = curr.next
                self.head=self.head.next
        return dummy.next


myLL = LinkedList()
myLL.AddNode(1)
myLL.AddNode(1)
myLL.AddNode(3)
myLL.AddNode(4)
myLL.AddNode(4)
#myLL.printNode()
myLL.removeDuplicates()
myLL.printNode()


