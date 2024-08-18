# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_the_sum(n):
    prime_sum = 0
    for i in range(2, n):
        if is_prime(i):
            prime_sum += i
    return prime_sum

n = int(input("n: "))   # all the primes below " n "
print("ans:", find_the_sum(n))