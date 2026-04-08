class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):
        # print("This method will be called when you run print(object)")
        return "{}/{}".format(self.num,self.den)
         


x=Fraction(3,5)
print(x)   
# <__main__.Fraction object at 0x0000018270B78C20>  This is the output of the print(x) before
#  __str__ magic method is created bcz 
# we haven't defined how to display the Fraction object yet, so it is directly provideing the 
# address of the x object