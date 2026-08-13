from abc import ABC,abstractmethod
class Operation(ABC):
    @abstractmethod
    def execute(self,a,b):
        pass
class Add(Operation):
    def execute(self, a, b):
        return a+b
class Sub(Operation):
    def execute(self, a, b):
        return a-b
class mul(Operation):
    def execute(self, a, b):
        return a*b
class div(Operation):
    def execute(self, a, b):
        if b==0:
            raise ValueError("Division by zero!")
        return a/b
class calculator:
    def __init__(self,Operation:Operation):
        self.Operation=Operation
    def calculator(self,a,b):
        return self.Operation.execute(a,b)
if __name__=="__main__":
    add_calc=calculator(Add())
    print("10+5=".add_calc.calculator(10,5))
    sub_calc=calculator(Sub())
    print("10-5=".add_calc.calculator(10,5))
    mul_calc=calculator(mul())
    print("10*5=".add_calc.calculator(10,5))
    div_calc=calculator(div())
    print("10/5=".add_calc.calculator(10,5))






