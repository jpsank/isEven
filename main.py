import re


def primeNumbersLessThan(n):
    # gets all prime numbers less than n
    primes = []
    for i in range(n-2):
        i = n-1-i
        isPrime = True
        for x in range(2,int(i/2)+1):
            if re.match(r'\d+\.0\Z',str(i/x)):
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes


def goldbachIsEven(n):
    # Checks for even using Goldbach's conjecture, which states that every even integer greater than 2
    # can be represented as a sum of two prime numbers.
    # Also uses the laws of addition and subtraction for even and odd numbers:
    # even ± even = even, even ± odd = odd, and odd ± odd = even
    # See Wikipedia page: https://en.wikipedia.org/wiki/Parity_(mathematics)
    # Disclaimer: numbers in the thousands may start to take a while
    if n == 0 or n == 2:
        return True
    elif n == 1:
        return False
    primes = primeNumbersLessThan(n)
    for p in primes:
        for p2 in primes:
            if p+p2 == n:
                if goldbachIsEven(p) == goldbachIsEven(p2):
                    return True
    return False


print(goldbachIsEven(21))