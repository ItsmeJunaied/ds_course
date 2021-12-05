class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def search(self,x):
        pss=0
        i=0
        current = self.head
        while current!= None:

            if current.data == x:
                pss+=1
                return True


            i=i+1#pss+=1
            current=current.next

            print("is found at index,", i)

a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end='')
a_llist.display()
a_llist.search(4)
a_llist.display()



