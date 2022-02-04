class Student:
    def __init__(self): # 初始化
        self.x = 5
        print("我誕生了")
        self.do_hw("英文")
        self.study()
        self.sleep()
    def do_hw(self, hw):
        print("我在做作業", hw)
    def study(self):
        print("我在讀書")
    def sleep(self):
        print("I am sleeping!")

s = Student()
print(dir(s))
