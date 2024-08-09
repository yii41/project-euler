# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible(n, num):
    for i in range(2, n+1):
        if num % i != 0:
            return False
    return True

def find_the_smallest_number(n):
    num = 1
    while True:
        if is_divisible(n, num):
            return num
        num += 1

n = int(input("n: "))   # from 1 to n
print("ans:", find_the_smallest_number(n))