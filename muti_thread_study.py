import threading
import requests
import os
 
# 虚拟文件URL列表
file_urls = [
    "https://www.example.com/file1.txt",
    "https://www.example.com/file2.txt",
    "https://www.example.com/file3.txt"
]
 
# 下载函数
def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {url} and saved to {save_path}")
 
# 下载器类
class DownloaderThread(threading.Thread):   #DownloaderThread继承Thread线程类
    def __init__(self, url, save_path):
        threading.Thread.__init__(self) #这里是显式调用Thread的构造方法(Thread这里是父类)
        self.url = url
        self.save_path = save_path
 
    def run(self):
        download_file(self.url, self.save_path)
 
# 创建保存文件的目录
download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)    #makedirs()创建多级目录
 
# 创建并启动多个下载线程
threads = []
for i, url in enumerate(file_urls): #enumerate()这个函数作用是，把一个可迭代对象包装成一个带编号的新迭代器，（enumerate(iterable, start=0)  start 表示编号从几开始，默认 0，这里的i就是编号）
    file_name = f"file{i+1}.txt"
    save_path = os.path.join(download_dir, file_name)   #os.path.join()将一个或多个 path（文件或目录） 进行拼接
    downloader = DownloaderThread(url, save_path)   #创建一个线程对象
    threads.append(downloader)  #将线程对象添加到线程列表中
    downloader.start()  #启动线程
 
# 等待所有线程完成下载
for thread in threads:
    thread.join()
 
print("All downloads completed!")