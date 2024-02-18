

class calculator:
    brand='CASIO991EX'
    price = 4000


    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 / num2
    def factrorial(self,n):
        if n==1 or n==0:
            return 1
        else:
            result =1
            for i in range(1,n+1,1):
                result = result *i
                # return result 
            return result 
        # return num1 + num2

    def rev(self, n):
        return 1/n
    
    def modulus(self, n):
        if n>=0:
            return n
        else:
            return -(n)



calculate = calculator()

print(calculate.addition(10,20))
print(calculate.subtraction(100,20))
print(calculate.multiplication(10,20))
print(calculate.division(20,10))
print(calculate.factrorial(5))
print(calculate.rev(5))
print(calculate.modulus(-5))
# print(calculate.modulus(-5)