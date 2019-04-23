##Check Prime
def checkPrime(number):
    if number ==1 or number==0:
        return False
    for x in range(2,number):
        if number%x == 0:
            return False
    return True
##Finding Ranges of prime
def primeBetweenRange(lower,upper):
    for i in range(lower,upper+1):
        if checkPrime(i):
        	yield i
