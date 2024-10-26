from Sample import Calculator

class childImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,10)

    def getcompletedata(self):
        return childImpl.num2 + self.num + self.Summation()

obj = childImpl()
result1 = obj.getcompletedata()
print(result1)
