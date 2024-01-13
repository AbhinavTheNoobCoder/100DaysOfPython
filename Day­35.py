#DAY 35 - for-else and while-else statements
def PrimeOrNot(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        else:
            return True

def FindingPrimes(start_value, end_value):
    primes = []
    for i in range(start_value, end_value + 1):
        if PrimeOrNot(i):
            primes.append(i)
    return primes
        
start = int(input("Enter start value of range: "))
end = int(input("Enter end value of range: "))
print(f"Primes numbers between {start} and {end} are", FindingPrimes(start, end))