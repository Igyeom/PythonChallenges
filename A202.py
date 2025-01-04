class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push_front(head, data):
    node = Node(data)
    node.next = head
    return node

def traverse(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' > ')
        ptr = ptr.next
    print(None)


head = None
head = push_front(head, 6)
head = push_front(head, 5)
head = push_front(head, 4)
head = push_front(head, 3)
head = push_front(head, 2)
head = push_front(head, 1)
traverse(head)
