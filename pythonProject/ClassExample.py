class Calculator:
    value = 500

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def Summation(self):
        print("I got executed")

    def adder(self):
        return self.a + self.b + Calculator.value


obj = Calculator(100, 400)

obj.adder()


class Chinnavan(Calculator):
    value1 = 5000

    def __init__(self, c, d):
        Calculator.__init__(self, c, d)
        self.c = c
        self.d = d

    def final_adder(self):
        return self.c + self.d + self.adder() + Chinnavan.value1 + self.value


obj1 = Chinnavan(200, 400)
print(obj1.final_adder())
