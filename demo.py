class Employee:
    def __init__(self,name,work_id):
        self.name = name
        self.work_id = work_id

    def print_info(self):
        print(f"姓名:{self.name},工号:{self.work_id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, work_id, month_salary):
        super().__init__(name, work_id)
        self.month_salary = month_salary

        def calculate_monthly_pay(self):
            return self.month_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, work_id, daliy_salary, work_days):
        super().__init__(name, work_id)
        self.daliy_salary = daliy_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daliy_salary * self.work_days
    

zhangsan = FullTimeEmployee("张三","001",15000)
lisi = PartTimeEmployee("李四","002",300,20)

lisi.print_info()
print(lisi.calculate_monthly_pay())

