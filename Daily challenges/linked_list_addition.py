'''
Google: You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):

        rl1 = reverseLinkedList(l1)
        rl2 = reverseLinkedList(l2)

        len1 = countNodes(rl1)
        len2 = countNodes(rl2)

        sum = (convertReversedList(rl1, len1) +
              convertReversedList(rl2, len2))
        return sum

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def getVal(self):
        return self.val

    def getNextNode(self):
        return self.next

    def setVal(self, val):
        self.val = val

def raise2Power(index):
    x = pow(10, index)
    return x

def convertReversedList(list, len):
    sum = 0
    while(list):
        sum = sum + list.getVal() * raise2Power(len)
        list = list.next
        len = len - 1
    return sum

def reverseLinkedList(head):
    prev = None
    while(head is not None):
        temp = head # temporarily hold the head node
        head = head.next # make the head node the second node
        temp.next = prev # point temp's pointer (which is actually the head(!) and now needs to point at None)
        prev = temp # make prev the new head node
    return prev # return this because its the new head!

# Utility functions
def countNodes(list):
    count = 0
    while(list):
        count = count + 1
        list = list.next
    return count - 1

def printLinkedList(list):
    while(list is not None):
        print(list.getVal())
        list = list.getNextNode()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = ListNode(1)
l3.next = ListNode(2)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8
