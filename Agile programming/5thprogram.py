class calculator:
    def Calculate (self,a,b,operation):
        if operation =="add":
            return a+b
        elif operation =="sub":
            return a-b
        elif operation =="mul":
            return a*b
        elif operation =="div":
            if b==0:
                raise ValueError("Divison by zero!")
            return a/b
        else:
            raise ValueError("Invalidoperation")
if __name__ =="__main__":
    calc=calculator()
    print("10+5=",calc.Calculate(10,5,"add"))
    print("10-5=",calc.Calculate(10,5,"sub"))
    print("10*5=",calc.Calculate(10,5,"mul"))
    print("10/5=",calc.Calculate(10,5,"div"))