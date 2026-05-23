import string
class carbody:
    model:string
    color:string
    wheel:int
    def open(self):
        print(f"{self.color}{self.model}车门已打开")
    def close(self):
        print(f"{self.color}{self.model}车门已关闭")

class engine:
    type:string
    power:float
    def start(self):
        print(f"{self.type}型{self.power}Kw功率发动机已启动")
    def close(self):
        print(f"{self.type}型{self.power}Kw功率发动机已关闭")

class control:
    def forward(self):
        print("汽车前进中")
    def backward(self):
        print("汽车倒退中")
    def quicken(self):
        print("汽车加速")
    def slowdown(self):
        print("汽车减速")
    def stop(self):
        print("汽车已关闭")


class CAR:
    body:carbody
    engine:engine
    control:control
    def car_info(self):
        print('='*30)

