from concurrent.futures import ThreadPoolExecutor
import time
 
# 定义一个任务函数
def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    return f"Task {n} completed"
 
# 创建 ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:  # 控制线程池大小为3
    # 提交任务给线程池
    future1 = executor.submit(task, 1)
    future2 = executor.submit(task, 2)
    future3 = executor.submit(task, 3)
 
    # 获取任务执行结果
    print(future1.result())
    print(future2.result())
    print(future3.result())