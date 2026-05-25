import string
class Student:
    name:string
    chinese:int
    math:int
    english:int
    def get_total(self):
        return self.chinese + self.math + self.english

    def get_avg(self):
        return self.get_total() / 3

stu=Student()
stu.name=input("请输入姓名")
stu.chinese=int(input("请输入语文成绩"))
stu.math=int(input("请输入数学成绩"))
stu.english=int(input("请输入英语成绩"))
print(f"总分{stu.get_total()}")
if stu.get_total()>=180:
    print(f"及格了 平均分是{stu.get_avg()}")
else:
    print(f"拉完了 平均分是{stu.get_avg()}")