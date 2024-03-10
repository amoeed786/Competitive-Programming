class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addnumbers(l1,l2):
    dummy=ListNode()
    current=dummy
    carry=0
    while l1 or l2 or carry:
        val1=l1.val if l1 else 0
        val2=l2.val if l2 else 0
        totalsum=val1+val2+carry
        carry=totalsum//10
        current_digit = totalsum%10
        current.next=ListNode(current_digit)
        current=current.next
        if l1:
            l1=l1.next
        if l2:
            l2=l2.next
    return dummy.next


l1=ListNode(2, ListNode(4, ListNode(3)))
l2=ListNode(5, ListNode(6, ListNode(4)))
result = addnumbers(l1,l2)
while result:
    print(result.val)
    result=result.next
