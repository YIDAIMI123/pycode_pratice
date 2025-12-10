
class student:
    def __init__(self,name,student_id,age):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grades = {"语文":0,"数学":0,"英语":0}
    
    def p(self):
        print(f"姓名:{self.name},学号:{self.student_id},年龄:{self.age},成绩:{self.grades}")


s1 = student("张三","001",18)
s1.grades["语文"] = 666666  
s1.grades["数学"] = 123456
s1.grades["英语"] = 666
s1.p()



