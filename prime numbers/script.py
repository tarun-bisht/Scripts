##Taking Input
try:
    print(":::CHOICE:::\n\t1: For checking a number for prime\n\t2: Finding Prime Number between a range")
    choice=eval(input("Enter Your Choice: "))
except Exception as e:
    print(f"Cannot take Choice:: {e}")
## Choice 1 for checking prime numbers
if choice==1:
    from prime import checkPrime
    try:
        a=eval(input("enter number to check: "))
    except Exception as e:
        print(f"Cannot take input:: {e}")
    if checkPrime(a):
    	print("Number is Prime")
    else:
    	print("Number is not Prime")
## Choice 2 for finding prime number between ranges
elif choice==2:
    from prime import primeBetweenRange
    try:
        p=eval(input("Enter Lower Limit of Range: "))
        q=eval(input("Enter Upper Limit of Range: "))
    except Exception as e:
        print(f"Cannot take input:: {e}")
    print(f"PRIME NUMBERS BETWEEN RANGE {p} - {q}")
    for i in primeBetweenRange(p,q):
        print(i)
else:
    print("Wrong Choice Entered")
input("Enter Button to Exit")
