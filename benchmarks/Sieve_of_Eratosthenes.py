import time


def Sieve_of_Eratosthenes_local(limit):
    # Create a boolean array "is_prime[0..limit]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    # Create a list of all prime numbers
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    
    return primes

def benchmark():
    start = time.time()
    Sieve_of_Eratosthenes_local(10000)
    end = time.time()
    return end - start