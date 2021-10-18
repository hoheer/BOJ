import sys


# node : class, a single element of list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list, node and list is diff
class Link:
    def __init__(self, data):
        self.head = None
        self.tail = None

    # add node to end of list
    # if head is none, then add to head, after head is fill, tail will be target
    def append(self, data):
        if self.head is None:
            head = Node(data)
            self.tail = head
        else:
            self.tail.next = Node(data)
            tmp = self.tail.next
            self.tail = tmp

    #delete end of node at list
    def delete(self):






str = sys.stdin.readline().rstrip()
cnt = int(input())
orders = []

while cnt > 0:
    order = sys.stdin.readline().rstrip()
    orders.append(order)

    if order[0] == 'P':
        print(order[2])
    cnt -= 1

    ls = link('head')
    for c in str:
        ls.append(c)

    ls.print_all()





# print(orders)