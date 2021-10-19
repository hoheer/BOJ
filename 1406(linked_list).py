import sys


# node : class, a single element of list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# linked list, node and list is diff
class Link:
    def __init__(self):
        self.head = Node(None)
        self.head.next = Node(None)
        self.head.prev = None
        self.cnt: int = 0
        self.tail = self.head.next
        self.tail.prev = self.head

    # add node to end of list
    # if head is none, then add to head, after head is fill, tail will be target
    # change tail as new node and add nonetype node for tail
    def append(self, data):
        curl: Node = self.tail
        curl.data = data
        self.tail.next = Node(None)
        self.tail = self.tail.next
        self.tail.prev = curl

        self.cnt += 1

    # delete end of node at list
    # def delete(self):
    #     curl = self.head
    #     while curl.next.next is not None:
    #         curl = curl.next
    #     curl.next = None
    #
    #     self.cnt -= 1

    def print_list(self):
        curl = self.head
        answer = []
        while curl.next is not None:
            curl = curl.next
            if curl.data is None:
                break
            answer.append(curl.data)
        print(''.join(answer))

    def insert(self, curl, data):
        prev = curl.prev
        nxt = curl.next
        new = Node(data)
        curl.next = new
        new.next = nxt
        nxt.prev = new
        new.prev = curl
        self.cnt += 1
        return new

    def remove(self, curl):
        prv = curl.prev
        nxt = curl.next
        prv.next = nxt
        nxt.prev = prv
        self.cnt -= 1
        return prv

    def select(self, idx):
        curl = self.head
        while idx > 0:
            idx -= 1
            curl = curl.next
        return curl


# curl node indicate prev node
stc: str = sys.stdin.readline().rstrip()
order_cnt = int(input())

lst = Link()
for c in stc:
    lst.append(c)

cursor = len(stc)
curl_node = lst.select(cursor)

while order_cnt > 0:
    order_cnt -= 1
    order = list(sys.stdin.readline().rstrip().split(' '))

    if order[0] == 'L':
        if cursor == 0:
            continue
        cursor -= 1
        curl_node = curl_node.prev

    elif order[0] == 'D':
        if cursor == lst.cnt:
            continue
        cursor += 1
        curl_node = curl_node.next

    elif order[0] == 'B':
        if cursor == 0:
            continue
        else:
            curl_node = lst.remove(curl_node)
            cursor -= 1

    elif order[0] == 'P':
        curl_node = lst.insert(curl_node, order[1])
        cursor += 1


lst.print_list()








