from collections import deque

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def say_hello(name):    #这里等价于 say_hello = decorator(say_hello)，当调用 say_hello("Alice") 时，实际上执行的是装饰器返回的 wrapper 函数，它在原始函数执行前后添加了额外的功能。
    print(f"Hello, {name}!")

say_hello("Alice")
