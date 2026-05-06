class Calculator:
    def __init__(self, a, b):
        self.a = a  
        self.b = b

    def get_sum(self):
        return self.a + self.b
        
        #Add the methods for subtraction, division and multitplication

    def get_subtraction(self):
        return self.a - self.b
    
    def get_multiplication(self):
        return self.a * self.b
    
    def get_division(self):
        return self.a / self.b
    

    
myCalc = Calculator(a=3,b=5)
print(myCalc.get_sum())
print(myCalc.get_subtraction())