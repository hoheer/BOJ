import sys


# node : class, a single element of list
# doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# linked list, node and list is diff
class Link:
    # init head and tail with None data
    def __init__(self):
        self.head = Node(None)
        self.head.next = Node(None)
        self.head.prev = None
        self.cnt: int = 0
        self.tail = self.head.next
        self.tail.prev = self.head

    def print_list(self):
        curl = self.head
        temp = []
        while curl.next is not self.tail:
            curl = curl.next
            temp.append(curl.data)
        return temp

    def insert(self, cur, data):
        new = Node(data)
        cursor = cur.prev
        cursor.next = new
        cur.prev = new
        new.prev = cursor
        new.next = cur
        self.cnt += 1
        return cur

    def remove(self, cur):
        prv = cur.prev.prev
        cur.prev.prev.next = cur
        cur.prev = cur.prev.prev
        self.cnt -= 1
        if prv is self.head:
            return self.head.next
        else:
            return cur


answers = []
cases = int(sys.stdin.readline().rstrip())
while cases > 0:
    answer = Link()
    cases -= 1
    stc = sys.stdin.readline().rstrip()
    # init cursor to tail
    curl_node = answer.head.next
    for c in stc:
        if c == '<':
            # if cursor on head
            if curl_node.prev == answer.head:
                continue
            else:
                curl_node = curl_node.prev
        elif c == '>':
            # if cursor on tail
            if curl_node == answer.tail:
                continue
            else:
                curl_node = curl_node.next
        elif c == '-':
            if answer.cnt == 0 or curl_node.prev == answer.head:
                continue
            else:
                curl_node = answer.remove(curl_node)
        else:
            curl_node = answer.insert(curl_node, c)
    answers.append(answer.print_list())
for stc in answers:
    sys.stdout.write(''.join(stc)+'\n')
