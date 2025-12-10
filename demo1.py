
str = 'Python'
print('str[0] str[-6] =', str[0], str[-6])
print('str[5] str[-1] =', str[5], str[-1])

l = ['d', 'b', 'a', 'f', 'd']
l.remove('d') #移除列表中某个值的首次匹配项
print(l)


import time
t = time.localtime()
print('t=', t)



class Cat:

    color = 'yellow'

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        self.__eat(food)    #私有方法只能通过其他普通方法访问
    
    def __eat(self, food):
        self.food = food
        print('%s is eating %s'%(self.name,self.food))


c = Cat('Tom') #给对象起名
print('c.name =', c.name)
c.eat('fish')
