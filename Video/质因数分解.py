def prime_factors(n):
    while n > 1:
        k = smallest_prime_factor(n)
        n //= k 
        print(k)

def smallest_prime_factor(n):
    k = 2
    while n % k != 0:
        k += 1
    return k 