class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

def addTwoNumbers(l1, l2):
    num1 = 0
    k = 0
    while l1.next is not None:
        num1 += l1.val*(10**k)
        l1 = l1.next
        k += 1
    num1+=l1.val*(10**k)
    num2 = 0
    k = 0
    while l2.next is not None:
        num2 += l2.val*(10**k)
        l2 = l2.next
        k += 1
    num2 += l2.val * (10 ** k)
    num1 = int(str(num1)[::-1])
    num2 = int(str(num2)[::-1])
    num = num1 + num2
    num = list(map(int, str(num)))
    L = ListNode()
    l = ListNode()
    for i in range(len(num)-2):
        v = num[i]
        L.val = v
        l.next = L
        l.val = num[i+1]
        L.next = l

    L.val = num[-1]

    return l









result = addTwoNumbers(l1, l2)
while result.next is not None:
    print(result.val)
    result = result.next
print(result.val)
