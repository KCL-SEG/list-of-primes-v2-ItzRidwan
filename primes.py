"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'Number of primes is {number_of_primes} but it has to be positive')
    list = []
    i=1
    while len(list) < number_of_primes:
        factorList = []
        for n in range(1,i+1):
            if i%n == 0:
                factorList.append(n)
            elif len(factorList) > 2:
                break
        if len(factorList) == 2:
            list.append(i)
        i += 1
    return list