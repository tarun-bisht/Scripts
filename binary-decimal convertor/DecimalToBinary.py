
# coding: utf-8

def DtoB(num):
    if num==0:
       return "0"    
    rem=0
    binary=""
    while num>=1:
        rem=num%2
        num=num//2
        binary=binary+str(rem)
    return binary

print("Decimal to Binary Convertor: ")
a=eval(input("Enter Number To Convert into Binary: "))
binary=DtoB(a)
binary=binary[::-1]
print(binary)

