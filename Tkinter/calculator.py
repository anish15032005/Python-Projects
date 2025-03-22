class Calculator:
    def add(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
    def factorial(self,a):
        if a==0:
            return 1
        else:
            return a*self.factorial(a-1)
        
    def power(self,a,b):
        return a**b  
      
    def square_root(self,a):
        return a**(1/2)
    
calc = Calculator()

print(f"2+3 = {calc.add(2,3)}")
print(f"2-3 = {calc.substract(2,3)}")
print(f"2*3 = {calc.multiply(2,3)}")
print(f"2/3 = {calc.divide(2,3)}")
print(f"5! = {calc.factorial(5)}")
print(f"2^3 = {calc.power(2,3)}")
print(f"sqrt(4) = {calc.square_root(4)}")

