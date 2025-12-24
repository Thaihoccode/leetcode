# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        nho = 0  #bien nho neu >10
        # 2. Lặp khi còn số trong l1, l2 hoặc vẫn còn số nhớ
        while l1 or l2 or nho:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # Tinh tong
            tong = v1 + v2 + nho
            nho = tong // 10    
            gia_tri = tong % 10
            #Tao nut moi
            curr.next = ListNode(gia_tri)
            #chuyen con tro den nut tiep theo
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        # 4. tra ve ket qua sau nut gia
        return dummy.next