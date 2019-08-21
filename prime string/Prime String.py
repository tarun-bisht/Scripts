def CheckPrimeString(n):
    i=2
    string=n
    while len(n)>1:
        mid=(len(n)+1)//2
        n=n[:mid]
        if n*i==string:
            return string+" Not Prime String"
        i+=1
    return string+" Prime String"
string=input("Enter String to Check: ")
print(CheckPrimeString(string))
