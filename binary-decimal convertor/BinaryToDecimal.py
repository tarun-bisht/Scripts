
# coding: utf-8
def DtoB(num):
    if num=="0":
       return num 
    decimal=0
    i=len(num)-1
    x=0
    while i>=0:
            decimal=decimal+int(num[i])*(2**x)
            x=x+1
            i=i-1
    return decimal

print("Decimal to Binary Convertor: ")
a=input("Enter Binary Number To Convert into Decimal: ")
decimal=DtoB(a)
#decimal=decimal[::-1]
print(decimal)

