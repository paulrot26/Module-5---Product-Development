from calculator import Calculator

myCalcV2 = calculator(2,9)

class SciCalc(calculator):
        def get_exp(self):
                return self.a**self.b
        
mySciCalc = SciCalc(a=2,b=4)
print(mySciCalc.get_exp())