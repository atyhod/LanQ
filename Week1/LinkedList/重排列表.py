'''
一个包含 n
 个元素的线性链表 L=(a1,a2,…,an-2,an-1,an)
。

现在要对其中的结点进行重新排序，得到一个新链表 L'=(a1,an,a2,an-1,a3,an-2…)

样例1:
输入:1->2->3->4

输出:1->4->2->3
样例2:
输入:1->2->3->4->5

输出:1->5->2->4->3
数据范围
1≤n≤1000
,
1≤ai≤10000
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rearrangedList(self, node):
        """
        :type node: ListNode
        :rtype: void 
        """
        #TODO
        if not node or not node.next:
            return
        slow = node
        fast = node.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow
        
        fir = mid.next
        mid.next = None
        sec = fir.next
        fir.next = None
        while sec.next:
            tem = sec.next
            sec.next = fir
            fir = sec
            sec = tem
        sec.next = fir
        
        head1 = node
        head2 = sec
        while head1.next:
            tem1 = head1.next
            tem2 = head2.next
            head1.next = head2
            head2.next = tem1
            head1 = tem1
            head2 = tem2
        head1.next = head2