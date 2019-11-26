# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        mid = self.getMidVal(head)
        left = head
        right = mid.next
        mid.next = None
        return self.merge(self.sortList(left), self.sortList(right))
    
    def merge(self,left,right):
        TempNode = ListNode(0)
        temp = TempNode
        
        while left is not None and right is not None:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
                
            temp = temp.next
            
        if left is not None:
            temp.next = left
            
        if right is not None:
            temp.next = right
            
        return TempNode.next
        
    def getMidVal(self, node):
        if node is None or node.next is None:
            return node
        
        fast = slow = node
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow