# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def the_sum_of_the_squares(n):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i ** 2
    return sum1

def the_square_of_the_sum(n):
    sum2 = 0
    for i in range(1, n + 1):
        sum2 += i
    return sum2 ** 2

def find_the_difference(n):
    return the_square_of_the_sum(n) - the_sum_of_the_squares(n)

n = int(input("n: "))    # the first " n " natural numbers
print("ans:", find_the_difference(n))