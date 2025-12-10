class ListNode:
    def __init__(self,val):   #链表节点
        self.val = val
        self.next = None


def create_listnode(arr: list[int]) -> ListNode:    #创建链表(将数组转换为链表)
    if arr is None or len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

head = create_listnode([1,2,3,4,5])

new_node = ListNode(0)
new_node.next = head
head = new_node
p = head

while p is not None:
    print(p.val)
    p = p.next



