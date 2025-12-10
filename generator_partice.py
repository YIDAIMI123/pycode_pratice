# def squre_numbers(num: list[int]):
#     squred_nums = []
#     for i in num:
#         squred_nums.append(i * i)
#     return squred_nums

# nums= [1,2,3,4,5]
# squred_nums = squre_numbers(nums)
# print(squred_nums)



def squre_numbers(num: list[int]):
    for i in num:   
        yield i * i #将这个函数转换成生成器的关键在于，不需要将运算结果存入squred_nums列表里(如果存入列表中，数据量大的时候会爆内存，毕竟列表会存放在内存中)，取而代之的是使用yield关键字

nums= [1,2,3,4,5]
squred_nums = squre_numbers(nums)
print(squred_nums)  #运行结果是一个生成器对象，此时还未进行任何计算
print(next(squred_nums))    #需要用next()函数来获取下一个计算结果

for i in squred_nums:   #也可以使用for循环来获取所有的计算结果
    print(i)