# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True 

def find_prime(n):
    num = 2
    count = 0
    while True:
        if is_prime(num):
            count += 1
            if n == count:
                return num
        num += 1

n = int(input("n: "))    # the " n " prime number
print("ans:", find_prime(n))