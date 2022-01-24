import sys


class Node:
    def __init__(self, num):
        self.prev = None
        self.next = None
        self.data = num


class Link:
    def __init__(self, nums):
        self.head = Node(nums[0])
        self.tail = None
        self.cnt = 0

    def push(self, nums):
        curl = self.head
        for x in range(1,len(nums)-1):
            new = Node(nums[x])
            curl.next = new
            new.prev = curl
            curl = curl.next
        tail = Node(nums[len(nums)-1])
        tail.next = self.head
        self.head.prev = tail
        curl.next = tail
        tail.prev = curl
        self.tail = tail
        self.cnt = len(nums)


    def print(self):
        curl = self.head
        while curl is not self.tail:
            print(curl.data)
            curl = curl.next

    def kill(self, num, answer, cur):
        curl = cur
        while num-1 > 0:
            num -= 1
            curl = curl.next
        prv = curl.prev
        nxt = curl.next
        curl.prev.next = nxt
        curl.next.prev = prv
        answer.append(curl.data)
        self.cnt -= 1
        return nxt


answer = []
n, k = map(int, sys.stdin.readline().rstrip().split(' '))
lst = [x for x in range(1,n+1)]
people = Link(lst)
people.push(lst)
cur = people.head
while people.cnt > 0:
    cur = people.kill(k, answer, cur)
y = ''
for n in answer:
    y += str(n) +', '
y = y.rstrip()
y = y[:-1]
print("<"+y+">")


