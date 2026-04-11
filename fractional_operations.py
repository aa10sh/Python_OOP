class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):
        # print("This method will be called when you run print(object)")
        return "{}/{}".format(self.num,self.den)
    def __add__(self, other):
        temp_num=self.num*other.den + other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    def __sub__(self, other):
        temp_num=self.num*other.den - other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __mul__(self, other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __truediv__(self, other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        return "{}/{}".format(temp_num,temp_den)


# x=Fraction(3,5)
# print(x)   
# <__main__.Fraction object at 0x0000018270B78C20>  This is the output of the print(x) before
#  __str__ magic method is created bcz 
# we haven't defined how to display the Fraction object yet, so it is directly provideing the 
# address of the x object
a=Fraction(4,6)
b=Fraction(5,6)
print(a+b)
print(a-b)
print(a*b)
print(a/b)