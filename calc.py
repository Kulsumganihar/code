import math as m

class calc:

    def add(self,num1,num2):
        return num1 + num2

    def sub(self,num1,num2):
        return num1 - num2

    def mul(self,num1,num2):
        return num1 * num2

    def div(self,num1,num2):
        if num2 == 0:
            raise ZeroDivisionError
        else:
            return num1 / num2
