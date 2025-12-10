from collections import deque   #双端队列

lst = deque([1, 2, 3, 4, 5])

print(len(lst))
lst.append(6)   #尾部插入数据



lst.appendleft(0) #头部插入数据

lst.insert(3, 2.5)  #在索引3的位置插入数据2.5


print(lst)