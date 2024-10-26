class Electronics:


    def __init__(self,a,b):
        print("I'm constructor. I got executed")
        self.a = a
        self.b = b

    def mobile(self):
        print("Hi! I'm mobile. I got executed")

    def mobile_price(self):
        return self.a + self.b


obj = Electronics(2,4)
obj.mobile()
result = obj.mobile_price()
print(result)

print("_________________________")

