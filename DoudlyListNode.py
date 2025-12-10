class DoudlyListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

def create_doudly_listnode(arr: list[int]) -> DoudlyListNode:
    if arr is None or len(arr) == 0:
        return None

    head = DoudlyListNode(arr[0])
    cur = head
    for i in arr[1:]:
        new_node = DoudlyListNode(i)
        cur.next = new_node
        new_node.prev = cur
        cur = cur.next

    return head

head = create_doudly_listnode([1,2,3,4,5])
p = head
while p:
    print(p.val)
    tail = p
    p = p.next